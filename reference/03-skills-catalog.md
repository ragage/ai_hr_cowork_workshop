# 03 · Skills Catalog

> Reference sheet for the "Getting Things Done with Copilot Cowork for HR Tasks" workshop.

## What is a "skill" in Cowork?

A **skill** is a specialized capability Cowork loads to do part of a task. You don't invoke skills
manually — Cowork **activates them automatically** based on what you ask. When a skill loads, you'll
see a message like *"Preparing to compose emails,"* and the skill appears as a **chip** in the
**Skills** section of the side panel, so you always know what Cowork is using.

There are three kinds of skills:

1. **Built-in (out-of-the-box) skills** — included with Cowork.
2. **Custom skills** — ones you create (see Exercise 3 and [05-custom-skill-guide.md](05-custom-skill-guide.md)).
3. **Plugin skills** — added from the Microsoft 365 App Store.

## Built-in skills

| Skill | What it does | Example HR use |
| --- | --- | --- |
| **Word** | Create and edit Word documents | Draft an offer letter or policy one-pager |
| **Excel** | Create and edit spreadsheets | Summarize a roster or ticket log into a table |
| **PowerPoint** | Create and edit presentations | Build an onboarding orientation deck |
| **PDF** | Work with PDF documents | Pull key points from a benefits PDF |
| **Email** | Compose, reply, forward, send; drafts and attachments | Draft a welcome email to a new hire |
| **Scheduling** | Schedule meetings | Set up an onboarding kickoff |
| **Calendar Management** | Create events in natural language, add Teams links, manage calendar | Book recurring 1:1s |
| **Meetings** | Prepare meeting intelligence | Prep notes before an interview panel |
| **Daily Briefing** | Prepare your daily briefing | Start-of-day summary for an HR coordinator |
| **Enterprise Search** | Search across your organization | Find an internal policy or document |
| **Deep Research** | In-depth research across multiple sources | Benchmark external leave-policy norms |
| **Communications** | Draft stakeholder communications | Company-wide benefits-enrollment announcement |
| **Adaptive Cards** | Interactive card responses with layouts, buttons, data | Structured, at-a-glance answers |
| **App (Frontier)** | Build lightweight no-code apps from a description | *Awareness only — needs Frontier* |

> **Note:** The **App (Frontier)** skill requires enrollment in the **Frontier** program. We mention
> it for awareness but don't rely on it in the hands-on exercises.

## Skills we focus on in this workshop

- **Exercise 1** — **Deep Research** (gathers and cites multiple web sources for a briefing), then
  **Word + Excel** for an interviewer scorecard from one follow-up prompt; optional `/cost` review.
- **Exercise 2** — **browser use** in Microsoft Edge (not a skill: Cowork searches and clicks through
  dol.gov and lni.wa.gov), then **Word** for a brief to payroll.
- **Exercise 3** — a **custom skill** you build ("HR Policy Answer").
- **Exercise 4** — Word + Excel (inclusive job posting + ticket reporting).
- **Exercise 5** — PowerPoint + Scheduling/Calendar + Communications (onboarding pack).
- **Exercise 6** — Automations + Daily Briefing + skill sharing.
- **Exercise 7** — Agent Builder (not a Cowork skill).
- **Exercise 8** — Work IQ signals across mail, calendar, chats & files → an interactive **HTML**
  dashboard, saved as a skill and scheduled (Executive Command Center capstone).

## How Deep Research uses the web

The **Deep Research** skill conducts in-depth research **across multiple sources**, including the
web, to compile a comprehensive answer or briefing on a complex topic. This is how Cowork
"navigates the web to get things done" — you describe the question, and it gathers, synthesizes, and
cites information from several sources rather than a single lookup. We use it in Exercise 1.

**Browser use** is the other way Cowork works on the web: it opens a real site in a hidden tab in
**your own Microsoft Edge** and works through it, with your sign-ins and your organization's
policies (no new access). It isn't a skill you pick; Cowork decides when a task needs the browser.
It needs Edge 152 or later and an admin to turn on **Cowork Browsing**. We use it in Exercise 2. See
[10-cowork-browser.md](10-cowork-browser.md).

> **Grounding note:** In this workshop everyone signs in to their **own organization's tenant**, so
> **Enterprise Search** and org-grounded results reflect real content and **differ by person**
> (each of you can see different files). Deep Research reaches **external/web sources**, which is why we use it
> for the web exercise. To keep results identical across the room, exercises still ground on the
> **shared sample files** you copy into your own OneDrive.

## Custom skills at a glance

You can create a custom skill three ways:

1. From the guided **Customize** page.
2. By **asking Cowork in chat** to build one for you.
3. By adding a **`SKILL.md`** file in its own subfolder of your OneDrive `/Documents/Cowork/skills/`
   folder (for example, `/Documents/Cowork/skills/hr-policy-answer/SKILL.md`), or uploading one from
   **Customize → Skills**.

Cowork **auto-evaluates** every skill and gives a plain-language quality report. Full detail is in
[05-custom-skill-guide.md](05-custom-skill-guide.md).
