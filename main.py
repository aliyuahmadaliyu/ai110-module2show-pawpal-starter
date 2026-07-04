from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import date

# Setup
owner = Owner(name="Aliyu")

dog = Pet(name="Biscuit", species="dog", breed="Golden Retriever", age=3)
cat = Pet(name="Mochi", species="cat", breed="Tabby", age=2)

# Tasks added out of order on purpose to test sorting
dog.add_task(Task(title="Evening walk",    time="18:00", duration_minutes=30, priority="high",   frequency="daily"))
dog.add_task(Task(title="Morning feeding", time="08:00", duration_minutes=10, priority="high",   frequency="daily"))
dog.add_task(Task(title="Medication",      time="12:00", duration_minutes=5,  priority="high"))

cat.add_task(Task(title="Grooming",        time="10:00", duration_minutes=15, priority="low"))
cat.add_task(Task(title="Feeding",         time="08:00", duration_minutes=5,  priority="high",   frequency="daily"))

owner.add_pet(dog)
owner.add_pet(cat)

scheduler = Scheduler(owner)

# 1. Sorting
print("=" * 45)
print("  1. Todays Schedule (sorted by time)")
print("=" * 45)
for task in scheduler.get_todays_schedule():
    status = "Done" if task.is_complete else "Pending"
    print(f"  {task.time}  {task.title:<20} [{task.priority}] [{status}]")

# 2. Conflict detection
print("\n2. Conflict Detection:")
conflicts = scheduler.detect_conflicts()
if conflicts:
    for w in conflicts:
        print(f"  WARNING: {w}")
else:
    print("  No conflicts found.")

# 3. Filtering by pet
print("\n3. Filter by pet (Biscuit only):")
for task in scheduler.filter_tasks(pet_name="Biscuit"):
    print(f"  {task.time}  {task.title}")

# 4. Filtering by completion status
print("\n4. Filter incomplete tasks only:")
for task in scheduler.filter_tasks(is_complete=False):
    print(f"  {task.time}  {task.title}")

# 5. Recurring tasks
scheduler.mark_task_complete("Biscuit", "Morning feeding")
print("\n5. Recurring task rescheduled after completion:")
for task in dog.get_tasks():
    if task.title == "Morning feeding":
        print(f"  is_complete: {task.is_complete}  next due: {task.due_date}")
