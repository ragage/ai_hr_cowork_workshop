# Pre-Workshop Readiness Checklist

> In this workshop **the ~25 attendees share one common tenant**, each signing in with **their own
> user account**, while the **facilitator demos from their own separate tenant**. That makes
> readiness mostly the **host's** job — provision the attendee accounts and stage the data ahead of
> time, and the day runs smoothly.

## Preparation timeline

| When | Owner | Do this |
| --- | --- | --- |
| **T − 3 weeks** | Host / admin | Confirm Microsoft 365 Copilot licenses and **usage-based billing** for the attendee tenant, create a **Cowork spending policy** for the attendee group, and turn on **Cowork Browsing** for that group. Estimate cost and set spend guardrails (see [Cost planning](#cost-planning)). Book the room and Wi-Fi. |
| **T − 2 weeks** | Host / admin | Provision **~25 accounts + 2–3 spares**, assign managers, create the 2–3 **seed sender** accounts ([seed-content.md](seed-content.md)). Confirm the facilitator's own tenant is Cowork-ready. |
| **T − 1 week** | Facilitator | **Full dry run** of all 8 exercises on a test attendee account, checking against the [answer key](facilitator-answer-key.md). Stage `zava-sample-knowledge.zip` in the shared Teams/SharePoint folder. Send attendees a joining note (bring a laptop, not a phone). |
| **T − 1 day** | Host / admin | Load the **seed emails, meetings, and Teams chat** into every account (1–2 days ahead, so the Exercise 1 command center sees them as this week). Sign in to 3 random accounts in **Edge** and run the smoke test **and** the Exercise 3 browser prompt (accept the consent notice). Print credential handouts and the [quick-reference card](quick-reference-card.docx). |
| **Day of, T − 45 min** | Facilitator + proctors | Test the projector, Wi-Fi, and demo tenant. Open the deck, the answer key, and a ready Cowork session. Brief proctors on the [troubleshooting triage](facilitator-guide.md#troubleshooting-triage-hand-to-proctors). |
| **Day after** | Host | **Pause or delete** Exercise 1 and 7 schedules (or have attendees do it), send the [after-the-workshop pack](after-the-workshop.md) and survey, and review usage and spend. |

## Cost planning

Cowork is **usage-billed**, so 25 people running Deep Research, dashboards, and automations at once
adds up. Before the session:

- **Set up billing:** [aka.ms/CopilotCredits/Setup](https://aka.ms/CopilotCredits/Setup)
- **Estimate the cost:** the [Customer cost estimator](https://aka.ms/CustomerCoworkEstimator) and the
  Copilot Credit Planning Model ([aka.ms/CopilotCreditPlanningMod](https://aka.ms/CopilotCreditPlanningMod)).
  Estimate for ~25 users × 8 exercises, plus spares, the facilitator's dry run, and the Exercise 1 and
  7 schedules that keep running until paused.
- **Set guardrails:** set a per-user credit limit and alerts on the workshop spending policy, and plan to
  **pause every schedule the day after**. A low limit doesn't block access: people can work until they
  reach it. To remove someone's access, take them out of the policy's scope instead.
- **After the event:** remove the workshop group from the spending policy (or delete the policy) if the
  accounts shouldn't keep Cowork access.
- **Reduce cost:** leave the model picker on **Let Cowork decide** and reasoning effort on the default
  unless an exercise calls for more.

## Plan B — if Cowork is down for the whole room

1. **Don't troubleshoot for more than 10 minutes.** Announce the switch.
2. **Demo from the facilitator tenant**, projected. Run each exercise live while the room follows the
   workbook, and use the [answer key](facilitator-answer-key.md) as the "expected result" handout.
3. **Keep the non-Cowork pieces hands-on:** Exercise 8 (Agent Builder) and the Copilot Chat
   comparison work without Cowork, if Microsoft 365 Copilot is up.
4. **Turn practice into judgment:** have attendees critique the demo outputs with the answer key and
   the [responsible-use checklist](reference/06-responsible-use.md#quick-pre-send-checklist).
5. **Reschedule a 90-minute hands-on follow-up** for Exercises 1, 3, 4, and 7, with the same
   accounts and seed data.

## For the host / tenant admin (do this before the workshop)

- [ ] Provision **~25 user accounts** in the **shared attendee tenant** (plus **2–3 spares**).
- [ ] Assign a **Microsoft 365 Copilot** license to each account.
- [ ] Put the attendee accounts (and spares) in a **security group**, e.g. *Zava Workshop Attendees*.
- [ ] **Usage-based billing** set up, with a **spending policy that selects Cowork** and is scoped to
      that group. The spending policy is what **grants access** to Cowork (the older *Agents → Cowork*
      setting no longer controls access). Add an estimate and guardrails (see [Cost planning](#cost-planning)).
- [ ] **Cowork Browsing** (for the Exercise 3 browser task): in the Microsoft 365 admin center, **Copilot →
      Settings → View all → Cowork settings → Allow browser access**, and allow it for the attendee
      group. It's **off by default**. Also check that web filtering doesn't block **dol.gov** or
      **lni.wa.gov**, and that the Edge policy **CopilotCoworkToolActionsEnabled** isn't set to
      Disabled on managed laptops. Details: [reference/10-cowork-browser.md](reference/10-cowork-browser.md).
- [ ] Attendee laptops have **Microsoft Edge 152 or later**. Each attendee will sign in to an **Edge
      profile** with their workshop account (InPrivate and guest windows can't run browser tasks) and
      check that **Allow Cowork to take actions on your behalf** is on in Edge **Settings**.
- [ ] Confirm the **facilitator's own (demo) tenant** is Copilot- and Cowork-ready for live demos.
- [ ] *(Optional)* For the **HR plugins spotlight**, have a plugin installed in the **facilitator's
      tenant** (e.g., an approved HR or Microsoft plugin) so you can show **Customize → Plugins**
      live. Otherwise the deck's screenshot is enough. Don't add plugins to the attendee tenant.
- [ ] **Stage the sample data:** upload **zava-sample-knowledge.zip** (the six Word and Excel sample files)
      to a shared location every attendee account can reach (a **Teams channel** or **SharePoint
      library**), so attendees can copy them into their own OneDrive.
- [ ] **Seed mail, calendar & chat for Exercise 1 (Executive Command Center):** new accounts are
      empty. Load the **7 emails**, **3 meetings** (including the deliberate Thursday conflict), and
      the short **Teams chat** from [seed-content.md](seed-content.md) into each attendee account
      **1–2 days before the session**, so the command center has signals to surface.
- [ ] **After class:** remind attendees (or clean up centrally) to **pause/delete the schedules**
      created in Exercises 1 and 7 so they stop consuming usage.
- [ ] Prepare a **credential handout** (account + password / sign-in instructions) for each seat.
- [ ] *(Optional)* **Frontier** enrollment — only if you want to demo the built-in **App** skill;
      not required for the core exercises.
- [ ] Confirm any **model/subprocessor policy** (e.g., use of Anthropic models as a subprocessor) so
      you can tell attendees what's allowed in the model picker.

## For attendees (during setup, first 20 minutes)

- [ ] I signed in with the **workshop account** I was given at **https://copilot.cloud.microsoft**
      in **Microsoft Edge**, in an Edge profile signed in with the workshop account.
- [ ] I can see the **Cowork** toggle at the top (next to **Chat**).
- [ ] I ran a smoke-test prompt in Cowork and got a response (e.g., *"Give me a one-sentence hello."*).
- [ ] I copied the **sample-knowledge** files from the shared location into my **own OneDrive**
      folder **Documents/ai_hr_cowork_workshop** (I created it in OneDrive → My files → Documents).
- [ ] I set my **custom instructions**: **Customize → Preferences → Customize instructions for Cowork**
      (workbook Setup step D).
- [ ] I'm on a **laptop/desktop** (custom skills aren't supported on mobile).

## Shared-tenant etiquette

- Your **OneDrive, drafts, and skills** are tied to **your account** — they're your own.
- Keep any **custom skill you build "Only you"** (or add your initials to the name) so you don't
  create 25 identically named skills across the shared tenant.
- Use **only the fictional sample data** in exercises — never real employee PII, and don't actually
  send emails to real people (save as drafts).

## If something isn't ready

- **Account/license/Cowork issue** → the host swaps in a **spare account**; meanwhile the attendee
  follows the **facilitator demo** (fallback follow-along), checking results against the
  [facilitator answer key](facilitator-answer-key.md), so they still learn the flow.
- **Can't find the sample files** → point to the staged Teams/SharePoint copy; a proctor helps copy
  them to OneDrive.
- Keep a **parking lot** for any tenant issue so the group stays on schedule.
- **Whole room blocked** (Cowork or tenant down)? Switch to [Plan B](#plan-b--if-cowork-is-down-for-the-whole-room).

## Quick reference: what each prerequisite unlocks

| Prerequisite | Needed for |
| --- | --- |
| Licensed account in the shared tenant | All of Cowork |
| Cowork spending policy (usage-based billing) | Access to Cowork, and running tasks (Cowork is usage-billed) |
| Cowork Browsing + Edge 152+ signed in with the workshop account | The Exercise 3 browser task |
| Staged sample files + OneDrive | Grounding exercises; saving custom skills |
| Laptop/desktop | Building custom skills (not available on mobile) |
| Frontier (optional) | The built-in **App** skill only |
