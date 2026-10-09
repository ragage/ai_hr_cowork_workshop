# 05 · Custom Skill Guide

> How to build, evaluate, and share a custom skill in Copilot Cowork.
> This backs **Exercise 3**, where you build the "HR Policy Answer" skill.

## What a custom skill is (and when to build one)

A **custom skill** teaches Cowork to handle a **recurring task consistently** — the same tone,
structure, and rules every time — without you re-explaining it in each prompt. Build one when you
find yourself typing the same kind of instructions repeatedly.

Good HR candidates:
- Answering policy/benefits questions in a consistent, sourced format.
- Drafting new-hire welcome messages in your team's voice.
- Producing a standard weekly HR ticket summary.

## Three ways to create a custom skill

1. **Guided Customize page** *(used in the workshop)* — Cowork walks you through naming, describing,
   and writing the skill in one session.
2. **Ask in chat** — tell Cowork you'd like help creating a skill, or describe what it should do, and
   it guides you through the same steps.
3. **Add a `SKILL.md` file** — in your OneDrive `/Documents/Cowork/skills/` folder, create a
   **subfolder** for the skill (e.g., `hr-policy-answer/`) and put a file named exactly **`SKILL.md`**
   inside it, with `name` and `description` front matter. Cowork finds it at the start of your next
   session. You can also **upload** a `.md`, `.zip`, or `.skill` file: **Customize → Skills →** the
   arrow next to **Add → Upload skill**. Only upload skills from sources you trust.

> Custom skills save to your OneDrive at `/Documents/Cowork/skills/{skill-name}/SKILL.md` and are
> available in your next session. **Not supported on mobile.**
>
> **Limits:** up to **50** custom skills; each `SKILL.md` up to **1 MB**; up to **20 companion files**
> (reference documents or scripts) and **10 MB** in total per skill.
> ([Microsoft Learn](https://learn.microsoft.com/microsoft-365/copilot/cowork/use-cowork#cowork-skills))

## Step-by-step: build from the Customize page

1. In Cowork, open the **Customize** page from the left navigation.
2. Select the **Skills** tab.
3. Select **Add** → **Create new**. Cowork opens a new session and starts a guided flow.
4. Answer the prompts to define the skill's **name, description, category, and instructions**. Cowork
   drafts the `SKILL.md` as you go.
5. When you're happy with the draft, **confirm in chat**. Cowork saves the skill to your OneDrive,
   where it becomes available next session.

## How Cowork evaluates your skill

When you create, update, or validate a skill, Cowork **automatically evaluates it** and returns a
plain-language quality report — you don't have to ask.

A skill can fail two ways, and evaluation checks for both:
- It **doesn't trigger** when it should (or steals requests meant for another skill).
- It **triggers but does the wrong thing**.

### Evaluation depth (scales with reach + risk)

| Depth | What runs |
| --- | --- |
| **Minimal** | Structural validation and a quality score |
| **Standard** | Adds a behavioral test |
| **Full** | Adds asset validation, a trust-and-safety set, and a conflict scan |
| **Maximal** | Adds human review, a regression suite, and an adversarial test set |

High-risk skills always run at least **Full**. If nothing changed since the last evaluation, Cowork
skips the run.

### The score (0–100)

Four dimensions, 25 points each:
- **Trigger clarity** — fires at the right time.
- **Instruction specificity** — knows what to do.
- **Scope boundaries** — stays within its purpose.
- **Robustness** — handles unexpected input safely.

Bands: **Excellent** (85+), **Good** (70–84), **Needs work** (50–69), **Poor** (<50).

> **Aim for Good or Excellent.** If you land in "Needs work," the report tells you which dimension to
> improve — usually clearer trigger wording or tighter scope.

## Sharing a skill

Open the skill's detail page on the **Customize** page, select **Share**, and choose **Only you** or
**Specific users in your organization**. If you change a shared skill, select **Re-share** to update
everyone. Sharing stays **within your own organization**.

## What makes a strong skill (checklist)

- [ ] **Clear trigger** — describe exactly when Cowork should use it ("when an employee asks a
      policy or benefits question…").
- [ ] **Specific instructions** — the steps and the output format.
- [ ] **Tight scope** — say what it should *not* do, so it doesn't overreach.
- [ ] **Safe defaults** — for HR, always "cite the source and remind the reader HR should confirm."
- [ ] **Reviewed output** — the skill should produce a draft, not auto-send.

## Example skill

See [../skills/hr-policy-answer/SKILL.md](../skills/hr-policy-answer/SKILL.md) for a ready-made
`SKILL.md` you can compare your workshop skill against. To use it directly, copy the whole
`hr-policy-answer` folder into your OneDrive `/Documents/Cowork/skills/` folder, or upload the file
from **Customize → Skills → Upload skill**.
