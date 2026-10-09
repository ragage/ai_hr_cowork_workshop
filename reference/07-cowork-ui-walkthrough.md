# 07 · Cowork UI Walkthrough

> Reference sheet for the "Getting Things Done with Copilot Cowork for HR Tasks" workshop.
> A quick tour of the Cowork interface so you can find your way around before the exercises.

Open Cowork at **https://copilot.cloud.microsoft** and select **Cowork** (next to **Chat**) at the top.
The left navigation has four places you'll use all day: **New task**, **My tasks**, **Automations**,
and **Customize**.

## New task (the home page)

This is where every session starts — the **"What can I do for you?"** screen with a **Start a
task…** box.

- **Start a task box** — type or speak what you want done. Press **@** while editing to pick from
  your M365 contacts.
- **Model picker** — choose the model for this task, or let Cowork decide. (Your tenant's screen may
  show a specific model, e.g. a named model with a dropdown.)
- **Reasoning effort** — set how hard Cowork works: higher = more thorough (slower, costs more);
  lower = faster and cheaper. Match it to the task.
- **Attach (+)** — add files to ground the task.
- **Dictate (mic)** and **rewrite/prompt tools** — speak your request or refine the prompt.
- **"Try these next"** — starter suggestions (e.g., *Organize my inbox*, *Arrange my week*, *Create
  a new business pitch*). Handy for ideas; select **Show more** for additional examples.

> **Tip:** The starter cards are a great way to show the room what Cowork can do in 10 seconds.

## My tasks

Your history of Cowork sessions — **find and resume previous tasks**. Everything you've asked Cowork
to do is here, so past work is always a click away. Use it to:

- Reopen a task and continue where you left off.
- Review an artifact Cowork produced earlier.
- Search across your previous tasks.

## Automations

Where Cowork works **on a schedule or in response to events** — no need to re-ask each time.

- **Scheduled prompts** run at a set time (e.g., *"Every Monday at 8 AM, summarize open HR tickets"*).
- **Event-driven tasks** run when something happens.
- Two tabs: **Runs** (each past/upcoming run) and **Manage schedules** (the definitions — edit,
  pause, resume, delete).
- Select **Create** to define a new schedule directly.

You'll build one in **Exercise 6**.

## Customize

Where you make Cowork **yours**. The page has three tabs:

- **Preferences** — **Customize instructions for Cowork**: guidance automatically added to the start of
  *every* task (tone,
  spelling, "always cite the source").
- **Skills** — add your own **personal/custom skills** (you build one in **Exercise 3**), and manage
  sharing.
- **Plugins** — the plugins you or your admin installed (each with an on/off toggle), plus **Discover**
  for plugins from the Microsoft 365 App Store. Plugins connect Cowork to systems such as payroll or
  recruiting. See [09-plugins.md](09-plugins.md) for more on HR plugins and a screenshot.

## The session side panel (while a task runs)

Once a task is running, open the **side panel** (the **side panel toggle** at the right of the
session) and watch it update in real time:

| Section | What you'll find |
| --- | --- |
| **Progress** | A progress bar and step-by-step log of what Cowork is doing |
| **Input folder** | Files **you** attached as context |
| **Output folder** | Files Cowork **created**, each with **Preview** and **Download** buttons |
| **Skills** | Chips for the skills Cowork loaded (e.g., *Email*, *Word*, *Deep Research*) |
| **Schedule** | Any automation tied to the session (edit, pause, resume, delete) |
| **Permissions** | "Don't ask again" approvals you've granted this session; revoke them here |

Cowork **pauses at checkpoints** for your approval as it works.

## Finding your outputs (the Output folder)

Everything Cowork creates (documents, spreadsheets, decks, HTML dashboards, images) lands in two
places:

1. **In the task:** side panel → **Output folder**.
   - **Preview** opens the file in a **split view** next to the chat. Word, Excel, and PowerPoint open
     in an online preview; HTML, PDF, CSV, Markdown, and images render inline. Use the **full-screen
     toggle** for a closer look, or **Open in native app**.
   - **Download** saves one file to your device; **Download All** (top of the list) saves every
     output as a single zip (up to 50 files / 500 MB).
2. **In OneDrive:** every output is also saved to your **OneDrive → Cowork** folder, so you can find
   it later without reopening the task (or reopen the task from **My tasks**).

> **Tip:** The facilitator introduces this with the optional scorecard in **Exercise 1**.
> Use it in every exercise that creates a file, including the HTML dashboard in **Exercise 8**.

## How approvals work

The detailed walkthrough is in the workbook's
[Optional Sections](../participant/participant-workbook.md#optional-sections), after Exercise 8.
During exercises, review and approve one action at a time; don't use Approve All or Always allow.

Before a sensitive action (sending an email, posting to Teams, deleting, creating a meeting), Cowork
shows an **approval dialog**, often with a preview of the email, message, or meeting.

| Option | What it does | Use it today? |
| --- | --- | --- |
| **Action button** (e.g., **Send**, **Post**, **Create**) | Approves **this one** action | ✅ Yes, after reading the preview |
| **Cancel** | Skips this action; Cowork continues with the rest | ✅ Yes, whenever unsure |
| **Show parameters** | Shows the technical details of the action | ✅ Yes, to check recipients and targets |
| **More options** → *Only to…* / *Always allow* / *Approve & don't ask again* | Approves and **stops asking** for similar actions for the rest of the session | ❌ **No** |
| **Approve All (n)** | Approves **every pending** action at once | ❌ **No** |

> **Workshop rule:** approve **one action at a time**. **Approve All** and **Always allow** skip the
> checkpoints that keep HR accountable, and one click could bulk-send mail or change many items at
> once. If you click one by mistake, open the side panel's **Permissions** section and revoke it.

## Quick map

| You want to… | Go to… |
| --- | --- |
| Start something new | **New task** |
| Resume or find past work | **My tasks** |
| Make it recurring | **Automations** |
| Set tone, add skills, add plugins | **Customize** |
| See what Cowork is doing right now | **Session side panel** |
| Open, preview, or download what Cowork created | **Side panel → Output folder**, or **OneDrive → Cowork** |
| Revoke an "always allow" approval | **Side panel → Permissions** |
