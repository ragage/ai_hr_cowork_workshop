# 06 · Responsible Use & Data Handling

> Reference sheet for the "Getting Things Done with Copilot Cowork for HR Tasks" workshop.
> HR works with sensitive people data — these practices keep Cowork use safe and compliant.

## Golden rules for HR

1. **Every Cowork output is a draft.** Review before you send, share, or file anything — especially
   employee communications and policy answers.
2. **Approve at the checkpoints — one at a time.** Cowork pauses before sensitive actions (sending
   email, posting to Teams, deleting, booking meetings). Read the preview (and **Show parameters**)
   before you confirm. Avoid **Approve All** and **Always allow / don't ask again**: they skip
   later checkpoints for the rest of the session. Revoke them in the side panel's **Permissions**
   section.
3. **Keep real data private in this workshop.** Exercise 8 reads your own mail, calendar, and Teams;
   its results stay in your account, so keep them off shared screens. Every other exercise uses the
   fictional *Zava* files: don't paste real employee personal data into them.
4. **Cite and confirm.** For policy answers, have Cowork name the source document and remind the
   reader that HR should confirm — policies change.
5. **Right person, right data.** Cowork acts in *your* context and accesses only what *you* are
   permitted to see. Don't use it to surface information you wouldn't otherwise have access to.

## What "grounding" means for your data

- Cowork grounds answers in your organization's data through **Work IQ**, respecting existing
  **permissions** — it only reaches content you already have access to.
- **Enterprise Search / org-grounded** results come from **your organization's tenant** and differ by
  person, because each of you can see different content. During exercises (except Exercise 8), ground
  on the **provided sample files** so results are predictable.
- Work stays within the **Microsoft 365 tenant boundary**; your drafts, OneDrive files, and custom
  skills live under **your own user account**.

## When Cowork uses the web

- **Deep Research:** open the citations and check that each one supports its claim. Prefer official
  sources (government, regulator, plan documents) for anything policy- or law-related.
- **Browser use:** Cowork works in **your** Edge with **your** sign-ins, so treat it like handing a
  colleague your keyboard. Give it **read-only** instructions unless you mean otherwise ("only read
  the page; don't fill in or submit anything"), approve each consequential step, and enter passwords
  or MFA codes yourself when it hands the browser back. It can't bypass your organization's site
  policies, and every browser task is recorded in the audit log.
- **Web content isn't legal advice.** Use it to check a policy, then confirm with legal or payroll
  before acting on it.

## Handling sensitive HR scenarios

| Scenario | Practice |
| --- | --- |
| Employee performance or disciplinary content | Keep it out of shared skills; review drafts privately before use |
| Compensation / offer details | Treat as confidential; never use real figures in training |
| Benefits / medical questions | Provide general guidance; direct employees to official plan documents |
| Anything you're unsure about | Escalate to a person; don't let an AI draft be the final word |

## Model & subprocessor awareness

- Cowork may use **Anthropic models as a subprocessor** in addition to other models. If your
  organization has policies about which models or subprocessors are permitted, follow them and set
  the **model picker** accordingly.
- Image generation uses the **ChatGPT Images 2.0** model and follows the same content policies as
  the rest of Cowork.

## Limitations to set expectations

- Cowork can make mistakes or miss nuance — **human review is required** for HR decisions.
- Custom skills and browser tasks aren't supported on **mobile**; browser tasks also need **Microsoft
  Edge** and an admin-enabled **Cowork Browsing** setting.
- Some capabilities (e.g., the **App** skill) require **Frontier** enrollment.
- Availability of specific models, plugins, and features depends on **tenant configuration**.

## Quick pre-send checklist

- [ ] Is the content accurate and grounded in a source I trust?
- [ ] Would I be comfortable if this were forwarded internally?
- [ ] Does it avoid real PII that shouldn't be there?
- [ ] Did I confirm any policy claims against the official document?
- [ ] Have I reviewed it in my own voice before sending?
