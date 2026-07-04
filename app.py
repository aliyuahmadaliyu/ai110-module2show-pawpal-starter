import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")
st.title("🐾 PawPal+")

# Keep the Owner alive across reruns
if "owner" not in st.session_state:
    st.session_state.owner = None

# -----------------------------------------------------------------------
# Step 1: Set up the owner
# -----------------------------------------------------------------------
st.header("Owner Setup")

owner_name = st.text_input("Your name", value="Aliyu")

if st.button("Set Owner"):
    st.session_state.owner = Owner(name=owner_name)
    st.success(f"Owner set to {owner_name}")

if st.session_state.owner is None:
    st.info("Set your name above to get started.")
    st.stop()

owner = st.session_state.owner

# -----------------------------------------------------------------------
# Step 2: Add a pet
# -----------------------------------------------------------------------
st.divider()
st.header("Add a Pet")

col1, col2, col3, col4 = st.columns(4)
with col1:
    pet_name = st.text_input("Pet name")
with col2:
    species = st.selectbox("Species", ["dog", "cat", "other"])
with col3:
    breed = st.text_input("Breed")
with col4:
    age = st.number_input("Age", min_value=0, max_value=30, value=1)

if st.button("Add Pet"):
    if pet_name.strip() == "":
        st.warning("Please enter a pet name.")
    elif any(p.name == pet_name for p in owner.pets):
        st.warning(f"{pet_name} is already added.")
    else:
        owner.add_pet(Pet(name=pet_name, species=species, breed=breed, age=age))
        st.success(f"Added {pet_name} the {species}!")

if owner.pets:
    st.write("Your pets:", ", ".join(p.name for p in owner.pets))

# -----------------------------------------------------------------------
# Step 3: Add a task
# -----------------------------------------------------------------------
st.divider()
st.header("Schedule a Task")

if not owner.pets:
    st.info("Add a pet first before scheduling tasks.")
else:
    pet_names = [p.name for p in owner.pets]

    col1, col2, col3 = st.columns(3)
    with col1:
        selected_pet = st.selectbox("Pet", pet_names)
        task_title = st.text_input("Task title", value="Morning walk")
    with col2:
        task_time = st.text_input("Time (HH:MM)", value="08:00")
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    with col3:
        priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
        frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])

    if st.button("Add Task"):
        if task_title.strip() == "":
            st.warning("Please enter a task title.")
        else:
            for pet in owner.pets:
                if pet.name == selected_pet:
                    pet.add_task(Task(
                        title=task_title,
                        time=task_time,
                        duration_minutes=duration,
                        priority=priority,
                        frequency=frequency,
                    ))
                    st.success(f"Added '{task_title}' for {selected_pet} at {task_time}.")

# -----------------------------------------------------------------------
# Step 4: Generate schedule
# -----------------------------------------------------------------------
st.divider()
st.header("Todays Schedule")

if st.button("Generate Schedule"):
    scheduler = Scheduler(owner)
    schedule = scheduler.get_todays_schedule()
    conflicts = scheduler.detect_conflicts()

    if conflicts:
        for warning in conflicts:
            st.warning(warning)

    if not schedule:
        st.info("No tasks scheduled for today.")
    else:
        rows = []
        for task in schedule:
            rows.append({
                "Time": task.time,
                "Task": task.title,
                "Pet": next((p.name for p in owner.pets if task in p.tasks), ""),
                "Priority": task.priority,
                "Done": "Yes" if task.is_complete else "No",
            })
        st.table(rows)
