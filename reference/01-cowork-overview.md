# 01 · Copilot Cowork Overview

> Reference sheet for the "Getting Things Done with Copilot Cowork for HR Tasks" workshop.

## What is Copilot Cowork?

**Microsoft Copilot Cowork** completes **multi-step tasks on your behalf**. You describe the
*outcome* you want — draft an email, build a spreadsheet, schedule a meeting, research a topic — and
Cowork:

1. **Plans** the steps needed to get there.
2. **Picks** the right skills and apps for the job.
3. **Pauses for your approval** at key checkpoints (for example, before sending an email).
4. **Returns finished artifacts** — a document, deck, report, or email — ready for your review.

Cowork grounds its work in your emails, meetings, files, and business data through **Work IQ**, the
workplace intelligence layer behind Microsoft 365 Copilot.

### Cowork vs. Copilot Chat

| Copilot Chat | Copilot Cowork |
| --- | --- |
| Fast Q&A and short single-turn help | Multi-step tasks that produce finished artifacts |
| You stay in the driver's seat step by step | You describe the outcome; Cowork plans and executes |
| Great for "explain / summarize / rewrite" | Great for "produce this deliverable end to end" |

For a fuller comparison and when-to-use-which guidance, see
[00-copilot-vs-cowork.md](00-copilot-vs-cowork.md).

**Rule of thumb for HR:** if the request would normally take *several manual steps* and end in a
document, email, or report, it's a good fit for Cowork.

## Where to use Cowork

Cowork works in:

- The browser at **https://copilot.cloud.microsoft** (select **Cowork** next to **Chat** at the top)
- **Outlook** and **Teams**
- The **Microsoft Copilot desktop app** (Windows and Mac)
- The **Microsoft Copilot mobile app** (iPhone and Android — note: custom skills aren't supported on mobile)

## The Cowork home page

When Cowork loads, the left navigation has four main places:

1. **New task** — the *"What can I do for you?"* home; a **Start a task** box, **model picker**,
   **reasoning effort**, attach (+), dictate, and *"Try these next"* starter suggestions.
2. **My tasks** — find and resume your previous tasks.
3. **Automations** — schedule tasks or run them on events; **Runs** and **Manage schedules** tabs.
4. **Customize** — custom instructions, your personal skills, and plugins.

For a full tour of each area, see [07-cowork-ui-walkthrough.md](07-cowork-ui-walkthrough.md).

## How Cowork uses the web

- **Deep Research** searches and reads many web sources and returns a **cited** briefing.
- **Browser use** lets Cowork work in a real website for you, in a **hidden tab in your own Microsoft
  Edge**, with your existing sign-ins and your organization's policies. It gets **no new access**,
  hands sensitive steps (sign-in, MFA, CAPTCHA) back to you, asks approval for consequential actions,
  and is recorded in the audit log. It needs Cowork on the web in **Edge 152 or later**, signed in with
  your work account, and your admin must turn on **Cowork Browsing** (off by default). The first
  browser task shows a consent notice; select **I understand**.

You'll use Deep Research in Exercise 2 and browser use in Exercise 3. Setup and troubleshooting:
[10-cowork-browser.md](10-cowork-browser.md). Learn: [Use the local browser with Copilot Cowork](https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-local-browser).

## The approval / checkpoint model (why HR should care)

Cowork is designed to **pause at key checkpoints** and show you what it's about to do. Nothing
irreversible — like sending an email or booking a meeting — happens without your confirmation. For
HR work, this matters because you stay accountable for what goes out. Throughout this workshop we
treat every Cowork output as a **draft to review before it's used**.

## This workshop's setup

- You and the other attendees work in **one shared tenant**, signing in with **your own user
  account**, so you each have your own OneDrive, drafts, and skills.
- Because the attendees share one tenant, **org search and grounding are consistent** across the
  room. The **facilitator demos from their own separate tenant**, so the instructor's screen may
  look a little different from yours — that's expected.
- Exercises are built on **provided sample files** you copy into your own OneDrive, so everyone
  works from the same fictional HR data.
- Since attendee accounts share a tenant, keep any **custom skills you build private** ("Only you")
  or add your initials to the name so you don't collide with your neighbors.

## Prerequisites (in the shared attendee tenant)

- A **user account** in the workshop tenant with an active **Microsoft 365 Copilot** license
  (provisioned by the host).
- **Usage-based billing**, with your account in the scope of a **spending policy that selects Cowork**;
  that policy is what grants access.
- **Microsoft Edge** (152 or later), signed in with your workshop account, with **Cowork Browsing**
  turned on by the admin, for the Exercise 3 browser task. Chrome works for everything else.
- *(Optional)* Enrollment in the **Frontier** program — only needed for the built-in **App** skill,
  which is awareness-only in this workshop.

See [readiness-checklist.md](../readiness-checklist.md) for the full pre-workshop setup.
