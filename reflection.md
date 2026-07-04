# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

The three core actions a user should be able to perform:
1. Add a pet by entering its name, species, breed, and age.
2. Schedule a task (like a walk, feeding, or medication) for a specific pet with a time, duration, and priority.
3. View todays schedule sorted by time, with warnings if two tasks clash.

Four classes were chosen:

Task holds all the data for a single care activity like the title, time, duration, priority, frequency, completion status, and due date. It is only responsible for its own data and rescheduling itself.

Pet stores the pets info and keeps a list of its tasks. It handles adding and removing tasks from that list.

Owner holds all the pets and gives one place to access every task across all of them.

Scheduler is the brain. It takes an Owner and handles sorting, filtering, conflict detection, and marking tasks complete.

**b. Design changes**

One change I made was moving the reschedule logic into the Task class instead of keeping it all inside the Scheduler. It made more sense for the task to know how to reschedule itself rather than having the Scheduler do it. That kept each class focused on its own job.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers time (HH:MM), priority level (low, medium, high), and task frequency (once, daily, weekly). Time was treated as the most important constraint because a pet owner needs to know what to do and when. Priority is stored on each task but sorting is done by time, not priority, since a low priority grooming at 10:00 still needs to happen before a high priority walk at 18:00.

**b. Tradeoffs**

The conflict detection only flags tasks that share the exact same time string. It does not check whether a 30-minute task at 08:00 overlaps with a task at 08:15. This is a reasonable tradeoff for a simple app because exact time matching is easy to understand and does not require tracking task end times, which would make the scheduler more complex without adding much value for most users.

---

## 3. AI Collaboration

**a. How you used AI**

I used AI mostly for generating the initial class skeletons and method stubs after I had already decided what classes I wanted. I also used it to help write the test cases once I knew what behaviors I wanted to test. The most useful prompts were specific ones like asking how to sort a list of objects by a string attribute, or asking what edge cases to cover in a scheduling app.

**b. Judgment and verification**

At one point the AI added type hint syntax that was not supported in Python 3.9, using things like list[Task] directly without importing from typing. I caught this when running the code and had to check which Python version the project was using before deciding to keep the syntax since we were on 3.13 where it works fine. I always ran the code myself to verify things actually worked before moving on.

---

## 4. Testing and Verification

**a. What you tested**

I tested task completion, task addition, sorting by time, daily and weekly recurrence, conflict detection, filtering by pet name, and edge cases like a pet with no tasks or an owner with no pets. These were important because they cover the core behaviors the scheduler depends on. If any of these broke, the whole app would stop working correctly.

**b. Confidence**

I am fairly confident the scheduler works correctly for normal use. All 11 tests pass. The main thing I would test next is overlapping task durations, for example a 45-minute task at 08:00 and a task at 08:30 should probably also trigger a conflict warning but currently does not.

---

## 5. Reflection

**a. What went well**

The class design worked out well. Keeping Task, Pet, Owner, and Scheduler as separate classes made it easy to add new features without breaking existing ones. Adding a new method to Scheduler did not require touching any other class.

**b. What you would improve**

I would improve the conflict detection to account for task duration, not just start time. Right now two tasks can technically overlap and the app would not catch it. I would also add the ability to remove a pet from the owner's list in the UI.

**c. Key takeaway**

The biggest thing I learned is that you have to design the system before writing any code. When I knew exactly what each class was responsible for, writing the actual logic was straightforward. AI is useful for filling in the details but it cannot figure out the design for you, that part still requires thinking it through yourself.
