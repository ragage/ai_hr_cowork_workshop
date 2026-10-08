# Facilitator Guide
## Getting Things Done with Copilot Cowork for HR Tasks (2½ hours, ~25 attendees)

This guide gives you a minute-by-minute run sheet, talking points, and troubleshooting for a
2½-hour, hands-on workshop. The **~25 attendees sign in with their own work accounts** (Exercise 1 reads their own mail and
calendar; everything else uses the Zava files). You, the **facilitator, demo from your own separate
tenant**, with your demo account seeded from [seed-content.md](seed-content.md).

Each exercise is introduced on screen with a **scenario card** (Function · Goal · Output · Why
Cowork? · Prompt · Workflow · Data sources). Walk the card top-left to bottom-right before attendees start.

## Before you start

- **Staffing:** 1 facilitator + **1–2 floaters/proctors** for a group of ~25. Proctors handle
  sign-in and account issues so you can keep pace.
- **Access ahead (host/admin):** attendees use **their own work accounts**, so there's nothing to
  provision or hand out. Check each has a Microsoft 365 Copilot license and is in a security group
  covered by a **Cowork spending policy** (that's what grants Cowork access) and allowed **Cowork
  Browsing** (for Ex 3); keep 1–2 licensed spares. Make sure **your own (demo) tenant** is
  Copilot/Cowork-ready too. See [readiness checklist](readiness-checklist.md).
- **Seed your demo account (1–2 days ahead):** load the Exercise 1 emails, meetings, and Teams chat
  into **your** demo account only, with VS Code, GitHub Copilot (Agent mode), and the **Work IQ MCP
  server** ([seed-content.md](seed-content.md#how-to-load-it)). Attendees need no seed: they run
  Exercise 1 on their own data.
- **Stage the sample data:** put **zava-sample-knowledge.zip** (from the kit's `sample-knowledge/`
  folder: the six Word and Excel sample files, in an `ai_hr_cowork_workshop` folder) in a **shared
  location in the attendees' tenant** (Teams/SharePoint) that every attendee can reach. Share only
  this **one zip**, not the individual files, so there's a single thing to download.
- **Pre-session setup:** the session is 2½ hours, so the [participant email](../communication/participant-email.html)
  asks attendees to sign in, run the smoke test, and upload the sample folder to their OneDrive
  **before** the day. The 10-minute setup segment is then only a check.
  Downloading the kit files from GitHub? If a link opens the file on GitHub, select the **Download**
  icon (**Download raw file**) at the top right of the file (see the picture below).
- **Dry run:** a full run of all 8 exercises with a licensed account in the attendees' tenant one week out, checked
  against the [answer key](facilitator-answer-key.md). The full prep timeline, cost planning, and
  whole-room **Plan B** are in the [readiness checklist](readiness-checklist.md#preparation-timeline).
- **Set expectations up front:** "You're in your own work accounts, so your screens match each other.
  I'm demoing from a **separate demo tenant**, so mine may look a little different. Exercise 1 reads
  your own mail and calendar, and the results stay private to you; everything else uses the fictional
  Zava files. Everything Cowork produces is a **draft to review**."

![Tip: on a GitHub file page, select the Download icon (Download raw file) at the top right of the file](../reference/media/download-hint.png)

> **Tenant and data reminder:** Attendees are in their **production tenant**, so org search returns
> real content that differs by person, and **your demo tenant is separate**. Except for Exercise 1,
> keep exercises grounded on the **provided sample files**. **Never ask attendees to project or share
> their Exercise 1 results.** Have attendees keep custom skills **"Only you"** (or initialed) to avoid
> 25 identical skills cluttering their tenant.

> **Navigating the deck:** every exercise starts with a **divider slide** (exercise number, picture,
> time, and an 8-step progress tracker), and each exercise is its own **PowerPoint section**. Open
> **View → Normal** and use the section headers in the thumbnail pane to jump straight to any exercise.

> **Prompts in the speaker notes:** every **Hands-on** slide's notes end with the exercise prompt as
> plain text, one block per task, so you can copy it straight into Cowork (or Agent Builder for
> Exercise 8) during your demo.

> **Demo videos:** each exercise has a **Demo** slide right after its scenario card, and so do the
> **Copilot and Cowork UI walkthrough** and **Prompting best practices** slides (10 in all). Each has an
> empty video frame. Cowork tasks can take several minutes, so **record each demo ahead of time** from
> your demo account (Exercise 1 from the seeded account, never real mail) and play the recording
> instead of waiting live. To add one, select the **media icon** in the frame (or **Insert → Video →
> This Device**), pick your recording, and on **Playback** set **Start: When Clicked On**. Trim long
> waits with **Playback → Trim Video**. With no video inserted, the slide still shows a clean frame, so
> you can run that demo live instead. Insert videos in **your own copy** of the deck: the kit's
> `instructor-deck.pptx` is regenerated by the build.

## Run sheet (150 minutes)

| Time | Segment | You do | Attendees do |
| --- | --- | --- | --- |
| 0:00–0:05 | **Welcome & context** | Explain what Cowork is, HR value, the approval/checkpoint model | Listen; open Cowork |
| 0:05–0:10 | **Copilot vs. Cowork** | Draw the assistant-vs-coworker distinction; when to use which | Ask questions; share HR examples |
| 0:10–0:20 | **Cowork UI walkthrough + setup** | Tour New task, My tasks, Automations, Customize, model picker, reasoning effort; show copying files | Sign in + smoke test + copy sample files + custom instructions |
| 0:20–0:35 | **Ex 1 — Executive Command Center** | Show the approval dialog (one at a time); walk the scenario card; demo the HTML dashboard; **show the Output folder** (Preview, Download, OneDrive → Cowork); skill save & schedule; optional: check the cost with `/cost` | Fill placeholders, run the prompt, open the dashboard from the Output folder |
| 0:35–0:50 | **Ex 2 — Deep Research (web)** | Demo the cited briefing; demo the optional scorecard | Run Deep Research, ground it in the job description for 5 questions; optional: Word + Excel scorecard |
| 0:50–1:05 | **Ex 3 — Navigate websites with the browser** | Demo the browser: consent, progress chips, Switch to tab as it searches dol.gov and lni.wa.gov | Run the two-site navigation, check the links; optional: Word brief for payroll |
| 1:05–1:20 | **Ex 4 — Build a custom skill** | Build "HR Policy Answer" live; read the evaluation aloud | Build, read score, test in/out of scope |
| 1:20–1:30 | **Ex 5 — Recruiting + reporting** | Demo the inclusive job posting + ticket summary | Do Task 5a & 5b |
| 1:30–1:45 | **Break** (15 min) | Reset; sweep for blockers; check Ex 4 skills saved | Stretch, coffee |
| 1:45–1:55 | **Ex 6 — Onboarding pack** | Demo deck + scheduling + announcement; call out new skill chips | Do Task 6a; optional: 6b, 6c |
| 1:55–2:10 | **Ex 7 — Automate & share** | Create an Automation; demo Daily Briefing + share/re-share | Do Task 7a, 7b; optional: 7c |
| 2:10–2:25 | **Ex 8 — Agent Builder (non-Cowork)** | Build the HR Policy Agent live; test on "Try it" | Build, add knowledge, test in/out of scope |
| 2:25–2:30 | **Wrap-up** | Recap the three tools, quick knowledge check, next steps | Q&A, pick a "next week" task |

## Segment talking points

### Welcome & context (0:00–0:05)
- Share the **six learning objectives** (README / workbook / deck slide 3): choose the right tool,
  delegate safely, ground in real content, package repeatable work, build a no-code agent, apply HR
  guardrails. Come back to them at wrap-up.
- Cowork = describe the **outcome**, it **plans → picks skills → pauses for approval → returns
  artifacts**. Powered by Work IQ.
- HR value: less time on repetitive drafting, research, and reporting; more time on people.
- Emphasize the **checkpoint model**: nothing irreversible without confirmation → HR stays
  accountable.

### Copilot vs. Cowork (0:05–0:10)
- The key framing for the whole day: **Copilot (Chat) = AI assistant** (you ask, it answers, you
  drive); **Cowork = AI coworker** (you describe an outcome, it does the multi-step work and hands
  back a deliverable). See [reference/00-copilot-vs-cowork.md](../reference/00-copilot-vs-cowork.md).
- Use one HR example of each: Chat *"summarize this policy in 3 bullets"* vs. Cowork *"draft welcome
  emails for all 4 new hires from our onboarding checklist and save them as drafts."*
- Land the rule of thumb: several steps ending in a file/email/schedule/report → **Cowork**; a quick
  answer or rewrite → **Chat**. Tease that we close by building an **agent** (a third tool) in Ex 8.

### Cowork UI walkthrough + setup (0:10–0:20)
- Tour the four nav areas live, matching what's on their screen:
  **New task** (the "What can I do for you?" home — Start a task box, model picker, reasoning effort,
  attach, "Try these next"), **My tasks** (resume past work), **Automations** (Runs / Manage
  schedules), **Customize** (custom instructions, skills, plugins). See
  [reference/07-cowork-ui-walkthrough.md](../reference/07-cowork-ui-walkthrough.md).
- Point out the **session side panel** (skills chips, files, schedule) — you'll refer back to it all day.
- Then **check the pre-session setup**: everyone is **signed in in Microsoft Edge**, their **Edge
  profile** is their work account (needed for the Ex 3 browser task; a proctor also checks the Edge
  **Cowork** setting), the **smoke test** worked, and the **sample folder** is in their OneDrive. Anyone
  who hasn't does it now with a proctor. Everyone sets their **custom instructions** (Customize → Preferences → **Customize instructions for
  Cowork**; paste the workbook's text, Setup step D) — this is where sign-in/account issues surface. Proctors triage while you keep going with
  those who are ready.

### Ex 1 — Executive Command Center (0:20–0:35)
- **Approvals first.** Before the room starts, show an approval dialog and name each option: the
  action button, **Cancel**, **Show parameters**, and the two to avoid today, **Approve All (n)** and
  **More options → Always allow**. Say plainly: "One at a time. No Approve All." Show where to
  revoke: side panel → **Permissions**. In this exercise they approve saving the skill and the
  schedule.
- **Set expectations before they paste the prompt** (the dry run showed people weren't sure what
  would pop up):
  - **Their own data, not Zava.** Ex 1 is the only exercise on their real mail, calendar, Teams, and
    transcripts, so the dashboard shows **their** meetings and tasks. That's expected.
  - **What Cowork will ask:** clarifying questions (answer in the chat), progress messages and skill
    chips (nothing to do), **two approval cards** near the end (save the skill, create the schedule;
    one at a time), and **suggested next steps** when it finishes (skip them for now). The workbook
    lists these in a "What Cowork will ask you" box.
- This is the first **scenario card** of the day, and every later exercise uses the same format. Walk it: **Goal → Output → Why
  Cowork? → Prompt → Workflow → Data sources**.
- It shows Cowork at full stretch in **one prompt**: Work IQ gathers calendar, mail, chats,
  transcripts, and files → analyzes signals → builds an **interactive HTML dashboard** → **saves
  itself as a skill** and **schedules itself**. Preview for Ex 4 (skills) and Ex 7 (Automations).
- Have attendees fill the placeholders: **`[Priority Folder]`** → a OneDrive folder of their own
  priority documents (or the Zava folder); **`[time]`** → e.g., 8:00 AM.
- **Slow down and show the Output folder (about 3 minutes, on screen).** This is the first
  exercise that creates a file, and every later exercise depends on finding outputs:
  1. Open the **side panel** with the side panel toggle at the right of the session.
  2. Point out **Input folder** (what *you* attached) vs. **Output folder** (what Cowork *created*).
  3. Select **Preview** on the HTML dashboard: it opens in a split view; show the **full-screen
     toggle** and **Open in native app**.
  4. Show **Download** (one file) and **Download All** (a zip of every output).
  5. Open **OneDrive → Cowork** in a new browser tab to show the same file saved there.
  Then have the room do it themselves before moving on; proctors help anyone who can't find the
  side panel toggle.
- **Attendees use their own mail, calendar, and Teams**, so results vary: a busy week gives a rich
  dashboard, a quiet one a light dashboard. Demo first from **your seeded demo account**
  ([seed-content.md](seed-content.md); the Thursday conflict and T-2008 should surface), then keep the
  room focused on the **pattern**. Debrief on structure, not content: **no screen sharing** of
  attendee dashboards.
- Reinforce the guardrail baked into the prompt: recommendations focus on **workstreams and
  decisions, not evaluating individual people** — an important norm for HR.
- **Cleanup:** skill stays **"Only you"**; ask everyone to **pause or delete the weekday schedule**
  after class (Automations → Manage schedules) so it doesn't keep consuming usage.
- **Optional last step if you're on time: check the cost (about 2 minutes, slide after the Output
  folder).** In the same task, type **`/cost`**: Cowork shows the approximate credits this task used,
  credits used this month, and credits remaining. `/cost` itself is free and works on any earlier
  task. Stress that it's an **estimate, not a bill**, you **can't see the cost before** a task runs,
  and the schedule they just created uses credits on every run. If you're behind, skip the slide and
  just mention `/cost` at the break. Source:
  [Credit usage for Copilot Cowork tasks](https://learn.microsoft.com/microsoft-365/copilot/usage-based-billing-copilot-credits-cost).

### Ex 2 — Deep Research (0:35–0:50)
- Deep Research reads and **cites** many web sources; contrast it with a single lookup.
- Have attendees **open two citations** and check them: the habit matters more than the briefing.
- **Required:** the Deep Research briefing (2a) and grounding it in `job-description-sample.docx`
  for 5 tailored questions (2b). The dry run took about 20 minutes with the scorecard included, so
  the scorecard is now **optional (Task 2c)** for fast finishers.
- **Optional follow-up, same task (2c):** *"Turn this into an interviewer scorecard in Word AND Excel
  with the scoring scales filled in."* One follow-up turns research into ready-to-use deliverables in
  **two formats** at once. Point out the **Word** and **Excel** skill chips, then have attendees
  open both files from the **Output folder** they learned in Ex 1.
- Check that the scales are actually **filled in** (anchored descriptions for each score), not
  placeholders. If they're blank, have attendees reply: *"Fill in the 1, 3, and 5 anchors for every
  competency."*
- **Timing:** Deep Research takes a few minutes. Use the wait to ask "When is web research better
  than our own content, and when is it riskier?" At **0:45**, demo the optional scorecard on your
  screen so everyone sees the Word + Excel output.

### Ex 3 — Navigate websites with Cowork's browser (0:50–1:05)
- This is the **"use the browser to navigate the web and get things done"** requirement. Cowork
  **operates websites** step by step, like a person or a test tool such as Playwright would: types
  in a site's search box, clicks links and menus, moves to a second site, and reports each page.
- **Say it early:** there's **no "browser" skill** to pick and no skill chip. Ask for something that
  needs a website and Cowork opens a **hidden tab in the attendee's own Edge**, with their sign-ins
  and the organization's policies. No new access; sign-in, MFA, and CAPTCHA are handed back to the
  person; consequential actions need approval; everything is audited.
- **Demo it first:** show the one-time **consent notice** (**I understand**), the **progress chips**
  (*Opening dol.gov*, searching), and **Switch to tab** so the room sees Edge typing in the DOL
  search box and clicking through. Then switch back to the chat.
- The prompt is **read-only** on two public government sites (dol.gov, lni.wa.gov), so it's safe
  for a room of 25. A good table: Zava's 1.5× over 40 hours **matches** federal and Washington rules;
  DOL adds the **regular-payday** rule, Washington adds **no waiver** and **no daily overtime**. So
  **T-2008** is time-sensitive. Remind the room: a policy check, not legal advice.
- **3b (optional)** turns the table into a Word brief for payroll; fast finishers find it in the
  **Output folder**.
- **Requirements** (host; see the [readiness checklist](readiness-checklist.md) and
  [reference/10-cowork-browser.md](../reference/10-cowork-browser.md)): browser access allowed for the
  attendee group, Edge 152 or later, Cowork open **in Edge on the web**, an Edge profile signed in
  with their **work account** (not InPrivate), and the Edge **Cowork** setting on. Anyone blocked
  follows your demo.
- **Stretch for fast finishers:** *is the HR Coordinator exempt from overtime?* Cowork finds DOL
  **Fact Sheet #17A** through the dol.gov site search and reads the administrative-exemption duties
  test, then finds Washington's **minimum salary for exempt employees** on lni.wa.gov. Read only,
  regular pages. Don't point people at interactive tools such as the DOL eLaws **Overtime Security
  Advisor**: in the dry run Cowork declined to open it.

### Ex 4 — Build a custom skill (1:05–1:20) — the centerpiece
- Build it live from **Customize → Skills → Add → Create new**.
- Read the **auto-evaluation** aloud; explain the four scoring dimensions and the bands.
- Demo both a **triggering** question and an **out-of-scope** one (salary) to show scope boundaries.
- **Test in a new task, and name Zava:** *"At Zava, when is open enrollment and how do I change my
  medical plan?"* Attendees' own tenants hold their company's real benefits content, and in the dry
  run a generic "When is open enrollment?" pulled that instead of the Zava file. The instructions
  now say to use **only** the two Zava files. A good answer: November, effective January 1, citing
  `benefits-summary.docx`.
- If someone scores "Needs work," coach them: tighten the **trigger wording** and **scope**.
- **Shared-tenant tip:** tell everyone to keep their skill **"Only you"** (or add initials) so you
  don't end up with 25 identically named skills shared across the tenant.
- Foreshadow Ex 8: this skill helps **you** in Cowork; later we build an **agent** others can use.

### Ex 5 — Recruiting + reporting (1:20–1:30)
- **Job posting (5a):** the follow-on to Ex 2. Ex 2 prepared the interview; 5a writes the posting
  that attracts candidates. Discuss the **wording-review table**: typical flags are the degree
  requirement and "1–3 years" read as must-haves. Ask the room whether they agree with every flag;
  HR keeps the final judgment.
- Ticket summary: the sample data has **6 open / 14 closed** tickets and exactly **one** high-priority
  open item — **T-2008** (overtime missing from a paycheck). T-2003 and T-2013 are also High but
  already closed — a good check on whether Cowork read the Status column. Full expected results:
  [facilitator-answer-key.md](facilitator-answer-key.md).
- Keep this a one-off report; they'll turn it into a scheduled **Automation** in Exercise 7.

### Break (1:30–1:45, 15 minutes)
- The only break. Help anyone still blocked catch up, and check that everyone's Exercise 4 skill
  saved — Ex 7 shares it. Restart on time.

### Ex 6 — Onboarding pack (1:45–1:55)
- **Story:** **Sofia Alvarez** (fictional; attendees invite only themselves) accepted the HR Coordinator role from Ex 2
  and Ex 5 and starts **next Monday**. The kickoff prompt gives a concrete time (9:30 AM) so Cowork
  doesn't have to guess.
- This exercise shows off **more built-in skills**: PowerPoint (deck), Scheduling/Calendar (kickoff),
  and Communications (announcement). Call out each new **skill chip** as it loads.
- Reinforce shared-tenant safety: for the kickoff invite, attendees invite **themselves only** — no
  real people — and everything stays a reviewed draft.
- **6a (the deck) is the must-do.** 6b and 6c are **optional** for fast finishers; demo them while
  the room's decks build. In the dry run, 6a alone took about 11 minutes.

### Ex 7 — Automate & share (1:55–2:10)

Ex 7 has 15 minutes because 7a alone took about 12 minutes in the dry run; Ex 4 has 15
because it took about 11.

- Create an **Automation** live (weekly Monday ticket digest). The prompt names the **exact file and
  folder** (`hr-tickets-sample.xlsx` in `Documents/ai_hr_cowork_workshop`) because a scheduled run can't ask for
  clarification. Choose **Activate and run now** so the room sees a real run, then show the **Runs**
  vs **Manage schedules** tabs so they know where to edit/pause.
- Demo a **Daily Briefing**, then walk the **Share / Re-share** flow on the custom skill from Ex 4.
  **7c (sharing) is optional** for attendees; 7a is the must-do.
- Emphasize etiquette: keep skills **"Only you"** or initialed; sharing stays within this tenant.

> **HR plugins:** the plugins spotlight isn't in the 2½-hour session; attendees get it in the
> [after-the-workshop pack](../participant/after-the-workshop.md) and
> [reference/09-plugins.md](../reference/09-plugins.md). If someone asks about connecting an HR system (for
> example SAP SuccessFactors), point them there.

### Ex 8 — Agent Builder, non-Cowork (2:10–2:25)
- **Say it out loud: "This one is not Cowork."** The divider, scenario card, and demo slides carry a
  **Not Cowork** banner. Attendees close their Cowork task and work in Agent Builder, which has no
  tasks, side panel, approvals, or skills.
- Step **outside Cowork**: open Microsoft 365 Copilot → **Create agent** and build the **HR Policy
  Agent** live. See [reference/08-agent-builder-policy-agent.md](../reference/08-agent-builder-policy-agent.md).
- Make the skill-vs-agent distinction explicit: the Ex 4 skill helps **you**; this **agent** is a
  standalone helper **others** can chat with in Copilot.
- Walk the **Describe → Configure → Try it** tabs; add the Zava HR docs as **knowledge**; test a
  policy question (sourced answer) and an out-of-scope one (declines).
- **Keep it on Zava's files.** In the Configure tab's **Knowledge** section, turn **Only use specified
  sources** on and **Search all websites** off, and test with *"At Zava, when is open enrollment…?"*
  In the dry run, the agent answered with the tester's **own company's** open-enrollment details.
  Agent Builder *prioritizes* the specified sources but can't fully block general knowledge; for
  stricter control, organizations use Copilot Studio.
- Note it's **no-code** but a **different tool** — needs a Copilot license, desktop/web only, and for
  external *actions* you'd move to Copilot Studio (out of scope). Good moment to show the breadth of
  the Copilot platform beyond Cowork.

### Wrap-up (2:25–2:30)
- Keep it tight: this segment is 5 minutes.
- Recap the **three tools**: Copilot Chat (quick answers), Cowork (get work done), Agent Builder
  (stand up a reusable helper).
- Remind everyone to **pause or delete the Exercise 1 and Exercise 7 schedules** if they don't want
  them to keep running.
- End on the deck's last slide, **Clean up the training data**, and leave it up while people pack
  up. The [clean-up steps](../participant/participant-workbook.md#clean-up-the-training-data) at the
  end of the workbook take about 5 minutes; attendees can finish them later today. Deleting the
  Exercise 1 and Exercise 7 schedules comes first, because they're usage-billed.
- Recap the five golden rules from [reference/06-responsible-use.md](../reference/06-responsible-use.md).
- Point to the [prompt library](../reference/04-prompt-library.md) as their takeaway.
- Run a **quick knowledge check** as a show of hands (deck slide: pick 2–3 of the 4 questions;
  questions and answers in [after-the-workshop.md](../participant/after-the-workshop.md)), then revisit the learning
  objectives.
- Have them name one task they'll try in real work next week.
- **Next day:** send [after-the-workshop.md](../participant/after-the-workshop.md) (full knowledge check, feedback
  survey, and 30-day adoption plan).

## Troubleshooting triage (hand to proctors)

| Symptom | Likely cause | Fix / fallback |
| --- | --- | --- |
| No **Cowork** toggle | Account missing license / Cowork not enabled | Host swaps to a spare licensed account; attendee uses **fallback follow-along** meanwhile (see the [answer key](facilitator-answer-key.md#fallback-walkthrough-for-attendees-who-cant-run-cowork)) |
| Prompt returns nothing / error | Usage-based billing not enabled | Host confirms tenant billing; fallback follow-along |
| Can't sign in | MFA prompt, wrong account in the browser, or a personal account | Sign in with the work account in an Edge work profile; else the host lends a spare account |
| Can't find sample files | Staged location not shared | Point to the Teams/SharePoint copy; proctor helps copy to OneDrive |
| Custom skill option missing | On mobile | Switch to laptop/desktop |
| Sees others' skills in the list | Shared tenant + org-shared skills | Keep skills **"Only you"** or initialed |
| Cowork acted without asking | **Approve All** or **Always allow** was clicked earlier in the session | Side panel → **Permissions** → revoke; start a **new task** to reset; check Sent/Deleted items |
| **Create agent** option missing (Ex 8) | On mobile, or wrong Copilot surface | Use desktop/web Microsoft 365 Copilot (Chat/Teams); confirm Copilot license |
| Command center is nearly empty (Ex 1) | Quiet week, or a spare account with no history | Expected: focus on the pattern and show your seeded demo; don't ask attendees to share real dashboards |
| Can't find the output file (any exercise) | Side panel closed, or looking in the chat | Open the **side panel toggle** → **Output folder**; or open **OneDrive → Cowork** |
| Schedule not created (Ex 1) | Checkpoint declined or `[time]` left blank | Re-run the last line of the prompt with a real time, or create it in Automations |
| Deep Research slow (Ex 2) | Multi-source research takes several minutes | Expected: discuss while it runs; demo the optional scorecard instead of waiting for it |
| Answer uses the attendee's **own company's** policies, not Zava's (Ex 4, Ex 8) | Generic question ("When is open enrollment?") matched real HR content in their tenant, or Agent Builder searched beyond its files | Ask again in a new task starting with "At Zava, …"; Ex 4: the skill's instructions say **only** the two Zava files; Ex 8: **Only use specified sources** on, **Search all websites** off, files no longer "Preparing" |
| Cowork won't open a site (Ex 3) | Some interactive government tools (e.g., DOL eLaws advisors) are declined | Skip that site; the core task and stretch use regular dol.gov and lni.wa.gov pages |
| "Browser tasks run in Microsoft Edge" (Ex 3) | Not in Edge, Edge profile isn't the work account, InPrivate window, or Edge older than 152 | Open Cowork in Edge in a profile signed in with the work account; update Edge; else watch the facilitator demo |
| Browser task never starts (Ex 3) | Browser access not allowed for this account, the Edge **Cowork** setting is off, or the consent notice wasn't accepted | Select **I understand** at the consent notice; host checks Copilot → Settings → Cowork settings → **Allow browser access** includes the attendee group |
| Falling behind | Group pace variance | Use **checkpoints** to sync; [stretch prompts](../participant/participant-workbook.md) for fast finishers |
| **Whole room** can't use Cowork | Service or tenant outage | Stop after 10 minutes; switch to [Plan B](readiness-checklist.md#plan-b--if-cowork-is-down-for-the-whole-room) |

## Time checks and what to cut

Two and a half hours with eight exercises has no slack, so check the clock at these points and cut
**in this order** if you're behind. Play the **demo video** for each exercise instead of waiting on a live
run. Never cut Ex 4 or the core of Ex 8. The optional sub-tasks (2c, 3b, 6b, 6c, 7c) are already
outside the core timing, so the first cut is simply not waiting for them.

| Clock | You should be... | If you're more than 5 minutes behind |
| --- | --- | --- |
| **0:20** | Starting Ex 1 | Finish sign-in and file uploads during Ex 1; proctors help stragglers |
| **0:35** | Starting Ex 2 | Skip the Ex 1 discussion; demo the Output folder only |
| **0:50** | Starting Ex 3 | Stop Ex 2 after the 5 questions; demo the optional scorecard |
| **1:05** | Starting Ex 4 | Move on after the comparison table; demo the optional 3b brief |
| **1:30** | Starting the break | Ex 5: do 5b only; shorten the break to 10 minutes |
| **1:55** | Starting Ex 7 | Ex 6: move on after 6a (6b and 6c are optional). Ex 7: do 7a only, demo 7b and 7c |
| **2:10** | Starting Ex 8 | Run Ex 8 as a facilitator demo; attendees build it after class |

**Fast room?** Use the **Stretch** prompts (at the end of each exercise in the
[participant workbook](../participant/participant-workbook.md)), or have early finishers try a prompt from the
[prompt library](../reference/04-prompt-library.md).

## Pacing tips for ~25 people

- Use the **✅ Checkpoints** in the workbook as sync points — "raise a hand when you hit the
  checkpoint."
- Keep **stretch prompts** ready (end of each exercise in the [participant workbook](../participant/participant-workbook.md)) so fast
  finishers stay engaged while others catch up.
- Don't let one tenant issue stall the room — **parking lot** it and keep moving; a proctor follows up.
- Timings are guidance; if you're running long, keep everyone on the required tasks (the optional
  2c, 3b, 6b, 6c, and 7c are for fast finishers) and/or run Ex 8 as a **facilitator demo** (attendees watch, then build after) — protect Ex 4 and the Ex 8 concept.

## Success criteria

By the end, each ready attendee has:
- [ ] Understood when to use **Copilot Chat vs. Cowork** (opening segment)
- [ ] Toured the Cowork UI — **New task, My tasks, Automations, Customize** (walkthrough)
- [ ] Built an **Executive Command Center** HTML dashboard, found it in the **Output folder** and
  OneDrive → Cowork, and saved it as a skill with a schedule, approving one action at a time (Ex 1)
- [ ] Produced a cited web-research briefing and 5 interview questions grounded in the job
  description (Ex 2)
- [ ] Had Cowork **navigate two websites** in Edge and build a linked comparison table (Ex 3)
- [ ] Built and tested a custom skill scoring Good+ (Ex 4)
- [ ] Wrote an inclusive job posting and a ticket report (Ex 5)
- [ ] Built an onboarding orientation deck from the Zava files (Ex 6)
- [ ] Created a recurring Automation and a Daily Briefing (Ex 7)
- [ ] Built and tested an **HR Policy Agent** in Copilot Agent Builder (Ex 8)
