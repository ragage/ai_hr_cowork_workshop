# Getting Things Done with Copilot Cowork for HR Tasks
### A 2½-hour, hands-on workshop kit for HR teams

This kit contains everything you need to run (or attend) a 2½-hour, hands-on workshop that teaches
**HR professionals** how to use **Microsoft Copilot Cowork** — no code required — for everyday HR
work: onboarding, policy and benefits Q&A, recruiting and interview prep, employee communications,
and reporting.

By the end, attendees will understand **when to use Copilot Chat vs. Cowork**, will have built an
**executive command center**, **researched the web** with Deep Research, had Cowork **navigate websites**
in its browser,
**built their own custom skill**, and finished by building a reusable **agent** with **Copilot Agent
Builder**. Every exercise is introduced with a **scenario card** (Function, Goal, Output, Why
Cowork?, Prompt, Workflow, Data sources).

## Learning objectives

By the end of the workshop, attendees will be able to:

1. **Choose the right tool:** Copilot Chat for quick answers, Cowork for multi-step work that ends
   in a deliverable, and Agent Builder for a reusable helper others can use.
2. **Delegate safely:** describe an outcome, follow Cowork's plan, and approve actions one at a
   time, with drafts reviewed before anything is sent.
3. **Ground work in real content:** attach or reference files, research and browse the web with citations,
   and check outputs against the source.
4. **Package repeatable work:** build and evaluate a custom skill, then schedule recurring work
   with Automations.
5. **Build a no-code agent** in Copilot Agent Builder, grounded in HR documents and scoped to decline
   out-of-scope questions.
6. **Apply HR guardrails:** keep real data private, cite and confirm policy answers, and
   keep people-related judgments with people.

## Who it's for

- **Audience:** HR practitioners doing day-to-day operations.
- **Level:** No-code, beginner-friendly.
- **Group size:** designed for ~25 attendees.
- **Tenant and data model:** the **~25 attendees sign in with their own work accounts** in their
  organization's tenant, so each person has their own OneDrive, drafts, and skills. **Exercise 1** runs
  on each attendee's **own mail, calendar, and Teams** (the results stay private to them); **every other
  exercise** uses the fictional **Zava sample files** each person copies into their own OneDrive. The
  **facilitator demos from a separate demo tenant**, seeded with [seed-content.md](instructor/seed-content.md),
  so the instructor's screen may look a little different from the attendees'.

## Prerequisites

