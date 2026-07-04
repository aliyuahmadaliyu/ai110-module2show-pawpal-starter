"""
PawPal+ — Logic Layer
All backend classes live here. The Streamlit UI in app.py imports from this module.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date


# ---------------------------------------------------------------------------
# Task
# ---------------------------------------------------------------------------

@dataclass
class Task:
    """Represents a single pet care activity."""

    title: str
    time: str                        # HH:MM format, e.g. 08:00
    duration_minutes: int
    priority: str = "medium"         # low, medium, or high
    frequency: str = "once"          # once, daily, or weekly
    is_complete: bool = False
    due_date: date = field(default_factory=date.today)

    def mark_complete(self) -> None:
        """Mark this task as complete."""
        self.is_complete = True

    def reschedule(self) -> None:
        """Move due_date forward based on frequency (daily or weekly)."""
        from datetime import timedelta
        if self.frequency == "daily":
            self.due_date = self.due_date + timedelta(days=1)
            self.is_complete = False
        elif self.frequency == "weekly":
            self.due_date = self.due_date + timedelta(weeks=1)
            self.is_complete = False


# ---------------------------------------------------------------------------
# Pet
# ---------------------------------------------------------------------------

@dataclass
class Pet:
    """Stores pet details and owns a list of Tasks."""

    name: str
    species: str                     # dog, cat, or other
    breed: str = ""
    age: int = 0
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list."""
        self.tasks.append(task)

    def remove_task(self, title: str) -> None:
        """Remove a task by title."""
        self.tasks = [t for t in self.tasks if t.title != title]

    def get_tasks(self) -> list[Task]:
        """Return all tasks for this pet."""
        return self.tasks


# ---------------------------------------------------------------------------
# Owner
# ---------------------------------------------------------------------------

@dataclass
class Owner:
    """Manages one or more pets."""

    name: str
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's roster."""
        self.pets.append(pet)

    def get_all_tasks(self) -> list[Task]:
        """Return every task across all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


# ---------------------------------------------------------------------------
# Scheduler
# ---------------------------------------------------------------------------

class Scheduler:
    """The brain. Retrieves, organizes, and manages tasks across pets."""

    def __init__(self, owner: Owner) -> None:
        """Initialise with an Owner instance."""
        self.owner = owner

    def get_todays_schedule(self) -> list[Task]:
        """Return all tasks due today, sorted by time."""
        from datetime import date
        today = date.today()
        todays_tasks = [t for t in self.owner.get_all_tasks() if t.due_date == today]
        return self.sort_by_time(todays_tasks)

    def sort_by_time(self, tasks: list[Task]) -> list[Task]:
        """Return tasks sorted chronologically by their time attribute."""
        return sorted(tasks, key=lambda t: t.time)

    def filter_tasks(
        self,
        pet_name: str | None = None,
        is_complete: bool | None = None,
    ) -> list[Task]:
        """Filter tasks by pet name and/or completion status."""
        results = []
        for pet in self.owner.pets:
            if pet_name and pet.name != pet_name:
                continue
            for task in pet.get_tasks():
                if is_complete is not None and task.is_complete != is_complete:
                    continue
                results.append(task)
        return results

    def detect_conflicts(self) -> list[str]:
        """Return warning strings for any two tasks scheduled at the same time."""
        all_tasks = self.owner.get_all_tasks()
        seen = {}
        warnings = []
        for task in all_tasks:
            if task.time in seen:
                warnings.append(
                    f"Conflict at {task.time}: '{seen[task.time]}' and '{task.title}'"
                )
            else:
                seen[task.time] = task.title
        return warnings

    def mark_task_complete(self, pet_name: str, title: str) -> None:
        """Mark a specific task complete and reschedule if recurring."""
        for pet in self.owner.pets:
            if pet.name == pet_name:
                for task in pet.get_tasks():
                    if task.title == title:
                        task.mark_complete()
                        if task.frequency in ("daily", "weekly"):
                            task.reschedule()
