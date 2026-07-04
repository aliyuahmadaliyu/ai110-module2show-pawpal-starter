from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import date, timedelta


def make_scheduler():
    owner = Owner(name="Aliyu")
    dog = Pet(name="Biscuit", species="dog")
    cat = Pet(name="Mochi", species="cat")
    dog.add_task(Task(title="Morning walk",  time="08:00", duration_minutes=30, priority="high",  frequency="daily"))
    dog.add_task(Task(title="Medication",    time="12:00", duration_minutes=5,  priority="high"))
    cat.add_task(Task(title="Feeding",       time="08:00", duration_minutes=5,  priority="medium", frequency="daily"))
    owner.add_pet(dog)
    owner.add_pet(cat)
    return Scheduler(owner)


# Task completion test
def test_mark_complete_changes_status():
    task = Task(title="Walk", time="09:00", duration_minutes=20)
    assert task.is_complete is False
    task.mark_complete()
    assert task.is_complete is True


# Task addition test
def test_add_task_increases_count():
    pet = Pet(name="Biscuit", species="dog")
    assert len(pet.get_tasks()) == 0
    pet.add_task(Task(title="Walk", time="08:00", duration_minutes=20))
    assert len(pet.get_tasks()) == 1


# Sorting test
def test_sort_by_time_returns_chronological_order():
    scheduler = make_scheduler()
    tasks = scheduler.owner.get_all_tasks()
    sorted_tasks = scheduler.sort_by_time(tasks)
    times = [t.time for t in sorted_tasks]
    assert times == sorted(times)


# Recurrence test
def test_daily_task_reschedules_to_next_day():
    task = Task(title="Feeding", time="08:00", duration_minutes=10, frequency="daily")
    today = task.due_date
    task.mark_complete()
    task.reschedule()
    assert task.due_date == today + timedelta(days=1)
    assert task.is_complete is False


# Conflict detection test
def test_conflict_detected_for_same_time():
    scheduler = make_scheduler()
    conflicts = scheduler.detect_conflicts()
    assert len(conflicts) > 0
    assert "08:00" in conflicts[0]