The **~25 attendees use their own work accounts** (no workshop accounts to provision); the
**facilitator uses a separate (demo) tenant**. The host/tenant admin ensures
each attendee has a **Microsoft 365 Copilot** license and is covered by a **Cowork spending
policy** (usage-based billing; this is what grants Cowork access), with **Cowork Browsing** allowed for
the Exercise 3 browser task. Attendees need a **laptop/desktop** with **Microsoft Edge** (version 152 or
later) signed in with their work account (custom skills and browser tasks aren't supported on mobile). Full details and a host checklist:
[readiness-checklist.md](instructor/readiness-checklist.md).

## Agenda (2½ hours)

| Time | Segment |
| --- | --- |
| 5 min | Welcome & context — what Cowork is, HR value, the approval model |
| 5 min | **Copilot vs. Cowork** — the difference and when to use which |
| 10 min | **Cowork UI walkthrough** + setup check — New task, My tasks, Automations, Customize (attendees sign in and upload the sample files before the session) |
| 15 min | **Exercise 1** — Executive Command Center (interactive HTML dashboard; approvals one at a time) |
| 15 min | **Exercise 2** — Research the web with Deep Research (cited briefing + 5 tailored interview questions) |
| 15 min | **Exercise 3** — Navigate websites with Cowork's browser (search and click through dol.gov and lni.wa.gov in Edge) |
| 15 min | **Exercise 4** — Build your own custom skill ("HR Policy Answer") |
| 10 min | **Exercise 5** — Recruiting + reporting mini-lab |
| 15 min | Break |
| 10 min | **Exercise 6** — Onboarding pack (orientation deck; scheduling + announcement if time allows) |
| 15 min | **Exercise 7** — Automate & share (Automations, Daily Briefing; skill sharing if time allows) |
| 15 min | **Exercise 8** — Build a Policy Agent with **Copilot Agent Builder** (non-Cowork) |
| 5 min | Wrap-up — best practices & next steps |

The pace is brisk: the facilitator plays a short **demo video** before each exercise instead of waiting
on long Cowork runs, and the **HR plugins** read (Customize → Plugins) is in the
[after-the-workshop pack](participant/after-the-workshop.md) for self-study.

## What's in this kit

> **Every guide comes in two formats:** Markdown (`.md`, for viewing and editing in GitHub or VS Code)
> and **Word** (`.docx`, for printing, sharing, and editing in Microsoft 365). The Word versions have
> the same content, with a table of contents on the longer guides, and link to each other. Each is
> listed below with both formats.
>
> Exception: the custom skill file (`skills/hr-policy-answer/SKILL.md`) must stay Markdown for Cowork to
> use it; its `.docx` copy is only for reading and printing.

The kit is organized by audience:

- **[participant/](participant)** — what attendees use: the workbook, the quick-reference card, and the
  after-the-workshop pack.
- **[instructor/](instructor)** — what the facilitator and host use: the instructor deck, facilitator
  guide, answer key, readiness checklist, and the facilitator's demo seed content.
- **[communication/](communication)** — what you send out: the training overview deck and paste-ready
  Outlook emails for participants and instructors.
- **[sample-knowledge/](sample-knowledge)** — the **only** place for the Zava sample data: the six Word and
  Excel files, and **one zip** with all six for attendees to download.
- **[reference/](reference)** and **[skills/](skills)** — background guides and the example custom skill.

> **Downloading a file from GitHub:** if a link opens the file on GitHub instead of downloading it,
> select the **Download** icon (**Download raw file**) at the top right of the file.

![Tip: on a GitHub file page, select the Download icon (Download raw file) at the top right of the file](reference/media/download-hint.png)

| File | Formats | Purpose |
| --- | --- | --- |
| README | [.md](README.md) · [.docx](README.docx) | This overview |
| summary/PROJECT-SUMMARY | [.md](summary/PROJECT-SUMMARY.md) (maintainers only) | Handoff notes: status, architecture, decisions, how to build and test, remaining work |
| [instructor/instructor-deck.pptx](instructor/instructor-deck.pptx) | pptx | Instructor deck (57 slides, speaker notes, alt text) — a **prompting best-practices slide** (Goal, Source, Expectations, Constraints, with a weak vs. strong HR prompt), a divider slide with a picture and progress tracker before each exercise, one PowerPoint section per exercise for quick navigation, objectives, approvals, a **workshop kit slide with download links** for participants and instructors, a scenario card, **demo video slide** (an empty video frame for your recording), and hands-on slide per exercise (its speaker notes carry the full prompt, ready to copy), demo video slides for the UI walkthrough and the prompting slide, an Output folder walkthrough, an optional **check-the-cost** (`/cost`) slide for Exercise 1, red **Not Cowork** banners on Exercise 8, a knowledge check, and a closing **clean up the training data** slide |
| [instructor/customer-preview-deck.pptx](instructor/customer-preview-deck.pptx) | pptx | Customer preview deck (17 slides) for the account team and facilitator to walk the customer through before delivery — format, agenda, the eight exercises, safety, prerequisites, cost planning, and questions for their feedback; title slide has `[Customer name]` and `[Date]` placeholders |
| [communication/training-overview.pptx](communication/training-overview.pptx) | pptx | Training overview deck (8 slides) for HR leaders and prospective attendees — what the training is, objectives, agenda, the eight exercises, what to prepare, and the same **download links** slide |
| [communication/participant-email.html](communication/participant-email.html) | html | Paste-ready Outlook invitation for attendees: session details, what to bring, and links to the workbook, sample data, and handouts |
| [communication/instructor-email.html](communication/instructor-email.html) | html | Paste-ready Outlook email for the instructor: links to every kit asset, the preparation timeline, and key reminders |
| instructor/readiness-checklist | [.md](instructor/readiness-checklist.md) · [.docx](instructor/readiness-checklist.docx) | Prep timeline, cost planning, whole-room Plan B, and setup for hosts + attendees |
| instructor/seed-content | [.md](instructor/seed-content.md) · [.docx](instructor/seed-content.docx) | Zava emails, meetings, and a Teams chat for the **facilitator's demo account** (Exercise 1), with how to load them through VS Code and the Work IQ MCP server |
| instructor/facilitator-guide | [.md](instructor/facilitator-guide.md) · [.docx](instructor/facilitator-guide.docx) | Minute-by-minute run sheet, talking points, troubleshooting |
| instructor/facilitator-answer-key | [.md](instructor/facilitator-answer-key.md) · [.docx](instructor/facilitator-answer-key.docx) | Expected results and verified figures for every exercise; fallback walkthrough |
| participant/participant-workbook | [.md](participant/participant-workbook.md) · [.docx](participant/participant-workbook.docx) | Step-by-step attendee exercises with checkpoints, ending with training-data clean-up steps |
| [participant/quick-reference-card.docx](participant/quick-reference-card.docx) | docx | One-page printable handout: tools, prompt recipe, approvals, UI map, golden rules |
| participant/after-the-workshop | [.md](participant/after-the-workshop.md) · [.docx](participant/after-the-workshop.docx) | Knowledge check, feedback survey (for Microsoft Forms), and 30-day adoption plan |
| reference/00-copilot-vs-cowork | [.md](reference/00-copilot-vs-cowork.md) · [.docx](reference/00-copilot-vs-cowork.docx) | Copilot Chat vs. Cowork — the difference (training opener) |
| reference/01-cowork-overview | [.md](reference/01-cowork-overview.md) · [.docx](reference/01-cowork-overview.docx) | What Cowork is and where to use it |
| reference/02-settings-and-models | [.md](reference/02-settings-and-models.md) · [.docx](reference/02-settings-and-models.docx) | Settings, model picker, reasoning effort, automations |
| reference/03-skills-catalog | [.md](reference/03-skills-catalog.md) · [.docx](reference/03-skills-catalog.docx) | Built-in skills and how skills work |
| reference/04-prompt-library | [.md](reference/04-prompt-library.md) · [.docx](reference/04-prompt-library.docx) | Copy-paste HR prompts by scenario |
| reference/05-custom-skill-guide | [.md](reference/05-custom-skill-guide.md) · [.docx](reference/05-custom-skill-guide.docx) | How to build, evaluate, and share a custom skill |
| reference/06-responsible-use | [.md](reference/06-responsible-use.md) · [.docx](reference/06-responsible-use.docx) | Data handling and responsible-use rules |
| reference/07-cowork-ui-walkthrough | [.md](reference/07-cowork-ui-walkthrough.md) · [.docx](reference/07-cowork-ui-walkthrough.docx) | UI tour — New task, My tasks, Automations, Customize |
| reference/08-agent-builder-policy-agent | [.md](reference/08-agent-builder-policy-agent.md) · [.docx](reference/08-agent-builder-policy-agent.docx) | Build a Policy Agent with Copilot Agent Builder (Exercise 8) |
| reference/09-plugins | [.md](reference/09-plugins.md) · [.docx](reference/09-plugins.docx) | Self-study: extend Cowork with HR plugins (Customize → Plugins), with an MCP example for IT |
| reference/10-cowork-browser | [.md](reference/10-cowork-browser.md) · [.docx](reference/10-cowork-browser.docx) | Navigate websites with Cowork's browser: what it is, how to turn it on, troubleshooting (Exercise 3) |
| skills/hr-policy-answer/SKILL | [.md](skills/hr-policy-answer/SKILL.md) (used by Cowork) · [.docx](skills/hr-policy-answer.SKILL.docx) (read-only copy) | Example custom skill (reference/answer key) |
| [sample-knowledge/](sample-knowledge) | folder | Fictional *Zava* HR data: the six Word/Excel files used in the exercises, and [zava-sample-knowledge.zip](sample-knowledge/zava-sample-knowledge.zip), the **one download** for attendees (all six in an `ai_hr_cowork_workshop` folder, ready to upload to OneDrive) |

### Sample data (all fictional — no real PII)

The exercises use the **Word and Excel** sample files (Exercise 1 also reads each attendee's own mail and
calendar). They work in both Cowork and Agent Builder
(which doesn't accept .md or .csv). Download **[zava-sample-knowledge.zip](sample-knowledge/zava-sample-knowledge.zip)**
to get all six at once. It extracts to a folder named **`ai_hr_cowork_workshop`**; upload that folder
to **Documents** in your OneDrive (`Documents/ai_hr_cowork_workshop`). The prompts use that path.

| File | Contents | Used in |
| --- | --- | --- |
| [employee-handbook-excerpt.docx](sample-knowledge/employee-handbook-excerpt.docx) | PTO, remote work, code of conduct, overtime, reviews | Ex 3, 4, 6, 8 |
| [benefits-summary.docx](sample-knowledge/benefits-summary.docx) | Health, retirement, enrollment windows | Ex 4, 6, 8 |
| [onboarding-checklist.docx](sample-knowledge/onboarding-checklist.docx) | New-hire onboarding steps | Ex 6 |
| [job-description-sample.docx](sample-knowledge/job-description-sample.docx) | Open HR Coordinator role | Ex 2, 5 |
| [employee-roster-sample.xlsx](sample-knowledge/employee-roster-sample.xlsx) | 20 fictional employees | Ex 5 (stretch) |
| [hr-tickets-sample.xlsx](sample-knowledge/hr-tickets-sample.xlsx) | 20 fictional HR tickets | Ex 1 (stretch), 5, 7 |

> **Editing the sample data?** The Word and Excel files in `sample-knowledge/` are the master copies:
> edit them directly, then rebuild the zip ([how](summary/PROJECT-SUMMARY.md#build-instructions)) so
> attendees always download one zip that matches.

## How to use this kit

1. **Account team + facilitator (4 to 6 weeks out):** walk the customer through the
   [customer preview deck](instructor/customer-preview-deck.pptx) to confirm the format, the exercises,
   and the cost plan, and collect their feedback.
2. **Host (3 weeks out):** follow the [preparation timeline](instructor/readiness-checklist.md#preparation-timeline).
   Confirm licenses and Cowork access, estimate cost, and stage the sample files. The facilitator loads
   [seed-content.md](instructor/seed-content.md) into their own demo account 1–2 days before.
   Send the instructor the [instructor email](communication/instructor-email.html), and attendees the
   [participant email](communication/participant-email.html) one week out; use the
   [training overview deck](communication/training-overview.pptx) to introduce the workshop. To use
   either email, open it in a browser, copy the email, and paste it into Outlook. The participant email
   has highlighted `[link: …]` placeholders for your Teams/SharePoint copies of the files. The instructor
   email links to this private repo, so give the instructor access first.
3. **Facilitator:** read [facilitator-guide.md](instructor/facilitator-guide.md), do a full dry run against the
   [answer key](instructor/facilitator-answer-key.md), and present with
   [instructor-deck.pptx](instructor/instructor-deck.pptx) (speaker notes carry the run sheet).
4. **Attendees:** on the day, follow [participant-workbook.md](participant/participant-workbook.md) start to
   finish, with the printed [quick-reference card](participant/quick-reference-card.docx) and the
   [prompt library](reference/04-prompt-library.md) open.
5. **Afterward:** send [after-the-workshop.md](participant/after-the-workshop.md) (knowledge check, survey, and
   30-day plan) and pause the Exercise 1 and 7 schedules.
6. **Everyone:** treat every Cowork output as a **draft to review**, approve **one action at a
   time**, keep Exercise 1 results private, and use the fictional sample data for the other exercises.

## Requirement coverage

- ✅ **Copilot vs. Cowork** difference explained up front (opening segment)
- ✅ **Cowork UI walkthrough** — New task, My tasks, Automations, Customize (walkthrough segment)
- ✅ Sample knowledge, instructions, prompt library, settings & models overview
- ✅ Using **predefined skills** — Deep Research, Word, Excel, PowerPoint, Scheduling, Calendar,
  Communications, Daily Briefing (Exercises 2, 5, 6 & 7)
- ✅ An **executive scenario** — the **Executive Command Center** (Exercise 1), which also saves
  itself as a skill and schedules itself
- ✅ Creating at least one **custom skill** and **sharing** it (Exercises 1, 4 & 7)
- ✅ Using the **browser / web** to get things done: **Deep Research** (Exercise 2) and Cowork **navigating
  websites in Microsoft Edge**, searching and clicking through two sites (Exercise 3)
- ✅ Using **Automations** for recurring HR work (Exercises 1 & 7)
- ✅ A **non-Cowork** finale: build a Policy Agent with **Copilot Agent Builder** (Exercise 8), flagged
  **Not Cowork** on its slides and in the guides
- ✅ **Cost awareness:** an optional `/cost` check at the end of Exercise 1, plus cost planning in the
  readiness checklist
- ✅ A **customer preview deck** to agree the format and gather feedback before delivery
- ✅ An **HR plugins** read on **Customize → Plugins** for self-study in the after-the-workshop pack
- ✅ Every exercise introduced with a **scenario card** (workbook + deck)
- ✅ **Learning objectives**, a verified **answer key**, facilitator **demo seed data**, a prep **timeline** with cost
  planning and **Plan B**, a **knowledge check**, and a **30-day adoption plan**
- ✅ Broad HR-lifecycle focus: onboarding, policy/benefits, recruiting, communications, reporting

---

*Sample content depicts the fictional company "Zava" and is for training purposes only.
Divider illustrations: [Fluent Emoji](https://github.com/microsoft/fluentui-emoji) by Microsoft (MIT License).
Product capabilities and available models may vary by tenant and over time; confirm current
behavior in your environment.*
