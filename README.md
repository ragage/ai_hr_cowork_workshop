# Getting Things Done with Copilot Cowork for HR Tasks
### A 4-hour, hands-on workshop kit for HR teams

This kit contains everything you need to run (or attend) a 4-hour, hands-on workshop that teaches
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
6. **Apply HR guardrails:** fictional or permitted data only, cite and confirm policy answers, and
   keep people-related judgments with people.

## Who it's for

- **Audience:** HR practitioners doing day-to-day operations.
- **Level:** No-code, beginner-friendly.
- **Group size:** designed for ~25 attendees.
- **Tenant model:** the **~25 attendees share one common tenant**, each signing in with **their own
  user account** — so each person has their own OneDrive, drafts, and skills, while org
  search/grounding is **consistent across attendees**. The **facilitator demos from their own
  separate tenant**, so the instructor's screen may look a little different from the attendees'.
  Exercises run on **shared sample files** each person copies into their own OneDrive.

## Prerequisites

The **~25 attendees share one common tenant** provisioned by the host, each with a **licensed user
account**; the **facilitator uses their own separate (demo) tenant**. The host/tenant admin ensures
each attendee account has a **Microsoft 365 Copilot** license and is covered by a **Cowork spending
policy** (usage-based billing; this is what grants Cowork access), with **Cowork Browsing** allowed for
the Exercise 3 browser task. Attendees need a **laptop/desktop** with **Microsoft Edge** (version 152 or
later) signed in with their workshop account (custom skills and browser tasks aren't supported on mobile). Full details and a host checklist:
[readiness-checklist.md](readiness-checklist.md).

## Agenda (240 minutes)

| Time | Segment |
| --- | --- |
| 10 min | Welcome & context — what Cowork is, HR value, the approval model |
| 10 min | **Copilot vs. Cowork** — the difference and when to use which |
| 20 min | **Cowork UI walkthrough** + setup — New task, My tasks, Automations, Customize, sign in, copy data |
| 25 min | **Exercise 1** — Executive Command Center (interactive HTML dashboard; approvals one at a time) |
| 20 min | **Exercise 2** — Research the web with Deep Research (cited briefing + Word/Excel scorecard) |
| 10 min | Break |
| 25 min | **Exercise 3** — Navigate websites with Cowork's browser (search and click through dol.gov and lni.wa.gov in Edge) |
| 30 min | **Exercise 4** — Build your own custom skill ("HR Policy Answer") |
| 15 min | **Exercise 5** — Recruiting + reporting mini-lab |
| 10 min | Break |
| 20 min | **Exercise 6** — Onboarding pack (PowerPoint + Scheduling + Communications) |
| 15 min | **Exercise 7** — Automate & share (Automations, Daily Briefing, skill sharing) |
| 5 min | **Spotlight** — Extend Cowork with HR plugins (Customize → Plugins; talk only, no hands-on) |
| 20 min | **Exercise 8** — Build a Policy Agent with **Copilot Agent Builder** (non-Cowork) |
| 5 min | Wrap-up — best practices & next steps |

## What's in this kit

> **Every guide comes in two formats:** Markdown (`.md`, for viewing and editing in GitHub or VS Code)
> and **Word** (`.docx`, for printing, sharing, and editing in Microsoft 365). The Word versions have
> the same content, with a table of contents on the longer guides, and link to each other. Each is
> listed below with both formats.
>
> Exception: the custom skill file (`skills/hr-policy-answer/SKILL.md`) must stay Markdown for Cowork to
> use it; its `.docx` copy is only for reading and printing.

| File | Formats | Purpose |
| --- | --- | --- |
| README | [.md](README.md) · [.docx](README.docx) | This overview |
| PROJECT-SUMMARY | [.md](PROJECT-SUMMARY.md) (maintainers only) | Handoff notes: status, architecture, decisions, how to build and test, remaining work |
| [instructor-deck.pptx](instructor-deck.pptx) | pptx | Instructor deck (54 slides, speaker notes, alt text) — a divider slide with a picture and progress tracker before each exercise, one PowerPoint section per exercise for quick navigation, objectives, approvals, a scenario card + **demo video slide** + hands-on slide per exercise, an Output folder walkthrough, a **check the cost (`/cost`)** step, an HR plugins spotlight, and a knowledge check |
| [customer-preview-deck.pptx](customer-preview-deck.pptx) | pptx | **Customer preview deck** (17 slides, speaker notes) to walk a prospective customer through the training *before* delivery: goals, agenda, the 8 exercises, safety, takeaways, prerequisites, and cost, then feedback questions, tailoring options, a feedback capture table, and next steps |
| readiness-checklist | [.md](readiness-checklist.md) · [.docx](readiness-checklist.docx) | Prep timeline, cost planning, whole-room Plan B, and setup for hosts + attendees |
| seed-content | [.md](seed-content.md) · [.docx](seed-content.docx) | Ready-made Zava emails, meetings, and a Teams chat to seed attendee accounts (Exercise 1) |
| facilitator-guide | [.md](facilitator-guide.md) · [.docx](facilitator-guide.docx) | Minute-by-minute run sheet, talking points, troubleshooting |
| facilitator-answer-key | [.md](facilitator-answer-key.md) · [.docx](facilitator-answer-key.docx) | Expected results and verified figures for every exercise; fallback walkthrough |
| participant-workbook | [.md](participant-workbook.md) · [.docx](participant-workbook.docx) | Step-by-step attendee exercises with checkpoints |
| [quick-reference-card.docx](quick-reference-card.docx) | docx | One-page printable handout: tools, prompt recipe, approvals, UI map, golden rules |
| after-the-workshop | [.md](after-the-workshop.md) · [.docx](after-the-workshop.docx) | Knowledge check, feedback survey (for Microsoft Forms), and 30-day adoption plan |
| reference/00-copilot-vs-cowork | [.md](reference/00-copilot-vs-cowork.md) · [.docx](reference/00-copilot-vs-cowork.docx) | Copilot Chat vs. Cowork — the difference (training opener) |
| reference/01-cowork-overview | [.md](reference/01-cowork-overview.md) · [.docx](reference/01-cowork-overview.docx) | What Cowork is and where to use it |
| reference/02-settings-and-models | [.md](reference/02-settings-and-models.md) · [.docx](reference/02-settings-and-models.docx) | Settings, model picker, reasoning effort, automations |
| reference/03-skills-catalog | [.md](reference/03-skills-catalog.md) · [.docx](reference/03-skills-catalog.docx) | Built-in skills and how skills work |
| reference/04-prompt-library | [.md](reference/04-prompt-library.md) · [.docx](reference/04-prompt-library.docx) | Copy-paste HR prompts by scenario |
| reference/05-custom-skill-guide | [.md](reference/05-custom-skill-guide.md) · [.docx](reference/05-custom-skill-guide.docx) | How to build, evaluate, and share a custom skill |
| reference/06-responsible-use | [.md](reference/06-responsible-use.md) · [.docx](reference/06-responsible-use.docx) | Data handling and responsible-use rules |
| reference/07-cowork-ui-walkthrough | [.md](reference/07-cowork-ui-walkthrough.md) · [.docx](reference/07-cowork-ui-walkthrough.docx) | UI tour — New task, My tasks, Automations, Customize |
| reference/08-agent-builder-policy-agent | [.md](reference/08-agent-builder-policy-agent.md) · [.docx](reference/08-agent-builder-policy-agent.docx) | Build a Policy Agent with Copilot Agent Builder (Exercise 8) |
| reference/09-plugins | [.md](reference/09-plugins.md) · [.docx](reference/09-plugins.docx) | Spotlight: extend Cowork with HR plugins (Customize → Plugins), with an MCP example for IT |
| reference/10-cowork-browser | [.md](reference/10-cowork-browser.md) · [.docx](reference/10-cowork-browser.docx) | Navigate websites with Cowork's browser: what it is, how to turn it on, troubleshooting (Exercise 3) |
| skills/hr-policy-answer/SKILL | [.md](skills/hr-policy-answer/SKILL.md) (used by Cowork) · [.docx](skills/hr-policy-answer.SKILL.docx) (read-only copy) | Example custom skill (reference/answer key) |
| [sample-knowledge/](sample-knowledge) | folder | Fictional *Zava* HR data: the Word/Excel files used in the exercises, plus their editable .md/.csv sources |
| [zava-sample-knowledge.zip](zava-sample-knowledge.zip) | zip | The six Word and Excel sample files, zipped for easy upload to OneDrive |
| [tools/](tools) | folder (maintainers only) | Scripts that build the deck, Word copies, quick-reference card, and sample files, plus the kit checks. See [How to build](#how-to-build-maintainers) |

### Sample data (all fictional — no real PII)

Every exercise uses the **Word and Excel** sample files. They work in both Cowork and Agent Builder
(which doesn't accept .md or .csv). Download **[zava-sample-knowledge.zip](zava-sample-knowledge.zip)**
to get all six at once, then upload them to a folder named **`ai_hr_cowork_workshop`** under
**Documents** in your OneDrive (`Documents/ai_hr_cowork_workshop`); the prompts use that path.

| File | Contents | Used in |
| --- | --- | --- |
| [employee-handbook-excerpt.docx](sample-knowledge/employee-handbook-excerpt.docx) | PTO, remote work, code of conduct, overtime, reviews | Ex 3, 4, 6, 8 |
| [benefits-summary.docx](sample-knowledge/benefits-summary.docx) | Health, retirement, enrollment windows | Ex 4, 6, 8 |
| [onboarding-checklist.docx](sample-knowledge/onboarding-checklist.docx) | New-hire onboarding steps | Ex 6 |
| [job-description-sample.docx](sample-knowledge/job-description-sample.docx) | Open HR Coordinator role | Ex 2, 5 |
| [employee-roster-sample.xlsx](sample-knowledge/employee-roster-sample.xlsx) | 20 fictional employees | Ex 5 (stretch) |
| [hr-tickets-sample.xlsx](sample-knowledge/hr-tickets-sample.xlsx) | 20 fictional HR tickets | Ex 1 (stretch), 5, 7 |

> **Editing the sample data?** The `.md` and `.csv` files in `sample-knowledge/` are the editable
> sources the Word and Excel files are generated from. Attendees don't need them, and they aren't in
> the zip. If you change one, run `python tools\make_office_samples.py` to regenerate the Word and
> Excel copies and the zip (see [How to build](#how-to-build-maintainers)).

## How to use this kit

1. **Account team + facilitator (4–6 weeks out):** walk the customer through
   [customer-preview-deck.pptx](customer-preview-deck.pptx), capture their feedback on the feedback
   slide, and tailor scenarios, data, and format before you lock the plan.
2. **Host (3 weeks out):** follow the [preparation timeline](readiness-checklist.md#preparation-timeline).
   Provision accounts, estimate cost, and load [seed-content.md](seed-content.md) the day before.
3. **Facilitator:** read [facilitator-guide.md](facilitator-guide.md), do a full dry run against the
   [answer key](facilitator-answer-key.md), and present with
   [instructor-deck.pptx](instructor-deck.pptx) (speaker notes carry the run sheet).
4. **Attendees:** on the day, follow [participant-workbook.md](participant-workbook.md) start to
   finish, with the printed [quick-reference card](quick-reference-card.docx) and the
   [prompt library](reference/04-prompt-library.md) open.
5. **Afterward:** send [after-the-workshop.md](after-the-workshop.md) (knowledge check, survey, and
   30-day plan) and pause the Exercise 1 and 7 schedules.
6. **Everyone:** treat every Cowork output as a **draft to review**, approve **one action at a
   time**, and use only the fictional sample data during exercises.

## How to build (maintainers)

The instructor deck, the customer preview deck, the Word copies of the guides, the quick-reference
card, and the sample Word/Excel files and zip are all generated by the scripts in [tools/](tools). Edit
the Markdown guides (or `tools/content.py` for the exercise text both decks use), then rebuild. Don't
edit the generated `.docx` and `.pptx` files by hand; the next build overwrites them. (Filling in the
customer name or the feedback table in a copy of the preview deck is fine.)

**You need:** Windows with PowerPoint and Word (Word updates the contents pages), and Python 3.14 with
`pip install python-pptx python-docx openpyxl pypandoc_binary Pillow lxml PyMuPDF`.

**Inputs and settings** (environment variables; all optional except the template):

| Variable | Default | What it is |
| --- | --- | --- |
| `DECK_TEMPLATE` | `tools/template.pptx` (git-ignored) | The source PowerPoint template the deck is built from. It isn't in the repo; ask the kit maintainer for it. |
| `DECK_UI_SHOT` | `tools/assets/cowork-home.png` | Cowork home-page screenshot for the UI walkthrough slide |
| `DECK_OUT` | `instructor-deck.pptx` | Where to save the deck. Point it elsewhere if the deck is open in PowerPoint. |
| `KIT_BUILD` | `.build/` (git-ignored) | Scratch folder: icons, the Word reference document, QA PDFs |
| `KIT_STALE_TERMS` | none | Extra terms the check should flag, separated by semicolons (for example, the template's name) |
| `PREVIEW_CUSTOMER`, `PREVIEW_DATE` | `[Customer name]`, `[Date]` | Customer name and meeting date on the preview deck's title slide (you can also edit them in PowerPoint) |

**Build everything, then check it:**

```powershell
$env:DECK_TEMPLATE = "C:\path\to\template.pptx"   # or save the template as tools\template.pptx
$env:PYTHONIOENCODING = "utf-8"
python tools\make_office_samples.py   # sample .docx/.xlsx files and zava-sample-knowledge.zip
python tools\build_deck.py            # instructor-deck.pptx (close it in PowerPoint first)
python tools\build_preview_deck.py    # customer-preview-deck.pptx (no template needed)
python tools\make_quickref.py         # quick-reference-card.docx
python tools\make_word_docs.py        # a .docx copy of every guide
powershell -ExecutionPolicy Bypass -File tools\finalize_word.ps1   # update contents pages; QA PDFs in .build
python tools\check_kit.py             # Markdown links and anchors, Word links, stale text
```

`check_kit.py` exits with an error if any link, anchor, or Word hyperlink is broken, or if it finds
stale text (the kit's old title, the old sample folder, or any `KIT_STALE_TERMS`). For a visual check,
export slides with PowerPoint and look at the QA PDFs in `.build`. `PROJECT-SUMMARY.md` and the files
in `tools/` don't get Word copies.

> **Demo videos aren't part of the build.** Facilitators insert their recordings into the deck's
> **Demo** slides in their own copy. Rebuilding replaces `instructor-deck.pptx`, so keep your copy
> with videos elsewhere, and don't commit videos to the repo.

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
- ✅ A **non-Cowork** finale: build a Policy Agent with **Copilot Agent Builder** (Exercise 8),
  flagged **Not Cowork** on its divider, scenario card, and demo slide
- ✅ Checking what a Cowork task **cost** with **`/cost`** (end of Exercise 1)
- ✅ A **demo video slide** per exercise, so the facilitator can play a recorded run instead of waiting
  for a long task
- ✅ A **customer preview deck** to present the training to a prospective customer and gather feedback
  before delivery
- ✅ A talk-only **HR plugins spotlight** on **Customize → Plugins**, with a screenshot and benefits
- ✅ Every exercise introduced with a **scenario card** (workbook + deck)
- ✅ **Learning objectives**, a verified **answer key**, **seed data**, a prep **timeline** with cost
  planning and **Plan B**, a **knowledge check**, and a **30-day adoption plan**
- ✅ Broad HR-lifecycle focus: onboarding, policy/benefits, recruiting, communications, reporting

---

*Sample content depicts the fictional company "Zava" and is for training purposes only.
Divider illustrations: [Fluent Emoji](https://github.com/microsoft/fluentui-emoji) by Microsoft (MIT License).
Product capabilities and available models may vary by tenant and over time; confirm current
behavior in your environment.*
