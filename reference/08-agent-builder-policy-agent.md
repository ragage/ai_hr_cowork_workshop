# 08 · Build a Policy Agent with Copilot Agent Builder

> Reference sheet for the "Getting Things Done with Copilot Cowork for HR Tasks" workshop.
> This backs **Exercise 8** — the closing, **non-Cowork** capstone.

## Cowork skill vs. Agent Builder agent — why both?

In Exercise 4 you built a **custom skill** *inside Cowork* — great for a recurring task **you**
do in your own sessions. Now we step **outside Cowork** to build a **persistent, shareable agent**
that **other people** can chat with directly in Microsoft 365 Copilot.

| | **Custom skill (Cowork, Ex 4)** | **Agent (Agent Builder, Ex 8)** |
| --- | --- | --- |
| Lives in | Your Cowork sessions | Microsoft 365 Copilot (Chat / Teams) |
| Who uses it | You (or people you share the skill with) | Anyone you share/publish the agent to |
| Best for | A repeatable step in your own workflow | A standalone Q&A assistant others can chat with |
| Grounded in | Files you reference in the task | Knowledge sources you attach (SharePoint, web, connectors) |

Both are **no-code**. This shows HR that the Copilot family has the right tool for both "do this task
for me" (Cowork) and "stand up a reusable helper" (Agent Builder).

## What Agent Builder is

**Agent Builder** in Microsoft 365 Copilot is a **no-code, guided** way to create **declarative
agents** — using plain language, no coding experience required. You can:

- Build from a **template** or by **describing** what you want.
- Add **knowledge sources**: SharePoint items, public websites, personal work info (Teams/Outlook),
  and **Copilot connectors** enabled in your tenant.
- **Test** the agent in the tool, then **share** or **publish** it (including to SharePoint or your
  org's catalog).

### Where to find it
Open Microsoft 365 Copilot (**microsoft365.com/chat**, **office.com/chat**, or the **Microsoft 365
Copilot** app/tab in **Teams**) and select **Create agent** / **New agent**.

- Available on **desktop and web** (Work and Web toolbars). **Not** on mobile.
- Requires a **Microsoft 365 Copilot** license; available knowledge sources depend on your tenant's
  licensing.
- Agent Builder is for **knowledge + instructions**. It doesn't author external-service *actions* —
  for those you'd copy the agent into **Microsoft Copilot Studio** (out of scope today).

### The three tabs
- **Describe** — tell the agent what to do in natural language; add knowledge here too.
- **Configure** — set the name, description, instructions, knowledge, and suggested prompts manually.
- **Try it** — test the agent's responses before sharing.

## Exercise 8 — Build the "HR Policy Agent"

**Goal:** stand up a no-code agent that answers employee policy/benefits questions, grounded in the
Zava HR documents, and test it.

### Step 1 — Create the agent
1. In Microsoft 365 Copilot, select **Create agent** (or **New agent**).
2. On the **Describe** tab, tell it what to build, for example:
   > "Create an **HR Policy Agent** that answers employee questions about company policies and
   > benefits — PTO, remote/hybrid work, benefits enrollment, overtime, and the code of conduct — in
   > a warm, professional tone. Always cite the source document and remind the reader that HR should
   > confirm. Politely decline questions about individual pay, performance, legal, or medical matters
   > and redirect them to HR."

### Step 2 — Name, describe, and set instructions (Configure tab)
- **Name:** HR Policy Agent
- **Description:** "Answers employee policy and benefits questions for Zava, grounded in our HR
  documents."
- **Instructions:** paste/adapt the behavior above — answer format (direct answer → details →
  **source** → "confirm with HR"), tone, and the out-of-scope guardrails.

### Step 3 — Add knowledge sources
Point the agent at the Zava HR documents (the same fictional Word files used all day):
`employee-handbook-excerpt.docx` and `benefits-summary.docx`. Either **upload** them from your device
(up to 20 embedded files) or use **Attach cloud files** to pick them from OneDrive/SharePoint.
- **File types matter:** Agent Builder knowledge accepts **.doc/.docx, .pdf, .ppt/.pptx, .txt,
  .xls/.xlsx** (plus .html from SharePoint), but **not Markdown (.md) or .csv**. Keep that in mind
  when you build agents on your own documents.
- Newly added OneDrive/SharePoint files can show **"Preparing"** for a few minutes; you can test
  while they prepare, but answers won't use them until they're ready.
- In a real tenant you'd add the **SharePoint site/library** where HR policies live.
- **Limits worth knowing** (per agent): up to **20 uploaded (embedded) files**, **100 SharePoint
  files**, **50 OneDrive files**, and **4 public websites**. Uploaded .docx/.pdf/.pptx/.txt files can be
  up to 512 MB; Excel files up to 30 MB. See
  [Add knowledge to an agent](https://learn.microsoft.com/microsoft-365-copilot/extensibility/agent-builder-add-knowledge).

### Step 4 — Add suggested prompts
Give users starting points, e.g.:
- "How much PTO do I get and can I carry it over?"
- "When is open enrollment and how do I change my plan?"
- "What are the anchor office days?"

### Step 5 — Test on the "Try it" tab
Ask a policy question and confirm the agent answers **in your format with a source**. Then ask an
**out-of-scope** question (e.g., *"What's my colleague's salary?"*) and confirm it **declines and
redirects**.

### Step 6 — Share / publish (optional)
When you're happy, **share** the agent with specific people or **publish** it (e.g., to a SharePoint
site or submit to the org catalog) so employees can self-serve policy answers in Copilot.

> **Before you share an agent with uploaded files:** people who get the agent can get answers from
> those files' content. Only upload documents everyone you share with may read, and check how
> sensitivity labels and encryption apply (some protected files can't be used as embedded
> knowledge). For real HR policies, point to the **SharePoint library** instead, so each person's
> existing permissions apply.

✅ **Checkpoint:** a working **HR Policy Agent** that answers grounded, sourced policy questions and
declines out-of-scope requests — built with **no code**, outside Cowork.

## Responsible use (same rules apply)
- Ground answers in **official HR documents**; have the agent **cite** and add *"confirm with HR."*
- Use only the **fictional Zava files** as knowledge in the workshop; no real employee personal data.
- Test the **out-of-scope** behavior before you share; an agent others use needs tight scope.
- Review what the agent returns before you publish it broadly.
