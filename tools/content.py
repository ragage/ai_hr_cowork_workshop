"""Scenario-card content for the instructor deck (mirrors participant-workbook.md).

Prompt text marks its elements for color coding: {g}Goal{/g}, {s}Source{/s}, {e}Expectations{/e},
{c}Constraints{/c} (the workbook uses <span class=...> for the same thing). Exercise 1 is left unmarked.
"""

GUIDE_CARD = dict(
    pill="Guide", title="How to read an exercise card", function="Every exercise", tag_label="Format",
    goal="What you\u2019ll accomplish \u2014 the business outcome in one sentence.",
    output="The finished artifact Cowork hands back: a document, dashboard, email, schedule, or agent.",
    why="Why this is a Cowork job \u2014 the multi-step, cross-app work it orchestrates, and where it pauses "
        "for your approval.",
    prompt=[
        "This panel holds the exact prompt you\u2019ll paste into Cowork.",
        "",
        "Before you run it:",
        "- Replace any [placeholders], such as [Priority Folder] or [time]",
        "- Keep \u201csave as a draft\u201d wording \u2014 never send to real people in class",
        "- Watch the side panel: skill chips, files, and schedules appear as Cowork works",
        "",
        "After it runs:",
        "- Review every output as a draft",
        "- Approve or decline each checkpoint deliberately",
        "- Use the hands-on slide that follows for steps, the checkpoint, and a stretch",
    ],
    prompt_size=13,
    workflow=[("Gather", "Cowork pulls context through Work IQ"), ("Analyze", "It reasons over what it found"),
              ("Build", "It creates the artifact"), ("Deliver", "It pauses for approval, then acts")],
    sources=["m365", "web", "onedrive"],
    notes_card="HOW TO READ A CARD. Every exercise is introduced with the same scenario "
               "format. Walk it top-left to bottom-right: Goal, Output, Why Cowork?, Prompt, Workflow, Data "
               "sources; the Function tag names the business area. Each card is followed by a hands-on slide "
               "with numbered steps, what to watch for, a checkpoint, and a stretch.",
)


EXEC_PROMPT = [
    "Build an interactive HTML Executive Command Center that shows what requires my attention today and this "
    "week.",
    "",
    "Use my calendar, recent emails, Teams conversations, meeting transcripts, and priority documents from "
    "[Priority Folder]. Focus on decisions, commitments, risks, and workstreams where my involvement could "
    "change the outcome.",
    "",
    "At the top, show:",
    "- One or two urgent items requiring action",
    "- Today\u2019s most important meeting or priority",
    "- My busiest day this week",
    "- Remaining working days this week",
    "",
    "Organize the command center into three views:",
    "- Meetings: Key meetings, preparation needed, conflicts, and follow-ups",
    "- Priorities: Active commitments, approaching deadlines, blockers, and decisions waiting on me",
    "- Org pulse: Workstreams receiving significant attention, areas with limited recent activity, and "
    "important commitments that may have gone quiet",
    "",
    "For each recommended action, label it:",
    "- Lean in; OR, Delegate; OR, Re-engage; OR, Protect time",
    "",
    "Explain the signal behind the recommendation and give me one clear next action. Keep recommendations "
    "focused on workstreams, decisions, and commitments rather than evaluating individual people. Make the "
    "dashboard executive-ready and easy to scan, with expandable sections, traffic-light indicators, and links "
    "to the supporting emails, meetings, chats, and files. The most important content should answer: What "
    "needs my attention, and what should I do differently today?",
    "",
    "Save this as a skill named [Executive Command Center] and schedule it to run every weekday at [time], "
    "using the latest available context.",
]

