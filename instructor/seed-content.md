# Seed Content Pack — Exercise 8 demo (instructor only)

> **For the facilitator's demo account only.** Attendees don't need any of this: they run Exercise 8
> on **their own work mail, calendar, and Teams** and use the **Zava sample files** for everything
> else. Your demo account (in your separate demo tenant) is usually quiet, so load the items below
> into it **1–2 days before the session**. Then your live Exercise 8 demo shows a rich, predictable
> command center, whatever the room's own data looks like.
>
> All content is **fictional Zava** material. What the command center should surface is in the
> [facilitator answer key](facilitator-answer-key.md#exercise-8--executive-command-center).

## How to load it

### Recommended: VS Code + GitHub Copilot (Agent mode) + the Work IQ MCP server

**Why this option:** the [Work IQ MCP server](https://learn.microsoft.com/microsoft-365/copilot/extensibility/work-iq/mcp/overview)
is Microsoft's generally available MCP server for Microsoft 365 data. One endpoint covers **mail,
calendar, and Teams chat**, it can **create** as well as read (`create_entity /me/events`,
`do_action /me/sendMail`, chat messages), every action runs **as the signed-in user only**, and VS Code
asks you to approve each tool call. It's also the same Work IQ layer Cowork reads from, so you can
check the result straight away. Sign-in is Microsoft Entra ID; there's no app to register in most
tenants.

> **Do this a week ahead (demo-tenant admin).** Work IQ MCP **blocks create, update, and send by
> default**. In the [Microsoft 365 admin center](https://admin.microsoft.com), go to **Agents → Tools →
> Work IQ MCP → Policy** and allow write operations for the demo tenant
> ([policy governance](https://learn.microsoft.com/microsoft-365/copilot/extensibility/work-iq/mcp/policy-governance-mcp)).
> The change can take **up to 24 hours** to apply. If Work IQ isn't on yet, an admin may also need to
> [enable your tenant for Work IQ](https://learn.microsoft.com/microsoft-365/copilot/extensibility/work-iq/enable-work-iq)
> and give it a spending policy (Work IQ is billed by usage). This is your demo tenant, not the
> attendees' production tenant.

| Option | Verdict |
| --- | --- |
| **Work IQ MCP server in VS Code (Agent mode)** | **Recommended.** About 20 minutes, mostly prompts you paste. |
| Microsoft Graph PowerShell or a Graph script (`sendMail`, `events`) | Good if you reseed often; more setup (app registration, permissions). |
| By hand in Outlook and Teams | Fine as a fallback; about 30 minutes, easy to get dates wrong. |
| Microsoft MCP Server for Enterprise | Not suitable: it reads tenant and directory data; it doesn't create mail or meetings. |
| Agent 365 per-workload MCP servers (Mail, Calendar, Teams) | Not recommended: legacy, kept for backward compatibility, and they need an app registration. |
| Microsoft 365 Agents Toolkit (VS Code extension) | Not suitable: it builds agents and apps; it doesn't load mailbox content. |

#### 1. One-time setup (about 10 minutes)

1. Install **Visual Studio Code** (1.118 or later; Insiders works too) and sign in to **GitHub
   Copilot** (Accounts menu, bottom left).
2. Open the Command Palette (**Ctrl+Shift+P**) → **MCP: Add Server** → **HTTP** → enter
   `https://workiq.svc.cloud.microsoft/mcp` → name it **workiq** → choose **Global**.
3. VS Code opens `mcp.json`; select **Start** above the `workiq` entry, then **Allow** and sign in
   with a **demo-tenant** account (never an attendee's or a production account).
4. Open **Chat** (**Ctrl+Alt+I**), switch the mode to **Agent**, select the **Tools** icon, and check
   that the **workiq** tools are on.
5. **Test it:** ask *"Using Work IQ, what's on my calendar tomorrow?"* A "policy denied" reply when
   you create or send something means the write policy above isn't on yet (or hasn't applied); it
   isn't a transient error, so don't keep retrying.

#### 2. Prepare the demo tenant

- **Sender accounts:** emails should arrive *from* other people, so each item is created while signed
  in as its sender. Use **Avery Quinn** (your manager, required) plus any one or two existing demo
  users for the rest. The command center reads the subject and body, so a different sender name is
  fine. Set your demo account's **manager** to Avery Quinn (Microsoft 365 admin center → **Users →
  Manager**), so requests from your manager stand out.
- **Dates:** pick the workshop week and note the real dates for `{Wednesday}`, `{Thursday}`, and
  `{Friday}`. Load everything **1–2 days before** the session, so it counts as "today and this week."

#### 3. Load the items, one sender at a time

Open this file (or `seed-content.docx` saved as text) in VS Code so Copilot can read it, then run one
pass per sender. To switch sender: **Accounts** menu → sign out of the Microsoft account → **MCP: List
Servers** → **workiq** → **Restart**, and sign in as the next sender.

| Pass | Sign in as | Items |
| --- | --- | --- |
| 1 | **Avery Quinn** | Emails 1 and 4 (send 4 as the meeting: calendar event 3 with you invited), calendar event 1 with you invited, the Teams chat (C) |
| 2 | A second demo user (e.g., *Zava Communications*) | Emails 3 and 6 |
| 3 | A third demo user (or the second again) | Emails 2, 5, and 7 (keep each body's signature: Owen, Dana, Hana) |
| 4 | **Your demo account** | Calendar event 2 (the overlapping interview), the optional quiet recurring meeting, and accept the kickoff invite |

Paste this prompt in Agent mode for each pass (fill in the brackets):

> Using the Work IQ tools and the file seed-content.md, create **only** these items: [items from the
> table]. Send or invite **only** [demo account email]; replace {attendee} with [demo account display
> name], {Wednesday} with [date], {Thursday} with [date], and {Friday} with [date]. Keep each subject,
> body, importance, time, and Teams-meeting setting exactly as written. Show me each item before you
> create or send it, and don't contact anyone else.

Approve each tool call as it comes (keep **Allow once**, not **Always allow**), so you see every
email and meeting before it goes.

#### 4. Check it

- In VS Code (signed in as your demo account): *"Using Work IQ, list my unread emails from the last
  two days and my meetings on [Thursday]."* You should see the 7 emails, the **Thursday conflict**,
  and the Wednesday kickoff.
- Then run your Exercise 8 dry run in Cowork and compare with the
  [answer key](facilitator-answer-key.md#exercise-8--executive-command-center).

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
| 3 | Benefits Open Enrollment Kickoff | {Wednesday} 14:00–14:30 | Same as email #4; accept it in your demo account's calendar |

Optional: add one **declined or quiet** recurring meeting (e.g., "Monthly engagement survey review",
no activity in 6 weeks). It gives the command center's **Org pulse** view a "gone quiet" signal.

---

## C. Teams chat (optional)

A 1:1 chat from **Avery Quinn** to your demo account:

> **Avery:** Heads up, payroll says the T-2008 overtime fix may slip to next cycle. Can you own the
> comms to Owen?
> **Avery:** Also, still need your Q4 onboarding input by Thursday.

This gives the command center a **decision waiting on you** (T-2008 comms) and a **commitment with a
deadline** (the Thursday input).

---

## What Exercise 8 should surface with this seed

- **Urgent items:** **T-2008** (the high-importance payroll email, plus the Teams chat if seeded) and
  the **Thursday deadline** for Avery's Q4 onboarding input.
- **Meetings:** a **conflict** on Thursday morning (leadership sync vs. candidate interview); the
  busiest day is **Thursday**.
- **Priorities:** replies waiting on you (Dana's training-budget question, Hana's interview-panel
  request).
- **Org pulse:** the quiet engagement-survey workstream (if seeded). The newsletter and FYI update
  should **not** be flagged as priorities.
