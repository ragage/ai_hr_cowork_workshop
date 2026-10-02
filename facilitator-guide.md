# Facilitator Guide
## Getting Things Done with Copilot Cowork for HR Tasks (4 hours, ~25 attendees)

This guide gives you a minute-by-minute run sheet, talking points, and troubleshooting for a
4-hour, hands-on workshop. The **~25 attendees share one common tenant**, each signed in with
**their own user account**. You, the **facilitator, demo from your own separate tenant**.

Each exercise is introduced on screen with a **scenario card** (Function · Goal · Output · Why
Cowork? · Prompt · Workflow · Data sources). Walk the card top-left to bottom-right before attendees start.

## Before you start

- **Staffing:** 1 facilitator + **1–2 floaters/proctors** for a group of ~25. Proctors handle
  sign-in and account issues so you can keep pace.
- **Provision ahead (host/admin):** ~25 **licensed user accounts** in the **shared attendee tenant**
  with a Microsoft 365 Copilot license, in a security group covered by a **Cowork spending policy**
  (that's what grants Cowork access) and allowed **Cowork Browsing** (for Ex 3); distribute credentials. Make sure **your own
  (facilitator) tenant** is Copilot/Cowork-ready too. See [readiness checklist](readiness-checklist.md).
- **Stage the sample data:** put **zava-sample-knowledge.zip** (the six Word and
  Excel sample files, in an `ai_hr_cowork_workshop` folder) in a **shared location in the attendee tenant** (Teams/SharePoint)
  that every account can reach, so attendees can copy them into their own OneDrive.
- **Dry run:** a full run of all 8 exercises on a test attendee account one week out, checked
  against the [answer key](facilitator-answer-key.md). The full prep timeline, cost planning, and
  whole-room **Plan B** are in the [readiness checklist](readiness-checklist.md#preparation-timeline).
- **Set expectations up front:** "You attendees share one tenant, so your screens match each other.
  I'm demoing from a **separate tenant**, so mine may look a little different. Your drafts, OneDrive,
  and skills are your own. Everything Cowork produces is a **draft to review**."

> **Tenant reminder:** The attendees share one tenant, so org search/grounding is consistent across
> the room — but so is any other demo content, and **your facilitator tenant is separate**. Keep
> exercises grounded on the **provided sample files**, and have attendees keep custom skills
> **"Only you"** (or initialed) to avoid 25 identical skills cluttering their tenant.

> **Navigating the deck:** every exercise starts with a **divider slide** (exercise number, picture,
> time, and an 8-step progress tracker), and each exercise is its own **PowerPoint section**. Open
> **View → Normal** and use the section headers in the thumbnail pane to jump straight to any exercise.

## Run sheet (240 minutes)

| Time | Segment | You do | Attendees do |
| --- | --- | --- | --- |
| 0:00–0:10 | **Welcome & context** | Explain what Cowork is, HR value, the approval/checkpoint model | Listen; open Cowork |
| 0:10–0:20 | **Copilot vs. Cowork** | Draw the assistant-vs-coworker distinction; when to use which | Ask questions; share HR examples |
| 0:20–0:40 | **Cowork UI walkthrough + setup** | Tour New task, My tasks, Automations, Customize, model picker, reasoning effort; show copying files | Sign in + smoke test + copy sample files + custom instructions |
| 0:40–1:05 | **Ex 1 — Executive Command Center** | Show the approval dialog (one at a time); walk the scenario card; demo the HTML dashboard; **show the Output folder** (Preview, Download, OneDrive → Cowork); skill save & schedule | Fill placeholders, run the prompt, open the dashboard from the Output folder |
| 1:05–1:25 | **Ex 2 — Deep Research (web)** | Demo the cited briefing; run the scorecard follow-up | Run Deep Research, tailor questions, build the Word + Excel scorecard |
| 1:25–1:35 | **Break** | Reset; help anyone still blocked | Stretch, coffee |
| 1:35–2:00 | **Ex 3 — Navigate websites with the browser** | Demo the browser: consent, progress chips, Switch to tab as it searches dol.gov and lni.wa.gov | Run the two-site navigation, check the links, build the Word brief for payroll |
| 2:00–2:30 | **Ex 4 — Build a custom skill** | Build "HR Policy Answer" live; read the evaluation aloud | Build, read score, test in/out of scope |
| 2:30–2:45 | **Ex 5 — Recruiting + reporting** | Demo the inclusive job posting + ticket summary | Do Task 5a & 5b |
| 2:45–2:55 | **Break** | Reset; sweep for blockers | Stretch, coffee |
| 2:55–3:15 | **Ex 6 — Onboarding pack** | Demo deck + scheduling + announcement; call out new skill chips | Do Task 6a, 6b, 6c |
| 3:15–3:30 | **Ex 7 — Automate & share** | Create an Automation; demo Daily Briefing + share/re-share | Do Task 7a, 7b, 7c |
| 3:30–3:35 | **Spotlight — HR plugins** (talk only) | Show Customize → Plugins (slide screenshot, or live in your tenant); HR examples and benefits | Listen; no hands-on |
| 3:35–3:55 | **Ex 8 — Agent Builder (non-Cowork)** | Build the HR Policy Agent live; test on "Try it" | Build, add knowledge, test in/out of scope |
| 3:55–4:00 | **Wrap-up** | Recap the three tools, quick knowledge check, next steps | Q&A, pick a "next week" task |

## Segment talking points

### Welcome & context (0:00–0:10)
- Share the **six learning objectives** (README / workbook / deck slide 3): choose the right tool,
  delegate safely, ground in real content, package repeatable work, build a no-code agent, apply HR
  guardrails. Come back to them at wrap-up.
- Cowork = describe the **outcome**, it **plans → picks skills → pauses for approval → returns
  artifacts**. Powered by Work IQ.
- HR value: less time on repetitive drafting, research, and reporting; more time on people.
- Emphasize the **checkpoint model**: nothing irreversible without confirmation → HR stays
  accountable.

### Copilot vs. Cowork (0:10–0:20)
- The key framing for the whole day: **Copilot (Chat) = AI assistant** (you ask, it answers, you
  drive); **Cowork = AI coworker** (you describe an outcome, it does the multi-step work and hands
  back a deliverable). See [reference/00-copilot-vs-cowork.md](reference/00-copilot-vs-cowork.md).
- Use one HR example of each: Chat *"summarize this policy in 3 bullets"* vs. Cowork *"draft welcome
  emails for all 4 new hires from our onboarding checklist and save them as drafts."*
- Land the rule of thumb: several steps ending in a file/email/schedule/report → **Cowork**; a quick
  answer or rewrite → **Chat**. Tease that we close by building an **agent** (a third tool) in Ex 8.

### Cowork UI walkthrough + setup (0:20–0:40)
- Tour the four nav areas live, matching what's on their screen:
  **New task** (the "What can I do for you?" home — Start a task box, model picker, reasoning effort,
  attach, "Try these next"), **My tasks** (resume past work), **Automations** (Runs / Manage
  schedules), **Customize** (custom instructions, skills, plugins). See
  [reference/07-cowork-ui-walkthrough.md](reference/07-cowork-ui-walkthrough.md).
- Point out the **session side panel** (skills chips, files, schedule) — you'll refer back to it all day.
- Then have everyone **sign in in Microsoft Edge**, check their **Edge profile** is the workshop account
  (needed for the Ex 3 browser task), run the **smoke test**, **copy the sample files** into their own
  OneDrive, and set their **custom instructions** (Customize → Preferences → **Customize instructions for
  Cowork**; paste the workbook's text, Setup step D) — this is where sign-in/account issues surface. Proctors triage while you keep going with
  those who are ready.

### Ex 1 — Executive Command Center (0:40–1:05)
- **Approvals first.** Before the room starts, show an approval dialog and name each option: the
  action button, **Cancel**, **Show parameters**, and the two to avoid today, **Approve All (n)** and
  **More options → Always allow**. Say plainly: "One at a time. No Approve All." Show where to
  revoke: side panel → **Permissions**. In this exercise they approve saving the skill and the
  schedule.
- This is the first **scenario card** of the day, and every later exercise uses the same format. Walk it: **Goal → Output → Why
  Cowork? → Prompt → Workflow → Data sources**.
- It shows Cowork at full stretch in **one prompt**: Work IQ gathers calendar, mail, chats,
  transcripts, and files → analyzes signals → builds an **interactive HTML dashboard** → **saves
  itself as a skill** and **schedules itself**. Preview for Ex 4 (skills) and Ex 7 (Automations).
- Have attendees fill the placeholders: **`[Priority Folder]`** → their OneDrive folder with the
  Zava files; **`[time]`** → e.g., 8:00 AM.
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
- **Data will be light** in fresh accounts. The seeded meetings (with a deliberate Thursday
  conflict) and Teams chat in [seed-content.md](seed-content.md) give it real signals. Keep the room
  focused on the **pattern**, and demo a richer result from your own tenant.
- Reinforce the guardrail baked into the prompt: recommendations focus on **workstreams and
  decisions, not evaluating individual people** — an important norm for HR.
- **Cleanup:** skill stays **"Only you"**; ask everyone to **pause or delete the weekday schedule**
  after class (Automations → Manage schedules) so it doesn't keep consuming usage.

### Ex 2 — Deep Research (1:05–1:25)
- Deep Research reads and **cites** many web sources; contrast it with a single lookup.
- Have attendees **open two citations** and check them: the habit matters more than the briefing.
- **Follow-up prompt, same task:** *"Turn this into an interviewer scorecard in Word AND Excel with
  the scoring scales filled in."* One follow-up turns research into ready-to-use deliverables in
  **two formats** at once. Point out the **Word** and **Excel** skill chips, then have attendees
  open both files from the **Output folder** they learned in Ex 1.
- Check that the scales are actually **filled in** (anchored descriptions for each score), not
  placeholders. If they're blank, have attendees reply: *"Fill in the 1, 3, and 5 anchors for every
  competency."*
- **Timing:** Deep Research takes a few minutes. Use the wait to ask "When is web research better
  than our own content, and when is it riskier?" If the room is behind at **1:20**, demo the
  scorecard follow-up on your screen.

### Break (1:25–1:35)
- Help anyone still blocked catch up. **Ask a proctor to check browser readiness** for Ex 3: Edge,
  workshop-account profile, and the Edge **Cowork** setting. Restart on time.

### Ex 3 — Navigate websites with Cowork's browser (1:35–2:00)
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
- **3b** turns the table into a Word brief for payroll; they find it in the **Output folder**.
- **Requirements** (host; see the [readiness checklist](readiness-checklist.md) and
  [reference/10-cowork-browser.md](reference/10-cowork-browser.md)): browser access allowed for the
  attendee group, Edge 152 or later, Cowork open **in Edge on the web**, an Edge profile signed in
  with the **workshop account** (not InPrivate), and the Edge **Cowork** setting on. Anyone blocked
  follows your demo.
- **Stretch for fast finishers:** the DOL's interactive **FLSA Overtime Security Advisor**, with
  Cowork saying each answer before it clicks. It shows multi-step form navigation without
  submitting anything personal.

### Ex 4 — Build a custom skill (2:00–2:30) — the centerpiece
- Build it live from **Customize → Skills → Add → Create new**.
- Read the **auto-evaluation** aloud; explain the four scoring dimensions and the bands.
- Demo both a **triggering** question and an **out-of-scope** one (salary) to show scope boundaries.
- If someone scores "Needs work," coach them: tighten the **trigger wording** and **scope**.
- **Shared-tenant tip:** tell everyone to keep their skill **"Only you"** (or add initials) so you
  don't end up with 25 identically named skills shared across the tenant.
- Foreshadow Ex 8: this skill helps **you** in Cowork; later we build an **agent** others can use.

### Ex 5 — Recruiting + reporting (2:30–2:45)
- **Job posting (5a):** the follow-on to Ex 2. Ex 2 prepared the interview; 5a writes the posting
  that attracts candidates. Discuss the **wording-review table**: typical flags are the degree
  requirement and "1–3 years" read as must-haves. Ask the room whether they agree with every flag;
  HR keeps the final judgment.
- Ticket summary: the sample data has **6 open / 14 closed** tickets and exactly **one** high-priority
  open item — **T-2008** (overtime missing from a paycheck). T-2003 and T-2013 are also High but
  already closed — a good check on whether Cowork read the Status column. Full expected results:
  [facilitator-answer-key.md](facilitator-answer-key.md).
- Keep this a one-off report; they'll turn it into a scheduled **Automation** in Exercise 7.

### Break (2:45–2:55)
- Second reset. Check that everyone's Exercise 4 skill saved — Ex 7 shares it. Restart on time.

### Ex 6 — Onboarding pack (2:55–3:15)
- **Story:** **Sofia Alvarez** (fictional, no account) accepted the HR Coordinator role from Ex 2
  and Ex 5 and starts **next Monday**. The kickoff prompt gives a concrete time (9:30 AM) so Cowork
  doesn't have to guess.
- This exercise shows off **more built-in skills**: PowerPoint (deck), Scheduling/Calendar (kickoff),
  and Communications (announcement). Call out each new **skill chip** as it loads.
- Reinforce shared-tenant safety: for the kickoff invite, attendees invite **themselves only** — no
  real people — and everything stays a reviewed draft.
- If you're short on time, have them do 6a + 6c and skip 6b, or make 6b a demo-only.

### Ex 7 — Automate & share (3:15–3:30)
- Create an **Automation** live (weekly Monday ticket digest). The prompt names the **exact file and
  folder** (`hr-tickets-sample.xlsx` in `Documents/ai_hr_cowork_workshop`) because a scheduled run can't ask for
  clarification. Choose **Activate and run now** so the room sees a real run, then show the **Runs**
  vs **Manage schedules** tabs so they know where to edit/pause.
- Demo a **Daily Briefing**, then walk the **Share / Re-share** flow on the custom skill from Ex 4.
- Emphasize etiquette: keep skills **"Only you"** or initialed; sharing stays within this tenant.

### Spotlight — Extend Cowork with HR plugins (3:30–3:35, talk only)
- **No hands-on.** Attendees are already on **Customize** after sharing their skill in Ex 7, so
  bridge with: "Skills package *how* you work; plugins connect Cowork to the *systems* you work in."
- Show **Customize → Plugins** on the slide (screenshot from Microsoft Learn) or live in **your own
  tenant** if you have a plugin installed. Point out **Installed** (on/off toggles), the **detail
  page** (skills, connectors, what data it reaches), **Discover**, and **Upload plugin**.
- Name HR plugins from Microsoft's published list
  ([Available plugins for Copilot Cowork](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-available-plugins)): **Gusto** (payroll, employee records, benefits
  enrollment), **ZipRecruiter** and **Dice.com** (job listings), **Cronofy MCP** (interview
  scheduling), **Articulate** (training outlines). Explain that connectors can be **MCP servers**,
  so IT can also connect the organization's **own HR system** as a custom plugin.
- **Expect the SAP SuccessFactors question.** There's no SuccessFactors plugin in the Cowork catalog
  yet (checked Oct 1, 2026). Point to the **Employee Self-Service agent** with its SAP SuccessFactors
  extension pack (a Copilot agent, not a Cowork plugin), or a **custom plugin** with an MCP connector
  built by IT. Re-check the catalog link before each delivery; it keeps growing.
- Walk the **T-2008 payroll example** from [reference/09-plugins.md](reference/09-plugins.md): with a
  payroll plugin, Cowork joins the ticket spreadsheet with live payroll data, then waits for approval.
- Land the benefits: fewer copy-and-paste hand-offs between systems; consistent answers across the
  team; **governed by IT** (approval, deployment, Purview audit logs); **no extra access** (each
  connector uses the person's own sign-in).
- Remind the room: **don't add or upload plugins in the shared tenant**; most need admin approval.
- Bridge to Ex 8: "Plugins bring other systems *into* Cowork. Next, Agent Builder lets you build a
  helper *other people* can use."

### Ex 8 — Agent Builder, non-Cowork (3:35–3:55)
- Step **outside Cowork**: open Microsoft 365 Copilot → **Create agent** and build the **HR Policy
  Agent** live. See [reference/08-agent-builder-policy-agent.md](reference/08-agent-builder-policy-agent.md).
- Make the skill-vs-agent distinction explicit: the Ex 4 skill helps **you**; this **agent** is a
  standalone helper **others** can chat with in Copilot.
- Walk the **Describe → Configure → Try it** tabs; add the Zava HR docs as **knowledge**; test a
  policy question (sourced answer) and an out-of-scope one (declines).
- Note it's **no-code** but a **different tool** — needs a Copilot license, desktop/web only, and for
  external *actions* you'd move to Copilot Studio (out of scope). Good moment to show the breadth of
  the Copilot platform beyond Cowork.

### Wrap-up (3:55–4:00)
- Keep it tight: this segment is 5 minutes.
- Recap the **three tools**: Copilot Chat (quick answers), Cowork (get work done), Agent Builder
  (stand up a reusable helper).
- Remind everyone to **pause or delete the Exercise 1 and Exercise 7 schedules** if they don't want
  them to keep running.
- Recap the five golden rules from [reference/06-responsible-use.md](reference/06-responsible-use.md).
- Point to the [prompt library](reference/04-prompt-library.md) as their takeaway.
- Run a **quick knowledge check** as a show of hands (deck slide: pick 2–3 of the 4 questions;
  questions and answers in [after-the-workshop.md](after-the-workshop.md)), then revisit the learning
  objectives.
- Have them name one task they'll try in real work next week.
- **Next day:** send [after-the-workshop.md](after-the-workshop.md) (full knowledge check, feedback
  survey, and 30-day adoption plan).

## Troubleshooting triage (hand to proctors)

| Symptom | Likely cause | Fix / fallback |
| --- | --- | --- |
| No **Cowork** toggle | Account missing license / Cowork not enabled | Host swaps to a spare licensed account; attendee uses **fallback follow-along** meanwhile (see the [answer key](facilitator-answer-key.md#fallback-walkthrough-for-attendees-who-cant-run-cowork)) |
| Prompt returns nothing / error | Usage-based billing not enabled | Host confirms tenant billing; fallback follow-along |
| Can't sign in / bad credentials | Account distribution mix-up | Proctor issues a spare account |
| Can't find sample files | Staged location not shared | Point to the Teams/SharePoint copy; proctor helps copy to OneDrive |
| Custom skill option missing | On mobile | Switch to laptop/desktop |
| Sees others' skills in the list | Shared tenant + org-shared skills | Keep skills **"Only you"** or initialed |
| Cowork acted without asking | **Approve All** or **Always allow** was clicked earlier in the session | Side panel → **Permissions** → revoke; start a **new task** to reset; check Sent/Deleted items |
| **Create agent** option missing (Ex 8) | On mobile, or wrong Copilot surface | Use desktop/web Microsoft 365 Copilot (Chat/Teams); confirm Copilot license |
| Command center is nearly empty (Ex 1) | Fresh account with little calendar/Teams history | Expected — focus on the pattern; show your richer demo; seed events/emails next time |
| Can't find the output file (any exercise) | Side panel closed, or looking in the chat | Open the **side panel toggle** → **Output folder**; or open **OneDrive → Cowork** |
| Schedule not created (Ex 1) | Checkpoint declined or `[time]` left blank | Re-run the last line of the prompt with a real time, or create it in Automations |
| Deep Research slow (Ex 2) | Multi-source research takes several minutes | Expected: discuss while it runs; demo the scorecard if the room is behind |
| "Browser tasks run in Microsoft Edge" (Ex 3) | Not in Edge, Edge profile isn't the workshop account, InPrivate window, or Edge older than 152 | Open Cowork in Edge in a profile signed in with the workshop account; update Edge; else watch the facilitator demo |
| Browser task never starts (Ex 3) | Browser access not allowed for this account, the Edge **Cowork** setting is off, or the consent notice wasn't accepted | Select **I understand** at the consent notice; host checks Copilot → Settings → Cowork settings → **Allow browser access** includes the attendee group |
| Falling behind | Group pace variance | Use **checkpoints** to sync; stretch prompts for fast finishers |
| **Whole room** can't use Cowork | Service or tenant outage | Stop after 10 minutes; switch to [Plan B](readiness-checklist.md#plan-b--if-cowork-is-down-for-the-whole-room) |

## Time checks and what to cut

Four hours with eight exercises has no slack, so check the clock at these points and cut **in this
order** if you're behind. Never cut Ex 4 or the core of Ex 8.

| Clock | You should be... | If you're more than 10 minutes behind |
| --- | --- | --- |
| **0:40** | Starting Ex 1 | Finish file copying during Ex 1; proctors help stragglers |
| **1:05** | Starting Ex 2 | Have the room skip the Ex 1 discussion; demo the Output folder only |
| **1:25** | Starting the first break | Shorten the break to 5 minutes |
| **2:00** | Starting Ex 4 | Skip Ex 3b (the Word brief); demo the Ex 2 scorecard if not done |
| **2:45** | Starting the second break | Drop the Ex 5 stretch; shorten the break to 5 minutes |
| **3:15** | Starting Ex 7 | Ex 6: do 6a + 6c, demo 6b. Ex 7: do 7a only, demo 7b and 7c |
| **3:35** | Starting Ex 8 | Run Ex 8 as a facilitator demo; attendees build it after class |

**Fast room?** Use the **Stretch** prompts, or have early finishers try a prompt from the
[prompt library](reference/04-prompt-library.md).

## Pacing tips for ~25 people

- Use the **✅ Checkpoints** in the workbook as sync points — "raise a hand when you hit the
  checkpoint."
- Keep **stretch prompts** ready so fast finishers stay engaged while others catch up.
- Don't let one tenant issue stall the room — **parking lot** it and keep moving; a proctor follows up.
- Timings are guidance; if you're running long, shorten Ex 6 (do 6a + 6c, demo 6b) and/or run Ex 8
  as a **facilitator demo** (attendees watch, then build after) — protect Ex 4 and the Ex 8 concept.

## Success criteria

By the end, each ready attendee has:
- [ ] Understood when to use **Copilot Chat vs. Cowork** (opening segment)
- [ ] Toured the Cowork UI — **New task, My tasks, Automations, Customize** (walkthrough)
- [ ] Built an **Executive Command Center** HTML dashboard, found it in the **Output folder** and
  OneDrive → Cowork, and saved it as a skill with a schedule, approving one action at a time (Ex 1)
- [ ] Produced a cited web-research briefing and an interviewer **scorecard in Word and Excel** (Ex 2)
- [ ] Had Cowork **navigate two websites** in Edge and turn the result into a Word brief (Ex 3)
- [ ] Built and tested a custom skill scoring Good+ (Ex 4)
- [ ] Wrote an inclusive job posting and a ticket report (Ex 5)
- [ ] Built an onboarding pack — deck, scheduled kickoff, and team announcement (Ex 6)
- [ ] Created a recurring Automation and walked the skill-sharing flow (Ex 7)
- [ ] Built and tested an **HR Policy Agent** in Copilot Agent Builder (Ex 8)