EXERCISES = [
    dict(
        num=1, pill="Ex 01", title="Executive Command Center", short="Executive Command Center", function="Executive",
        minutes="25 min",
        goal="Turn your calendar, communications, and priority work into a daily executive view of decisions, "
             "risks, and actions requiring attention.",
        output="An interactive executive command center covering meetings, priorities, and org pulse, with labeled "
               "recommendations and links to supporting context.",
        why="What needs your attention is scattered across calendar, email, chats, and documents. Cowork combines: "
            "calendar and priority documents, emails, chats and transcripts, signal detection across workstreams, "
            "and an interactive daily dashboard, into one recurring workflow.",
        prompt=EXEC_PROMPT,
        workflow=[("Work IQ", "Gather calendar, emails, chats, documents"),
                  ("Analyze", "Surface urgent items, blockers, quiet signals"),
                  ("Build", "Interactive HTML command center"), ("Schedule", "Daily run every weekday morning")],
        sources=["m365"],
        discuss='Which recommendations would you trust? What would an **HR-leader** version track — open reqs, ER cases, policy deadlines?',
        steps=["Fill **[Priority Folder]** (your OneDrive folder with the Zava files) and **[time]** (e.g., 8:00 AM).",
               "**New task** \u2192 paste the Executive Command Center prompt.",
               "**Side panel \u2192 Output folder \u2192 Preview** the HTML dashboard (see the next slide).",
               "Check the top summary, the three views, the action labels, and the links.",
               "**Approve** the skill save and weekday schedule \u2014 confirm in Customize and Automations."],
        watch=["Work IQ gathering calendar, mail, chats, and files",
               "Labels: Lean in \u00b7 Delegate \u00b7 Re-engage \u00b7 Protect time",
               "Focus on workstreams \u2014 not on evaluating people",
               "Light data in new accounts is expected"],
        checkpoint="An HTML command center opened from the Output folder and found in OneDrive \u2192 Cowork, a "
                   "saved skill, and a weekday schedule. Pause it after class.",
        stretch="Make an HR Leader variant with a view for open requisitions and HR ticket trends.",
        notes_card="EXERCISE 1 CARD (0:40-1:05, 25 min). SAY: 'Watch one prompt gather signals, build a dashboard, save itself as a skill, and schedule itself.' APPROVALS FIRST: this is the first exercise where Cowork asks permission (saving the skill, creating the schedule). Point back to the approvals slide: one at a time, no Approve All. It previews Ex 4 (skills) and Ex 7 (Automations). Read the guardrail in the prompt aloud: workstreams, not people.",
        notes_hands="EXERCISE 1 HANDS-ON. DO: show how to fill [Priority Folder] (e.g., Documents/ai_hr_cowork_workshop) and [time] (e.g., 8:00 AM), then start your demo. WATCH FOR: Work IQ gathering; the HTML file in the Output folder; the Thursday conflict and T-2008 from the seed data. Light results on fresh accounts are expected; show your richer demo. SLOW DOWN at step 3: the next slide walks the Output folder. CLEANUP: skill stays 'Only you'; pause or delete the weekday schedule after class. NEXT: Output folder slide, then Deep Research.",
    ),
    dict(
        num=2, pill="Ex 02", title="Research the Web with Deep Research", short="Deep Research",
        function="HR \u00b7 Talent", minutes="20 min",
        goal="Get an evidence-based view of structured behavioral interviewing and turn it into questions for a "
             "real open role.",
        output="A cited one-page briefing, five tailored questions for Zava\u2019s HR Coordinator role, and an "
               "interviewer scorecard in Word and Excel with the scoring scales filled in.",
        why="Good research means reading and citing many sources. Deep Research does that across the web, applies "
            "the findings to your job description, and a follow-up turns them into ready-to-use documents.",
        prompt=["{g}Use Deep Research to summarize current best practices for structured behavioral interviews{/g} {s}from "
                "multiple reputable sources{/s}. {e}Produce a 1-page briefing with the key practices and cite your sources.{/e}",
                "",
                "## Then:",
                "{g}Now compare these best practices to our HR Coordinator interview needs{/g} {s}in "
                "job-description-sample.docx{/s}, {e}and suggest 5 interview questions.{/e}",
                "",
                "## Follow-up:",
                "{g}Turn this into an interviewer scorecard{/g} {e}in Word AND Excel with the scoring scales filled in.{/e}"],
        prompt_size=12.5,
        workflow=[("Deep Research", "Search and read multiple web sources"), ("Synthesize", "Key practices with citations"),
                  ("Ground", "Compare to job-description-sample.docx"), ("Draft", "Briefing + 5 tailored questions"),
                  ("Build", "Scorecard in Word + Excel")],
        sources=["web", "onedrive"],
        discuss='When is web research better than searching your own organization\u2019s content \u2014 and when is it riskier?',
        steps=["**New task** \u2192 run the Deep Research prompt.",
               "**Watch** it search and read multiple sources, citing each. Open two citations.",
               "**Ground it:** attach job-description-sample.docx and compare the findings to it.",
               "**Ask for** five tailored interview questions.",
               "**Follow-up:** scorecard in **Word AND Excel**, scales filled in; open both from the **Output folder**."],
        watch=["The **Deep Research** skill chip and progress", "Citations you can open and check",
               "**Word** and **Excel** chips for the scorecard", "Scales filled in \u2014 no \u201cTBD\u201d anchors"],
        checkpoint="A cited briefing, five tailored questions, and a Word + Excel interviewer scorecard with every "
                   "scale filled in.",
        stretch="Benchmark PTO / annual-leave norms for mid-size tech firms against the Zava handbook.",
        notes_card="EXERCISE 2 CARD (1:05-1:25, 20 min). SAY: 'Deep Research reads many web sources and cites them, then we make it useful by grounding it in our own job description and turning it into documents.' Point out the three stages on the card: research, ground, build (Word + Excel). Next exercise shows the OTHER way Cowork uses the web: driving a browser.",
        notes_hands="EXERCISE 2 HANDS-ON. DO: start Deep Research on your screen first (it takes a few minutes), then the room starts theirs. Use the wait: 'When is web research better than our own content, and when is it riskier?' WATCH FOR: the Deep Research chip; citations that open; Word and Excel chips for the scorecard. IF STUCK: blank scales -> reply 'Fill in the 1, 3, and 5 anchors for every competency.' Only one file -> 'Also create the Excel version.' TIME CHECK: at 1:20, demo the scorecard follow-up on your screen if most are still researching. NEXT: break, then the browser.",
    ),
    dict(
        num=3, pill="Ex 03", title="Navigate Websites with Cowork\u2019s Browser", short="Browser",
        function="HR \u00b7 Compliance", minutes="25 min",
        goal="Have Cowork drive a real web browser for you \u2014 search a site, click through, move to a second "
             "site \u2014 and bring back a sourced comparison.",
        output="An overtime comparison (U.S. DOL vs. Washington L&I vs. Zava handbook) with a link to every page "
               "visited, and a one-page Word brief for payroll about T-2008.",
        why="Checking policy against official sites means searching, clicking, and copying. Cowork does the clicks in a "
            "hidden tab in your own Edge, with your sign-ins and policies, and asks before anything consequential.",
        prompt=["## Task 3a \u2014 Attach the handbook, then:",
                "{e}Use my browser to do this step by step, and tell me which page you\u2019re on at each step:{/e}",
                "1. {s}Go to https://www.dol.gov and use the site\u2019s search box to find the Wage and Hour Division\u2019s "
                "overtime pay fact sheet (Fact Sheet #23).{/s} {g}Open it and note the overtime rules and when overtime must "
                "be paid.{/g}",
                "2. {s}Go to https://lni.wa.gov and use the site\u2019s menu or search to find Washington State\u2019s "
                "overtime page.{/s} {g}Open it and note anything Washington adds to the federal rules.{/g}",
                "3. {g}Compare both with the overtime rule{/g} {s}in employee-handbook-excerpt.docx{/s}. {e}Give me a table with the "
                "columns Rule, Federal (DOL), Washington (L&I), and Zava handbook, plus a link to every page you used.{/e}",
                "{c}Only read: don\u2019t sign in, and don\u2019t fill in or submit any form except a site search box.{/c}",
                "",
                "## Task 3b \u2014 Follow-up",
                "{g}Turn this into a one-page Word brief for our payroll team about ticket T-2008{/g}: {e}what the rules say, "
                "what our handbook says, and the recommended next step.{/e} {c}Don\u2019t send it.{/c}"],
        prompt_size=12,
        workflow=[("Navigate", "dol.gov: site search \u2192 Fact Sheet #23"), ("Navigate", "lni.wa.gov: menu \u2192 overtime page"),
                  ("Ground", "Compare with the Zava handbook"), ("Build", "Table with links + Word brief")],
        sources=["web", "onedrive"],
        discuss='When would you use browser use instead of Deep Research? What would you never let it do unwatched?',
        steps=["**Check:** Cowork open **in Edge**; Edge profile = **workshop account**; Edge setting **Allow Cowork to take actions** on.",
               "**New task:** attach the handbook; paste the two-site prompt.",
               "**Consent:** select **I understand** at the browser notice.",
               "**Switch to tab** to watch it search dol.gov and click through; open two links yourself.",
               "**Follow-up:** the Word brief for payroll; open it from the **Output folder**."],
        watch=["No \u201cbrowser\u201d skill chip \u2014 watch the **progress chips**",
               "It types in the **site search** and clicks menus (not guessed URLs)",
               "Sign-in or CAPTCHA? It hands back \u2014 don\u2019t enter anything",
               "Nothing submitted beyond a search box"],
        checkpoint="Two sites navigated by search and menus, a comparison table linking the DOL fact sheet and the "
                   "Washington L&I overtime page, and a Word brief about T-2008.",
        stretch="Step through the DOL FLSA Overtime Security Advisor, with Cowork telling you each answer before it clicks.",
        notes_card="EXERCISE 3 CARD (1:35-2:00, 25 min). SAY: 'This is Cowork driving a real browser, like a person or a test tool such as Playwright: it types in a site's search box, clicks links and menus, and moves to another site. There's no browser skill to pick and no skill chip; ask for something that needs a website and Cowork opens a hidden tab in your own Edge, with your sign-ins and your company's policies.' Contrast with Deep Research (reads and cites) from Ex 2.",
        notes_hands="EXERCISE 3 HANDS-ON. DO: demo first. Show the consent notice (I understand), the progress chips, and Switch to tab so the room sees Edge typing in the DOL search box and clicking through to Fact Sheet #23, then lni.wa.gov. WATCH FOR: a table showing Zava's 1.5x over 40 hours matches federal and Washington rules; DOL adds the regular-payday rule; Washington adds no waiver and no daily overtime; links to both pages. IF STUCK: 'Browser tasks run in Microsoft Edge' -> wrong browser; no browser at all -> Edge profile isn't the workshop account, InPrivate, the Edge setting is off, or the admin hasn't allowed browser access (reference/10-cowork-browser.md). They follow your demo. TIME CHECK: at 1:55 skip 3b and demo it. NEXT: 'You've used built-in skills and the browser. Now build your own skill.'",
    ),
    dict(
        num=4, pill="Ex 04", title="Build a Custom Skill: HR Policy Answer", short="Custom Skill",
        function="HR \u00b7 Policy", minutes="30 min",
        goal="Teach Cowork to answer policy and benefits questions the same clear, sourced way \u2014 every time.",
        output="A saved custom skill, \u201cHR Policy Answer,\u201d with a quality score, that triggers on policy "
               "questions and answers Answer \u2192 Details \u2192 Source \u2192 \u201cconfirm with HR.\u201d",
        why="Repeating the same instructions in every prompt is error-prone. A custom skill packages tone, format, "
            "sources, and guardrails once; Cowork auto-evaluates it (0\u2013100) and applies it when it\u2019s needed.",
        prompt=["In Customize \u2192 Skills \u2192 Add \u2192 Create new, give Cowork these details:",
                "",
                "- Name: HR Policy Answer",
                "- Category: Human Resources",
                "- Description: Answers employee policy and benefits questions in a consistent, sourced format, "
                "grounded in our handbook and benefits documents.",
                "",
                "## Instructions:",
                "{g}Use this skill when someone asks about company HR policy or benefits (PTO, remote/hybrid work, "
                "benefits enrollment, overtime, code of conduct, learning budget).{/g} {s}Ground answers in "
                "employee-handbook-excerpt.docx and benefits-summary.docx in my OneDrive folder Documents/ai_hr_cowork_workshop{/s}; {c}if "
                "the answer isn\u2019t in them, say so instead of guessing.{/c} {e}Answer in this format: a direct "
                "plain-language answer, then a short Details "
                "section, then a Source line naming the document, then the note \u201cPolicies can change \u2014 "
                "please confirm with HR.\u201d Keep a warm, professional tone.{/e} {c}Do not handle individual pay, "
                "performance, disciplinary, legal, or medical questions \u2014 politely redirect those. Produce a "
                "draft for HR to review; never send automatically.{/c}"],
        prompt_size=11,
        workflow=[("Customize", "Skills \u2192 Add \u2192 Create new"), ("Define", "Name, description, category, instructions"),
                  ("Evaluate", "Auto-score on four dimensions"), ("Test", "In-scope triggers; out-of-scope declines")],
        sources=["onedrive"],
        discuss='Which recurring HR question would you turn into a skill next, and what must it **never** answer?',
        steps=["**Customize \u2192 Skills \u2192 Add \u2192 Create new.**",
               "Name **HR Policy Answer**, category **Human Resources**, and paste the instructions.",
               "**Confirm** \u2014 Cowork saves it to your OneDrive skills folder.",
               "**Read the score** (aim for Good 70+ or Excellent 85+); tighten trigger or scope if needed.",
               "**Test:** a policy question should trigger it; \u201cWhat\u2019s my colleague\u2019s salary?\u201d should be declined."],
        watch=["Scores: trigger clarity, instruction specificity, scope boundaries, robustness",
               "Answer \u2192 Details \u2192 Source \u2192 \u201cconfirm with HR\u201d",
               "Keep the skill **\u201cOnly you\u201d** in the shared tenant"],
        checkpoint="Your skill scores Good or better, triggers on its own, follows the format, and declines "
                   "out-of-scope questions.",
        stretch="Add a rule to link to the HR portal whenever a change requires a form.",
        notes_card="EXERCISE 4 CARD (2:00-2:30, 30 min) - CENTERPIECE. SAY: 'In Ex 1 a skill was saved for you from a prompt. Now you build one on purpose and Cowork grades it.' Explain why a skill beats re-typing instructions: same format, sources, and guardrails every time. Scoring bands: Excellent 85+, Good 70-84, Needs work 50-69, Poor <50.",
        notes_hands="EXERCISE 4 HANDS-ON. DO: build it live from Customize -> Skills -> Add -> Create new; paste the instructions; read the evaluation ALOUD and name the four dimensions (trigger clarity, instruction specificity, scope boundaries, robustness). Then test both questions. WATCH FOR: the skill triggering WITHOUT being named; Answer -> Details -> Source -> confirm-with-HR; the salary question declined. IF STUCK: 'Needs work' -> tighten trigger wording and the out-of-scope list; wrong facts -> check the two file names in the instructions match their OneDrive. Keep skills 'Only you'. Answer key: facilitator-answer-key.md and skills/hr-policy-answer/SKILL.md. NEXT: 'This skill helps YOU. In Ex 8 we build an agent that helps OTHERS.'",
    ),
    dict(
        num=5, pill="Ex 05", title="Recruiting + Reporting", short="Recruiting + Reporting",
        function="HR \u00b7 Talent & Ops", minutes="15 min",
        goal="Attract the right candidates for an open role and get on top of the HR service queue in minutes.",
        output="An inclusive HR Coordinator job posting in Word, with off-putting wording flagged, and a ticket "
               "summary highlighting today\u2019s high-priority open items.",
        why="One task reads a job description and writes a structured document; the other analyzes a spreadsheet and reports "
            "on it. Cowork picks the right skills (Word, Excel) for each and grounds both in your files.",
        prompt=["## Task 5a \u2014 Inclusive job posting",
                "{s}Using job-description-sample.docx{/s}, {g}write an inclusive, engaging job posting for the HR Coordinator "
                "role for our careers page.{/g} {e}Keep it under 350 words, with short What you\u2019ll do, What you\u2019ll "
                "bring, and What we offer sections, and mention the hybrid schedule. Then add a separate table that "
                "flags any wording in the original description that could discourage qualified applicants, with a "
                "suggested alternative for each. Save it as a Word doc.{/e} {c}Don\u2019t add pay figures, perks, or "
                "requirements that aren\u2019t in the description.{/c}",
                "",
                "## Task 5b \u2014 Ticket summary",
                "{s}Using hr-tickets-sample.xlsx{/s}, {g}summarize open vs. closed tickets by category and priority, and list "
                "the high-priority open items I should follow up on today.{/g} {e}Put it in a short report.{/e}"],
        prompt_size=12.5,
        workflow=[("Ground", "Read the job description and ticket spreadsheet"), ("Draft", "Inclusive job posting (Word)"),
                  ("Analyze", "Open vs. closed by category & priority"), ("Report", "Today\u2019s high-priority follow-ups")],
        sources=["onedrive"],
        discuss='Which recruiting or reporting task eats most of your week today?',
        steps=["**Task 5a:** attach job-description-sample.docx; write the inclusive job posting and save it as Word.",
               "**Check** the wording-review table: do you agree with every flag?",
               "**Task 5b:** attach hr-tickets-sample.xlsx; summarize open vs. closed by category and priority.",
               "**List** today\u2019s high-priority open items to follow up."],
        watch=["**Word** for the posting; **Excel** for the analysis",
               "The High/Open overtime ticket (T-2008)", "You\u2019ll automate this report in Exercise 7"],
        checkpoint="A Word job posting with a wording-review table, and a ticket summary: 6 open / 14 closed, with "
                   "T-2008 as the only high-priority open ticket.",
        stretch="Summarize employee-roster-sample.xlsx: headcount by department, remote vs. on-site, average PTO used.",
        notes_card="EXERCISE 5 CARD (2:30-2:45, 15 min). SAY: 'Two quick wins. In Ex 2 we prepared to interview for the HR Coordinator role; now we write the posting that attracts the right candidates. Then we get on top of the ticket queue.' Point out that Cowork picks Word for writing and Excel for analysis on its own.",
        notes_hands='EXERCISE 5 HANDS-ON. DO: run 5a and 5b back to back; attendees can start 5b while 5a is still working. WATCH FOR: 5a -> a posting under 350 words with the hybrid schedule, plus a wording-review table (e.g., degree requirement, years of experience framed as must-haves); discuss whether every flag is fair. 5b -> 6 open / 14 closed, T-2008 as the ONLY high-priority open ticket. TRAP: T-2003 and T-2013 are High but Closed; listing them means Status was ignored. IF STUCK: wrong counts -> ask Cowork to show the table it counted from. NEXT: break, then they automate this report in Ex 7.',
    ),
    dict(
        num=6, pill="Ex 06", title="Onboarding Orientation Pack", short="Onboarding Pack",
        function="HR \u00b7 Onboarding", minutes="20 min",
        goal="Give a new hire a polished first-day experience without assembling it by hand.",
        output="A 6\u20138 slide orientation deck, a scheduled kickoff with a Teams link, and a team announcement "
               "draft for Sofia Alvarez, Zava\u2019s new HR Coordinator.",
        why="Onboarding spans documents, calendars, and communications. Cowork chains PowerPoint, Scheduling, and "
            "Communications skills in one flow, grounded in your checklist, handbook, and benefits.",
        prompt=["## Task 6a \u2014 Orientation deck",
                "{s}Using onboarding-checklist.docx, employee-handbook-excerpt.docx, and benefits-summary.docx{/s}, {g}build a short "
                "onboarding orientation PowerPoint{/g} {e}(6\u20138 slides){/e} {g}covering first-day logistics, PTO, remote/hybrid "
                "work, and benefits basics.{/g} {e}Keep it clean and friendly.{/e} {c}Use only facts from these files.{/c}",
                "",
                "## Task 6b \u2014 Schedule the kickoff",
                "{g}Schedule a 30-minute onboarding kickoff for Sofia Alvarez\u2019s first day{/g}, {e}next Monday at 9:30 AM, "
                "add a Teams meeting link{/e}, {c}and invite only me. Show it to me before you send it.{/c}",
                "",
                "## Task 6c \u2014 Team announcement",
                "{g}Draft a warm, inclusive team announcement introducing Sofia Alvarez, our new HR Coordinator starting "
                "next Monday, and her first-week plan{/g}, {s}using onboarding-checklist.docx{/s}. {e}Save it as an Outlook email "
                "draft addressed to me{/e}; {c}don\u2019t send it.{/c}"],
        prompt_size=11.5,
        workflow=[("Ground", "Checklist, handbook, benefits"), ("Build", "Orientation deck (PowerPoint)"),
                  ("Schedule", "30-min kickoff with a Teams link"), ("Communicate", "Team announcement draft")],
        sources=["onedrive", "m365"],
        discuss='What else belongs in a new-hire pack at your organization — and who should review it?',
        steps=["**Task 6a:** attach the checklist, handbook, and benefits files; build a 6\u20138 slide orientation deck.",
               "**Task 6b:** schedule a 30-minute kickoff with a Teams link \u2014 invite **only yourself**.",
               "**Task 6c:** draft a warm team announcement and save it as an Outlook draft to yourself.",
               "**Review** each artifact at its checkpoint."],
        watch=["**PowerPoint**, **Scheduling/Calendar**, and **Communications** chips",
               "No real invitees in the shared tenant", "Short on time? Do 6a + 6c; watch 6b as a demo"],
        checkpoint="An orientation deck, a reviewed kickoff invite, and a team announcement draft for Sofia Alvarez.",
        stretch="Turn the orientation deck into a one-page PDF handout.",
        notes_card="EXERCISE 6 CARD (2:55-3:15, 20 min). SAY: 'Sofia Alvarez accepted the HR Coordinator role and starts next Monday. Let's get her first day ready.' This is the story arc from Ex 2 (interview) and Ex 5 (posting). Several built-in skills chain together: PowerPoint, Scheduling, Communications. Call out each new skill chip.",
        notes_hands="EXERCISE 6 HANDS-ON. DO: 6a first (the deck takes longest), then 6b and 6c while it builds. WATCH FOR: PowerPoint, Scheduling/Calendar, and Communications chips; an approval dialog before the invite is sent; the announcement saved as a draft, not sent. SAFETY: invite yourself only; Sofia is fictional and has no account. IF STUCK: no Teams link -> ask Cowork to add one before approving. TIME CHECK: short on time, do 6a + 6c and watch 6b as a demo. NEXT: 'Now let's stop re-asking for the same work.'",
    ),
    dict(
        num=7, pill="Ex 07", title="Automate & Share", short="Automate & Share", function="HR \u00b7 Operations",
        minutes="15 min",
        goal="Stop re-asking for the same work \u2014 put it on a schedule and share what you built.",
        output="An active weekly automation (Monday HR-ticket digest), a Daily Briefing, and your custom skill shared "
               "(or kept private) and re-shared after an edit.",
        why="Recurring work belongs on autopilot. Automations run prompts on a schedule or on events, Daily Briefing "
            "pulls your day together, and sharing turns a personal skill into a team asset.",
        prompt=["## Task 7a \u2014 Automations \u2192 Create",
                "{e}Every Monday at 8:00 AM{/e}, {s}read hr-tickets-sample.xlsx in my OneDrive folder Documents/ai_hr_cowork_workshop{/s}, {g}summarize "
                "open tickets by category and priority{/g}, {e}list high-priority open tickets first, and put it in a short "
                "report.{/e} {c}Don\u2019t email anyone.{/c}",
                "",
                "Choose Activate and run now to see the first run in class.",
                "",
                "## Task 7b \u2014 New task",
                "{g}Give me a Daily Briefing{/g} {s}focused on my HR tasks and meetings for today{/s}. {e}List the most urgent items first.{/e}",
                "",
                "## Task 7c \u2014 Share your skill",
                "Open HR Policy Answer on the Customize page \u2192 Share. Keep it \u201cOnly you\u201d or share to one "
                "colleague (add your initials first). Make a small edit, then Re-share."],
        prompt_size=12.5,
        workflow=[("Automations", "Create a weekly schedule"), ("Monitor", "Runs and Manage schedules"),
                  ("Brief", "Daily Briefing for today"), ("Share", "Share / re-share your skill")],
        sources=["m365", "onedrive"],
        discuss='Which report do you rebuild every week that should become an automation?',
        steps=["**Automations \u2192 Create:** paste the digest prompt \u2014 it names the exact file and folder.",
               "Choose **Activate and run now**, then check the **Runs** tab for today\u2019s run.",
               "**New task:** ask for a Daily Briefing on your HR tasks and meetings.",
               "**Customize \u2192 Skills \u2192 HR Policy Answer \u2192 Share;** make an edit, then Re-share."],
        watch=["Where to pause, edit, or delete a schedule", "The **Daily Briefing** skill chip",
               "Share etiquette: \u201cOnly you\u201d or initialed names"],
        checkpoint="An active weekly schedule with a completed run naming T-2008, a Daily Briefing, and the "
                   "share / re-share flow completed.",
        stretch="Send the Monday digest as an email draft to your manager instead of a report.",
        notes_card="EXERCISE 7 CARD (3:15-3:30, 15 min). SAY: 'You built a skill and a report. Now put recurring work on a schedule and share what you built.' They already created one schedule in Ex 1; now they see where schedules live and how to control them.",
        notes_hands="EXERCISE 7 HANDS-ON. DO: create the Automation live; choose 'Activate and run now'; show Runs vs Manage schedules (edit, pause, resume, delete). Demo a Daily Briefing, then Share / Re-share on the Ex 4 skill. WATCH FOR: an Active schedule and a completed run naming T-2008. IF STUCK: run can't find the file -> the prompt must name the exact file and folder. Sharing stays inside the attendee tenant: 'Only you' or initialed names. TIME CHECK: 7a is the must-do; 7b and 7c can be demo-only. NEXT: the plugins spotlight.",
    ),
    dict(
        num=8, pill="Ex 08", title="HR Policy Agent with Agent Builder", short="HR Policy Agent",
        function="Agent Builder", minutes="20 min", why_label="Agent Builder",
        goal="Stand up a reusable Q&A agent employees can chat with to get sourced policy answers.",
        output="A working \u201cHR Policy Agent\u201d in Microsoft 365 Copilot, grounded in Zava\u2019s HR documents, that "
               "cites sources and declines out-of-scope questions.",
        why="A Cowork skill helps you in your own tasks. An agent is a standalone helper other people use directly in "
            "Copilot \u2014 built with no code via Describe \u2192 Configure \u2192 Try it, then shared or published.",
        prompt=["## Describe tab",
                "{g}Create an HR Policy Agent that answers employee questions about company policies and benefits \u2014 "
                "PTO, remote/hybrid work, benefits enrollment, overtime, and the code of conduct{/g} \u2014 {e}in a warm, "
                "professional tone. Always cite the source document and remind the reader that HR should confirm.{/e} "
                "{c}Politely decline questions about individual pay, performance, legal, or medical matters and "
                "redirect them to HR.{/c}",
                "",
                "## Configure tab",
                "- Name: HR Policy Agent",
                "- Knowledge: employee-handbook-excerpt.docx and benefits-summary.docx (upload, or pick from OneDrive)",
                "- Suggested prompts: \u201cHow much PTO do I get?\u201d \u00b7 \u201cWhen is open enrollment?\u201d \u00b7 "
                "\u201cWhat are the anchor office days?\u201d"],
        prompt_size=11.5,
        workflow=[("Describe", "Define the agent in plain language"), ("Configure", "Name, instructions, knowledge, prompts"),
                  ("Try it", "Test in-scope and out-of-scope"), ("Share", "Share or publish (optional)")],
        sources=["sharepoint"],
        discuss='Who would use a policy agent in your org, and which questions should it always hand to a human?',
        steps=["**Microsoft 365 Copilot \u2192 Create agent** (desktop or web).",
               "**Describe** the HR Policy Agent in plain language.",
               "**Configure:** name, instructions, knowledge (the Zava Word files), suggested prompts.",
               "**Try it:** a policy question gets a sourced answer; a salary question is declined.",
               "**Share or publish** (optional)."],
        watch=["This is **Agent Builder** \u2014 not Cowork", "Knowledge must be **.docx/.pdf/.xlsx** \u2014 not .md or .csv",
               "Skill (Ex 4) helps you; this agent helps others", "New files show \u201cPreparing\u201d for a few minutes"],
        checkpoint="A working HR Policy Agent that gives grounded, sourced answers and declines out-of-scope questions.",
        stretch="Add the onboarding checklist as a third knowledge source and a new-hire suggested prompt.",
        notes_card="EXERCISE 8 CARD (3:35-3:55, 20 min) - NON-COWORK CAPSTONE. SAY: 'Everything so far helped YOU. Now we build something OTHER people can use: an agent, in Microsoft 365 Copilot's Agent Builder.' Same no-code spirit, different tool: a persistent, shareable agent grounded in the same Zava files.",
        notes_hands="EXERCISE 8 HANDS-ON. DO: build live via Describe -> Configure -> Try it; add the two Zava Word files as KNOWLEDGE; test the open-enrollment question (sourced answer) and the salary question (declines). WATCH FOR: files showing 'Preparing' for a few minutes; .md or .csv files are rejected. IF STUCK: answers ignore the files -> wait, or refresh Knowledge in Configure; no Create agent -> desktop/web Microsoft 365 Copilot with a license. External ACTIONS need Copilot Studio (out of scope). TIME CHECK: if behind, run it as a demo and have attendees build it after class. Detail: reference/08-agent-builder-policy-agent.md. NEXT: wrap-up.",
    ),
]
