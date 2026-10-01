# Seed Content Pack — Exercise 1 (Executive Command Center)

> **For the host.** New workshop accounts have empty mailboxes and calendars, so the Exercise 1
> command center has nothing to work with. Load the items below into **each attendee account**
> **1–2 days before the session**, so they count as "today and this week."
>
> All content is **fictional Zava** material. What the command center should surface is in the
> [facilitator answer key](facilitator-answer-key.md#exercise-1--executive-command-center).

## How to send it

- **Senders:** create 2–3 extra accounts in the attendee tenant to send from (e.g., *Avery Quinn* as
  "HR Manager," *Zava Communications*, *Jordan Lee*). Optionally set each attendee's **manager** to
  Avery Quinn in the Microsoft 365 admin center (**Users → Manager**), so the command center can
  recognize requests from the manager.
- **Delivery:** send by hand, or script it with Microsoft Graph (`sendMail` / `events`) or
  PowerShell. Script it for 25 accounts.
- Replace `{attendee}` with each attendee's display name, and `{Thursday}` etc. with real dates in
  the workshop week.

---

## A. Emails (7)

### 1. Manager request (a commitment with a deadline)
- **From:** Avery Quinn (HR Manager) · **Importance:** Normal
- **Subject:** Q4 onboarding plan — need your input by Thursday
- **Body:**
  > Hi {attendee}, can you review the draft Q4 onboarding plan and send me your top 3 changes by
  > Thursday EOD? Focus especially on first-week scheduling and the benefits-enrollment reminder.
  > Thanks, Avery

### 2. Urgent payroll issue (urgent; high importance)
- **From:** Owen Wright (Support Agent) · **Importance:** **High**
- **Subject:** URGENT: Payroll correction needed for T-2008
- **Body:**
  > Hi, my overtime hours from last pay period are still missing from my paycheck (ticket T-2008).
  > Rent is due Friday. Can someone confirm today when this will be corrected? Thank you, Owen

### 3. Newsletter (background noise)
- **From:** Zava Communications · **Importance:** Low
- **Subject:** Zava Weekly: Office updates & wellness tips
- **Body:**
  > This week at Zava: the Seattle office café reopens Monday; October wellness challenge sign-ups are
  > open ($50/month wellness stipend reminder); Tuesday and Thursday remain anchor days; and a reminder
  > that open enrollment is in November. Have a great week!

### 4. Meeting invite (send as an accepted meeting)
- **Type:** Meeting request · **From:** Avery Quinn
- **Subject:** Benefits Open Enrollment Kickoff
- **When:** {Wednesday}, 2:00–2:30 PM · **Teams meeting:** yes
- **Body:**
  > Kickoff for November open enrollment planning: timeline, comms plan, and FAQ owners.

### 5. Employee question (waiting on a reply)
- **From:** Dana Kim (Sales Development Rep) · **Importance:** Normal
- **Subject:** Quick question about the training budget
- **Body:**
  > Hi HR team, can I use my training budget for a sales conference in December? How much is left for
  > this year, and what do I need to submit? Thanks! Dana

### 6. FYI update (background noise)
- **From:** Zava Communications · **Importance:** Normal
- **Subject:** FYI: Updated remote work FAQ posted
- **Body:**
  > FYI: the remote-work FAQ on the HR portal has been updated with the fully-remote approval process
  > (VP approval plus a signed agreement) and the $300 home-office stipend details. No action needed.

### 7. Recruiting thread (a decision waiting on you)
- **From:** Hana Suzuki (Recruiter) · **Importance:** Normal
- **Subject:** Re: Interview panel for HR Coordinator
- **Body:**
  > Hi {attendee}, can you join the HR Coordinator interview panel on {Friday} at 10:00? If not, who
  > should I ask instead? I'll send the scorecard once the panel is confirmed. — Hana

---

## B. Calendar events (3)

| # | Title | When | Notes |
| --- | --- | --- | --- |
| 1 | HR leadership sync | {Thursday} 10:00–11:00 | Organizer: Avery Quinn. Agenda: Q4 onboarding plan, T-2008 escalation |
| 2 | Candidate interview — HR Coordinator | {Thursday} **10:30–11:15** | **Deliberately overlaps #1**, so the command center should flag a **conflict** |
| 3 | Benefits Open Enrollment Kickoff | {Wednesday} 14:00–14:30 | Same as email #4; add it to each attendee's calendar as accepted |

Optional: add one **declined or quiet** recurring meeting (e.g., "Monthly engagement survey review",
no activity in 6 weeks). It gives the command center's **Org pulse** view a "gone quiet" signal.

---

## C. Teams chat (optional)

A 1:1 chat from **Avery Quinn** to the attendee:

> **Avery:** Heads up, payroll says the T-2008 overtime fix may slip to next cycle. Can you own the
> comms to Owen?
> **Avery:** Also, still need your Q4 onboarding input by Thursday.

This gives the command center a **decision waiting on you** (T-2008 comms) and a **commitment with a
deadline** (the Thursday input).

---

## What Exercise 1 should surface with this seed

- **Urgent items:** **T-2008** (the high-importance payroll email, plus the Teams chat if seeded) and
  the **Thursday deadline** for Avery's Q4 onboarding input.
- **Meetings:** a **conflict** on Thursday morning (leadership sync vs. candidate interview); the
  busiest day is **Thursday**.
- **Priorities:** replies waiting on you (Dana's training-budget question, Hana's interview-panel
  request).
- **Org pulse:** the quiet engagement-survey workstream (if seeded). The newsletter and FYI update
  should **not** be flagged as priorities.
