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
    time: str                        # "HH:MM" format, e.g. "08:00"
    duration_minutes: int
    priority: str = "medium"         # "low" | "medium" | "high"
    frequency: str = "once"          # "once" | "daily" | "weekly"
    is_complete: bool = False
    due_date: date = field(default_factory=date.today)

    def mark_complete(self) -> None:
        """Mark this task as complete."""
        pass

    def reschedule(self) -> None:
        """Create the next occurrence date based on frequency."""
        pass


# ---------------------------------------------------------------------------
# Pet
# ---------------------------------------------------------------------------

@dataclass
class Pet:
    """Stores pet details and owns a list of Tasks."""

    name: str
    species: str                     # "dog" | "cat" | "other"
    breed: str = ""
    age: int = 0
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list."""
        pass

    def remove_task(self, title: str) -> None:
        """Remove a task by title."""
        pass

    def get_tasks(self) -> list[Task]:
        """Return all tasks for this pet."""
        pass


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
        pass

    def get_all_tasks(self) -> list[Task]:
        """Return every task across all pets."""
        pass


# ---------------------------------------------------------------------------
# Scheduler
# ---------------------------------------------------------------------------

class Scheduler:
    """The 'brain' — retrieves, organizes, and manages tasks across pets."""

    def __init__(self, owner: Owner) -> None:
        """Initialise with an Owner instance."""
        self.owner = owner

    def get_todays_schedule(self) -> list[Task]:
        """Return all tasks due today, sorted by time."""
        pass

    def sort_by_time(self, tasks: list[Task]) -> list[Task]:
        """Return tasks sorted chronologically by their time attribute."""
        pass

    def filter_tasks(
        self,
        pet_name: str | None = None,
        is_complete: bool | None = None,
    ) -> list[Task]:
        """Filter tasks by pet name and/or completion status."""
        pass

    def detect_conflicts(self) -> list[str]:
        """Return warning strings for any two tasks scheduled at the same time."""
        pass

    def mark_task_complete(self, pet_name: str, title: str) -> None:
        """Mark a specific task complete and reschedule if recurring."""
        pass
