# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

```
=============================================
         Todays Schedule
=============================================
  08:00  Morning feeding      [high] [Pending]
  08:00  Feeding              [high] [Pending]
  10:00  Grooming             [low] [Pending]
  12:00  Medication           [high] [Pending]
  18:00  Evening walk         [high] [Pending]

Conflict check:
  WARNING: Conflict at 08:00: 'Morning feeding' and 'Feeding'

Biscuits tasks only:
  18:00  Evening walk
  08:00  Morning feeding
  12:00  Medication

After marking Morning feeding complete:
  is_complete: False  next due: 2026-07-05
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
================================================= test session starts ==================================================
platform win32 -- Python 3.13.14, pytest-9.1.1, pluggy-1.6.0
collected 11 items

tests/test_pawpal.py::test_mark_complete_changes_status PASSED                                                    [  9%]
tests/test_pawpal.py::test_add_task_increases_count PASSED                                                        [ 18%]
tests/test_pawpal.py::test_sort_by_time_returns_chronological_order PASSED                                        [ 27%]
tests/test_pawpal.py::test_daily_task_reschedules_to_next_day PASSED                                              [ 36%]
tests/test_pawpal.py::test_conflict_detected_for_same_time PASSED                                                 [ 45%]
tests/test_pawpal.py::test_pet_with_no_tasks_returns_empty_list PASSED                                            [ 54%]
tests/test_pawpal.py::test_owner_with_no_pets_returns_no_tasks PASSED                                             [ 63%]
tests/test_pawpal.py::test_weekly_task_reschedules_to_next_week PASSED                                            [ 72%]
tests/test_pawpal.py::test_once_task_does_not_reschedule PASSED                                                   [ 81%]
tests/test_pawpal.py::test_filter_by_pet_name_returns_only_that_pets_tasks PASSED                                 [ 90%]
tests/test_pawpal.py::test_no_conflicts_when_all_tasks_at_different_times PASSED                                  [100%]
================================================== 11 passed in 0.12s ==================================================
```

Confidence level: ⭐⭐⭐⭐ — core behaviors and edge cases all pass. The main untested area is the Streamlit UI itself.

## 📐 Smarter Scheduling

| Feature | Method | Notes |
|---------|--------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Sorts all tasks by HH:MM time string so the schedule always reads chronologically |
| Filtering | `Scheduler.filter_tasks()` | Filters by pet name, completion status, or both |
| Conflict detection | `Scheduler.detect_conflicts()` | Checks if two tasks share the same time and returns a warning string instead of crashing |
| Recurring tasks | `Task.reschedule()` | When a daily or weekly task is marked complete, the due date moves forward automatically and the task resets to incomplete |

## 📸 Demo Walkthrough

1. Open the app with `streamlit run app.py` and go to http://localhost:8501
2. Enter your name and click Set Owner to create an owner object in session state
3. Add two pets by filling in the name, species, breed and age fields and clicking Add Pet
4. For each pet, add a few tasks with different times, priorities, and frequencies
5. Give two pets the same time on purpose to see the conflict warning appear
6. Click Generate Schedule to see all tasks sorted by time in a table
7. Any conflicts show as yellow warnings above the table

Key scheduler behaviors shown:
- Tasks always appear in chronological order regardless of the order they were added
- Conflict warnings appear automatically when two tasks share the same time
- Daily and weekly tasks reschedule themselves when marked complete
- You can filter the schedule by pet name or completion status

Sample CLI output from `python main.py`:

```
=============================================
  1. Todays Schedule (sorted by time)
=============================================
  08:00  Morning feeding      [high] [Pending]
  08:00  Feeding              [high] [Pending]
  10:00  Grooming             [low] [Pending]
  12:00  Medication           [high] [Pending]
  18:00  Evening walk         [high] [Pending]

2. Conflict Detection:
  WARNING: Conflict at 08:00: 'Morning feeding' and 'Feeding'

3. Filter by pet (Biscuit only):
  18:00  Evening walk
  08:00  Morning feeding
  12:00  Medication

4. Filter incomplete tasks only:
  18:00  Evening walk
  08:00  Morning feeding
  12:00  Medication
  10:00  Grooming
  08:00  Feeding

5. Recurring task rescheduled after completion:
  is_complete: False  next due: 2026-07-04
```
