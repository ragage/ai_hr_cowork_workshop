# 10 · Navigate Websites with Cowork's Browser

> Reference sheet for the "Getting Things Done with Copilot Cowork for HR Tasks" workshop.
> Backs **Exercise 2**. Covers what browser use is, how to turn it on, and what to do when it doesn't
> start.

## What it is (and why you don't see a "browser" skill)

Cowork can **operate a website for you**, much like a person, or a test-automation tool such as
Playwright, would: it opens the page, types in search boxes, clicks links and menus, reads the
result, and moves on to the next site. It works in a **hidden tab in your own Microsoft Edge**, so
it uses your existing sign-ins and your organization's policies, with **no new access**.

**There's no browser skill to select, and no skill chip.** Browser use is a built-in capability.
Ask for something that needs a website (*"Go to dol.gov and use the site search to find…"*) and
Cowork decides to open the browser. You'll see **progress chips** such as *Opening dol.gov* and a
**Switch to tab** option to watch it work.

| | Deep Research (Exercise 1) | Browser use (Exercise 2) |
| --- | --- | --- |
| What it does | Searches and **reads** many sources, then writes a **cited** synthesis | **Operates** specific websites step by step: search, click, navigate, read |
| Where it runs | In the Cowork service | In a hidden tab in **your** Edge, on your device |
| Good for | "What does the evidence say about…?" | "Go to this site, find this page, check this rule, bring back the link" |
| Sign-ins | Doesn't sign in to websites | Uses the sites you're already signed in to (it hands sign-in back to you) |

## How to turn it on

Browser use is **off by default**. All of the following must be true.

### For the admin (once per tenant)

1. In the **Microsoft 365 admin center**, go to **Copilot → Settings → View all → Cowork settings**.
2. Under **Allow browser access**, select **Allow Cowork to use the Microsoft Edge browser to perform
   tasks on behalf of users**, and scope it to the right users or security group (for the workshop,
   the attendee group).
3. If devices are managed, check the Edge policy **CopilotCoworkToolActionsEnabled** ("Allow Cowork
   to take actions on your behalf"). **Disabled** blocks browser use; **Enabled** forces it on; not
   configured lets each user choose in Edge settings.
4. Make sure web filtering doesn't block the sites the exercise uses (**dol.gov**, **lni.wa.gov**).

### For each user (on the day)

1. Use **Microsoft Edge 152 or later** (released the week of August 24, 2026). Edge doesn't need to
   be your default browser.
2. Open Cowork **in Edge, on the web**, at https://copilot.cloud.microsoft. Browser use doesn't run
   from the Copilot desktop app, from mobile, or when Cowork is open in Chrome.
3. Be signed in to **Edge** with the **same work account** you use for Cowork. In the workshop, that
   means an Edge profile for your **work account**. InPrivate and guest windows don't work.
4. In Edge **Settings**, search for **Cowork** and make sure **Allow Cowork to take actions on your
   behalf** is on (it's greyed out if your organization manages it).
5. The first time Cowork needs the browser, a **consent notice** appears in the conversation. Select
   **I understand**.

## What you'll see

- **Progress chips** for each step (opening a site, searching, reading a page).
- **Switch to tab** to watch the hidden Edge tab, and switch back to the conversation.
- **Questions in the chat** when Cowork needs information it can't find on the page.
- **Approval cards** before consequential actions (for example, submitting a form). Select
  **Approve** for that one action, or **Reject**.
- **Hand-back** for sensitive steps: a password, an MFA code, a CAPTCHA, or a locked account. Cowork
  pauses and shows you the tab; it continues after you finish.
- If the tab closes or your device sleeps, the task **pauses**. Reopen the conversation and type
  *continue*.

## Troubleshooting

| What you see | Likely cause | Fix |
| --- | --- | --- |
| "Browser tasks run in Microsoft Edge" and a **Get Microsoft Edge** link | Cowork is open in Chrome or another browser | Open https://copilot.cloud.microsoft in Edge |
| Cowork answers from memory or with Deep Research and never opens a site | Browser use isn't allowed for your account, or the Edge setting is off | Admin: check **Allow browser access** and the Edge policy. User: Edge **Settings → Cowork** |
| Nothing happens, or it can't use your sign-ins | Edge profile isn't your work account, or you're InPrivate | Switch to (or add) an Edge profile signed in with your work account |
| Browser option unavailable in the desktop app | Desktop app isn't supported | Use Cowork on the web in Edge |
| Old Edge | Version below 152 | Edge menu → **Help and feedback → About Microsoft Edge** to update |
| "Your organization's policy doesn't allow this action" | DLP, web filtering, or Conditional Access | Expected: Cowork has your access, never more. Do that step by hand |
| Consent notice keeps reappearing | **I understand** wasn't selected | Select it; the choice is saved in Edge on that device |

## Good prompts for browser use

- Say **which site** and **how to navigate**: *"use the site's search box"*, *"use the menu"*,
  *"follow the links; don't guess the URL"*.
- Ask it to **report each page**: *"tell me which page you're on at each step"*, and to **bring back
  links**.
- Set **limits**: *"only read; don't sign in, fill in, or submit anything except a site search box"*.
- For anything that submits data (a form, a purchase, a request), ask it to **show you each step
  before it clicks**, and approve each action yourself.

## Responsible use

- Treat browser use like handing a colleague your keyboard: approve **one action at a time**, and
  enter passwords and MFA codes yourself.
- Cowork can't bypass sign-in, Conditional Access, DLP, or a site's terms of service, and every
  browser task is recorded in the **audit log**.
- Web pages aren't legal advice. Use them to check a policy, then confirm with legal or payroll.

## Learn more

- [Use the local browser with Copilot Cowork](https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-local-browser)
- [Manage Copilot Cowork: browser use](https://learn.microsoft.com/microsoft-365/copilot/cowork/cowork-admin-governance#browser-use)
- [Edge policy: CopilotCoworkToolActionsEnabled](https://learn.microsoft.com/deployedge/microsoft-edge-policies/copilotcoworktoolactionsenabled)
- [Responsible AI FAQ: how Cowork uses the local browser](https://learn.microsoft.com/microsoft-365/copilot/responsible-ai/cowork-responsible-ai-faq#how-does-cowork-use-the-local-browser-responsibly)
