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

No changes yet. This will be updated in Phase 2 once the logic is written.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

The scheduler considers time (HH:MM), priority level (low, medium, high), and task frequency (once, daily, weekly). Time was treated as the most important constraint because a pet owner needs to know what to do and when. Priority is stored on each task but sorting is done by time, not priority, since a "low priority" grooming at 10:00 still needs to happen before a "high priority" walk at 18:00.

**b. Tradeoffs**

The conflict detection only flags tasks that share the exact same time string. It does not check whether a 30-minute task at 08:00 overlaps with a task at 08:15. This is a reasonable tradeoff for a simple app because exact time matching is easy to understand and does not require tracking task end times, which would make the scheduler more complex without adding much value for most users.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
