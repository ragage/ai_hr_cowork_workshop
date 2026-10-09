"""Scenario-card content for the instructor deck (mirrors participant-workbook.md).

Prompt text marks its elements for color coding: {g}Goal{/g}, {s}Source{/s}, {e}Expectations{/e},
{c}Constraints{/c} (the workbook uses <span class=...> for the same thing). Exercise 8 keeps its exact
wording; only the markers were added.
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
        "- Colors mark the {g}Goal{/g}, {s}Source{/s}, {e}Expectations{/e}, and {c}Constraints{/c} (see the Prompt key)",
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
               "with numbered steps, what to watch for, a checkpoint, and a stretch. The Prompt key at the bottom right "
               "shows what each prompt color means; the colors are the same on every card and in the workbook.",
)


EXEC_PROMPT = [
    "{g}Build an interactive HTML Executive Command Center that shows what requires my attention today and this "
    "week.{/g}",
    "",
    "{s}Use my calendar, recent emails, Teams conversations, meeting transcripts, and priority documents from "
    "[Priority Folder].{/s} {g}Focus on decisions, commitments, risks, and workstreams where my involvement could "
    "change the outcome.{/g}",
    "",
    "{e}At the top, show:{/e}",
    "- {e}One or two urgent items requiring action{/e}",
    "- {e}Today\u2019s most important meeting or priority{/e}",
    "- {e}My busiest day this week{/e}",
    "- {e}Remaining working days this week{/e}",
    "",
    "{e}Organize the command center into three views:{/e}",
    "- {e}Meetings: Key meetings, preparation needed, conflicts, and follow-ups{/e}",
    "- {e}Priorities: Active commitments, approaching deadlines, blockers, and decisions waiting on me{/e}",
    "- {e}Org pulse: Workstreams receiving significant attention, areas with limited recent activity, and "
    "important commitments that may have gone quiet{/e}",
    "",
    "{e}For each recommended action, label it:{/e}",
    "- {e}Lean in; OR, Delegate; OR, Re-engage; OR, Protect time{/e}",
    "",
    "{e}Explain the signal behind the recommendation and give me one clear next action.{/e} {c}Keep recommendations "
    "focused on workstreams, decisions, and commitments rather than evaluating individual people.{/c} {e}Make the "
    "dashboard executive-ready and easy to scan, with expandable sections, traffic-light indicators, and links "
    "to the supporting emails, meetings, chats, and files.{/e} {g}The most important content should answer: What "
    "needs my attention, and what should I do differently today?{/g}",
    "",
    "{e}Save this as a skill named [Executive Command Center] and schedule it to run every weekday at [time], "
    "using the latest available context.{/e}",
]

EXERCISES = [
    dict(
        num=1, pill="Ex 01", title="Research the Web with Deep Research", short="Deep Research",
        function="HR \u00b7 Talent", minutes="15 min",
        goal="Get an evidence-based view of structured behavioral interviewing and turn it into questions for a "
             "real open role.",
        output="A cited one-page briefing and five tailored questions for Zava\u2019s HR Coordinator role; if time "
               "allows, an interviewer scorecard in Word and Excel with the scoring scales filled in.",
        why="Good research means reading and citing many sources. Deep Research does that across the web, applies "
            "the findings to your job description, and a follow-up turns them into ready-to-use documents.",
        prompt=["{g}Use Deep Research to summarize current best practices for structured behavioral interviews{/g} {s}from "
                "multiple reputable sources{/s}. {e}Produce a 1-page briefing with the key practices and cite your sources.{/e}",
                "",
                "## Then:",
                "{g}Now compare these best practices to our HR Coordinator interview needs{/g} {s}in "
                "job-description-sample.docx{/s}, {e}and suggest 5 interview questions.{/e}",
                "",
                "## Optional follow-up (if you have time):",
                "{g}Turn this into an interviewer scorecard{/g} {e}in Word AND Excel with the scoring scales filled in.{/e}"],
        prompt_size=12.5,
        workflow=[("Deep Research", "Search and read multiple web sources"), ("Synthesize", "Key practices with citations"),
                  ("Ground", "Compare to job-description-sample.docx"), ("Draft", "Briefing + 5 tailored questions"),
                  ("Build", "Optional: scorecard in Word + Excel")],
        sources=["web", "onedrive"],
        discuss='When is web research better than searching your own organization\u2019s content \u2014 and when is it riskier?',
        steps=["**New task** \u2192 run the Deep Research prompt.",
               "**Watch** it search and read multiple sources, citing each. Open two citations.",
               "**Ground it:** attach job-description-sample.docx and compare the findings to it.",
               "**Ask for** five tailored interview questions.",
               "**Optional:** scorecard in **Word AND Excel**, scales filled in; open both from the **Output folder**.",
               "**Optional:** type **/cost** in this task to check approximate credits used (next slide)."],
        watch=["The **Deep Research** skill chip and progress", "Citations you can open and check",
               "Optional scorecard: **Word** + **Excel** chips", "Scales filled in \u2014 no \u201cTBD\u201d anchors"],
        checkpoint="A cited briefing and five interview questions tied to the HR Coordinator role (plus the optional "
                   "Word + Excel scorecard, every scale filled in).",
        stretch="Benchmark PTO / annual-leave norms for mid-size tech firms against the Zava handbook.",
        notes_card="EXERCISE 1 CARD (0:20-0:35, 15 min). SAY: 'Deep Research reads many web sources and cites them, then we make it useful by grounding it in our own job description and turning it into documents.' Point out the three stages on the card: research, ground, and an optional build (Word + Excel). Next exercise shows the OTHER way Cowork uses the web: driving a browser.",
        notes_hands="EXERCISE 1 HANDS-ON. DO: start Deep Research on your screen first (it takes a few minutes), then the room starts theirs. Use the wait: 'When is web research better than our own content, and when is it riskier?' WATCH FOR: the Deep Research chip; citations that open; Word and Excel chips for the scorecard. IF STUCK: blank scales -> reply 'Fill in the 1, 3, and 5 anchors for every competency.' Only one file -> 'Also create the Excel version.' The scorecard (Task 1c) is OPTIONAL: fast finishers run it. TIME CHECK: at 0:30, demo the scorecard on your screen so everyone sees the Word + Excel output. NEXT: the browser.",
    ),
    dict(
        num=2, pill="Ex 02", title="Navigate Websites with Cowork\u2019s Browser", short="Browser",
        function="HR \u00b7 Compliance", minutes="15 min",
        goal="Have Cowork drive a real web browser for you \u2014 search a site, click through, move to a second "
             "site \u2014 and bring back a sourced comparison.",
        output="An overtime comparison (U.S. DOL vs. Washington L&I vs. Zava handbook) with a link to every page "
               "visited; if time allows, a one-page Word brief for payroll about T-2008.",
        why="Checking policy against official sites means searching, clicking, and copying. Cowork does the clicks in a "
            "hidden tab in your own Edge, with your sign-ins and policies, and asks before anything consequential.",
        prompt=["## Task 2a \u2014 Attach the handbook, then:",
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
                "## Task 2b \u2014 Optional follow-up",
                "{g}Turn this into a one-page Word brief for our payroll team about ticket T-2008{/g}: {e}what the rules say, "
                "what our handbook says, and the recommended next step.{/e} {c}Don\u2019t send it.{/c}"],
        prompt_size=12,
        workflow=[("Navigate", "dol.gov: site search \u2192 Fact Sheet #23"), ("Navigate", "lni.wa.gov: menu \u2192 overtime page"),
                  ("Ground", "Compare with the Zava handbook"), ("Build", "Table with links (+ optional brief)")],
        sources=["web", "onedrive"],
        discuss='When would you use browser use instead of Deep Research? What would you never let it do unwatched?',
        steps=["**Check:** Cowork open **in Edge**; Edge profile = **your work account**; Edge setting **Allow Cowork to take actions** on.",
               "**New task:** attach the handbook; paste the two-site prompt.",
               "**Consent:** select **I understand** at the browser notice.",
               "**Switch to tab** to watch it search dol.gov and click through; open two links yourself.",
               "**Optional:** the Word brief for payroll; open it from the **Output folder**."],
        watch=["No \u201cbrowser\u201d skill chip \u2014 watch the **progress chips**",
               "It types in the **site search** and clicks menus (not guessed URLs)",
               "Sign-in or CAPTCHA? It hands back \u2014 don\u2019t enter anything",
               "Nothing submitted beyond a search box"],
        checkpoint="Two sites navigated by search and menus, and a comparison table linking the DOL fact sheet and "
                   "the Washington L&I overtime page (plus the optional Word brief about T-2008).",
        stretch="Read only: DOL Fact Sheet #17A and Washington\u2019s exempt salary minimum. Is a salaried HR Coordinator likely exempt?",
        notes_card="EXERCISE 2 CARD (0:35-0:50, 15 min). SAY: 'This is Cowork driving a real browser, like a person or a test tool such as Playwright: it types in a site's search box, clicks links and menus, and moves to another site. There's no browser skill to pick and no skill chip; ask for something that needs a website and Cowork opens a hidden tab in your own Edge, with your sign-ins and your company's policies.' Contrast with Deep Research (reads and cites) from Ex 1.",
        notes_hands="EXERCISE 2 HANDS-ON. DO: demo first. Show the consent notice (I understand), the progress chips, and Switch to tab so the room sees Edge typing in the DOL search box and clicking through to Fact Sheet #23, then lni.wa.gov. WATCH FOR: a table showing Zava's 1.5x over 40 hours matches federal and Washington rules; DOL adds the regular-payday rule; Washington adds no waiver and no daily overtime; links to both pages. IF STUCK: 'Browser tasks run in Microsoft Edge' -> wrong browser; no browser at all -> Edge profile isn't their work account, InPrivate, the Edge setting is off, or the admin hasn't allowed browser access (reference/10-cowork-browser.md). They follow your demo. 2b is OPTIONAL: fast finishers run it; at 0:45 demo it. STRETCH: Fact Sheet #17A on dol.gov plus Washington's exempt salary minimum on lni.wa.gov, read only. Don't send people to interactive tools such as the DOL eLaws advisors; Cowork declined one in the dry run. NEXT: 'You've used built-in skills and the browser. Now build your own skill.'",
    ),
    dict(
        num=3, pill="Ex 03", title="Build a Custom Skill: HR Policy Answer", short="Custom Skill",
        function="HR \u00b7 Policy", minutes="15 min",
        goal="Teach Cowork to answer policy and benefits questions the same clear, sourced way \u2014 every time.",
        output="A saved custom skill, \u201cHR Policy Answer,\u201d with a quality score, that triggers on policy "
               "questions and answers Answer \u2192 Details \u2192 Source \u2192 \u201cconfirm with HR.\u201d",
        why="Repeating the same instructions in every prompt is error-prone. A custom skill packages tone, format, "
            "sources, and guardrails once; Cowork auto-evaluates it (0\u2013100) and applies it when it\u2019s needed.",
        prompt=["In Customize \u2192 Skills \u2192 Add \u2192 Create new, give Cowork these details:",
                "",
                "- Name: HR Policy Answer",
                "- Category: Human Resources",
                "- Description: Answers Zava employee policy and benefits questions in a consistent, sourced "
                "format, grounded only in Zava\u2019s handbook and benefits documents.",
                "",
                "## Instructions:",
                "{g}Use this skill when someone asks about Zava\u2019s HR policy or benefits (PTO, remote/hybrid work, "
                "benefits enrollment, overtime, code of conduct, learning budget).{/g} {s}Ground answers only in "
                "employee-handbook-excerpt.docx and benefits-summary.docx in my OneDrive folder Documents/ai_hr_cowork_workshop.{/s} "
                "{c}Don\u2019t use web results or any other documents in my Microsoft 365, and if the answer isn\u2019t in "
                "these two files, say so instead of guessing.{/c} {e}Answer in this format: a direct "
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
               "**Test** in a **new task:** \u201cAt Zava, when is open enrollment\u2026?\u201d should trigger it; a salary question should be declined."],
        watch=["Scores: trigger clarity, instruction specificity, scope boundaries, robustness",
               "Answer \u2192 Details \u2192 Source \u2192 \u201cconfirm with HR\u201d",
               "Name **Zava** in the test, or it may answer from your own company\u2019s content",
               "Keep the skill **\u201cOnly you\u201d** in the shared tenant"],
        checkpoint="Your skill scores Good or better, triggers on its own, follows the format, and declines "
                   "out-of-scope questions.",
        stretch="Add a rule to link to the HR portal whenever a change requires a form.",
        notes_card="EXERCISE 3 CARD (0:50-1:05, 15 min) - CENTERPIECE. SAY: 'Build your first custom skill on purpose and let Cowork grade it; the capstone later saves one from a prompt.' Explain why a skill beats re-typing instructions: same format, sources, and guardrails every time. Scoring bands: Excellent 85+, Good 70-84, Needs work 50-69, Poor <50.",
        notes_hands="EXERCISE 3 HANDS-ON. DO: build it live from Customize -> Skills -> Add -> Create new; paste the instructions; read the evaluation ALOUD and name the four dimensions (trigger clarity, instruction specificity, scope boundaries, robustness). Then test both questions in a NEW task, and start the policy question with 'At Zava': attendees' own tenants hold real benefits content, and in the dry run a generic question pulled that instead. WATCH FOR: the skill triggering WITHOUT being named; Answer -> Details -> Source -> confirm-with-HR; the salary question declined. IF STUCK: 'Needs work' -> tighten trigger wording and the out-of-scope list; wrong facts -> check the two file names in the instructions match their OneDrive; answer quotes their own company's benefits -> the instructions must say ONLY the two Zava files, then retest in a new task. Keep skills 'Only you'. Answer key: facilitator-answer-key.md and skills/hr-policy-answer/SKILL.md. NEXT: 'This skill helps YOU. In Ex 7 we build an agent that helps OTHERS.'",
    ),
    dict(
        num=4, pill="Ex 04", title="Recruiting + Reporting", short="Recruiting + Reporting",
        function="HR \u00b7 Talent & Ops", minutes="15 min",
        goal="Attract the right candidates for an open role and get on top of the HR service queue in minutes.",
        output="An inclusive HR Coordinator job posting in Word, with off-putting wording flagged, and a ticket "
               "summary highlighting today\u2019s high-priority open items.",
        why="One task reads a job description and writes a structured document; the other analyzes a spreadsheet and reports "
            "on it. Cowork picks the right skills (Word, Excel) for each and grounds both in your files.",
        prompt=["## Task 4a \u2014 Inclusive job posting",
                "{s}Using job-description-sample.docx{/s}, {g}write an inclusive, engaging job posting for the HR Coordinator "
                "role for our careers page.{/g} {e}Keep it under 350 words, with short What you\u2019ll do, What you\u2019ll "
                "bring, and What we offer sections, and mention the hybrid schedule. Then add a separate table that "
                "flags any wording in the original description that could discourage qualified applicants, with a "
                "suggested alternative for each. Save it as a Word doc.{/e} {c}Don\u2019t add pay figures, perks, or "
                "requirements that aren\u2019t in the description.{/c}",
                "",
                "## Task 4b \u2014 Ticket summary",
                "{s}Using hr-tickets-sample.xlsx{/s}, {g}summarize open vs. closed tickets by category and priority, and list "
                "the high-priority open items I should follow up on today.{/g} {e}Put it in a short report.{/e}"],
        prompt_size=12.5,
        workflow=[("Ground", "Read the job description and ticket spreadsheet"), ("Draft", "Inclusive job posting (Word)"),
                  ("Analyze", "Open vs. closed by category & priority"), ("Report", "Today\u2019s high-priority follow-ups")],
        sources=["onedrive"],
        discuss='Which recruiting or reporting task eats most of your week today?',
        steps=["**Task 4a:** attach job-description-sample.docx; write the inclusive job posting and save it as Word.",
               "**Check** the wording-review table: do you agree with every flag?",
               "**Task 4b:** attach hr-tickets-sample.xlsx; summarize open vs. closed by category and priority.",
               "**List** today\u2019s high-priority open items to follow up."],
        watch=["**Word** for the posting; **Excel** for the analysis",
               "The High/Open overtime ticket (T-2008)", "You\u2019ll automate this report in Exercise 6"],
        checkpoint="A Word job posting with a wording-review table, and a ticket summary: 6 open / 14 closed, with "
                   "T-2008 as the only high-priority open ticket.",
        stretch="Summarize employee-roster-sample.xlsx: headcount by department, remote vs. on-site, average PTO used.",
        notes_card="EXERCISE 4 CARD (1:05-1:20, 15 min). SAY: 'Two quick wins. In Ex 1 we prepared to interview for the HR Coordinator role; now we write the posting that attracts the right candidates. Then we get on top of the ticket queue.' Point out that Cowork picks Word for writing and Excel for analysis on its own.",
        notes_hands='EXERCISE 4 HANDS-ON. DO: run 4a and 4b back to back; attendees can start 4b while 4a is still working. WATCH FOR: 4a -> a posting under 350 words with the hybrid schedule, plus a wording-review table (e.g., degree requirement, years of experience framed as must-haves); discuss whether every flag is fair. 4b -> 6 open / 14 closed, T-2008 as the ONLY high-priority open ticket. TRAP: T-2003 and T-2013 are High but Closed; listing them means Status was ignored. IF STUCK: wrong counts -> ask Cowork to show the table it counted from. NEXT: break, then they automate this report in Ex 6.',
    ),
    dict(
        num=5, pill="Ex 05", title="Onboarding Orientation Pack", short="Onboarding Pack",
        function="HR \u00b7 Onboarding", minutes="10 min",
        goal="Give a new hire a polished first-day experience without assembling it by hand.",
        output="A 6\u20138 slide orientation deck for Sofia Alvarez, Zava\u2019s new HR Coordinator; if time allows, a "
               "scheduled kickoff with a Teams link and a team announcement draft.",
        why="Onboarding spans documents, calendars, and communications. Cowork chains PowerPoint, Scheduling, and "
            "Communications skills in one flow, grounded in your checklist, handbook, and benefits.",
        prompt=["## Task 5a \u2014 Orientation deck",
                "{s}Using onboarding-checklist.docx, employee-handbook-excerpt.docx, and benefits-summary.docx{/s}, {g}build a short "
                "onboarding orientation PowerPoint{/g} {e}(6\u20138 slides){/e} {g}covering first-day logistics, PTO, remote/hybrid "
                "work, and benefits basics.{/g} {e}Keep it clean and friendly.{/e} {c}Use only facts from these files.{/c}",
                "",
                "## Task 5b \u2014 Optional: schedule the kickoff",
                "{g}Schedule a 30-minute onboarding kickoff for Sofia Alvarez\u2019s first day{/g}, {e}next Monday at 9:30 AM, "
                "add a Teams meeting link{/e}, {c}and invite only me. Show it to me before you send it.{/c}",
                "",
                "## Task 5c \u2014 Optional: team announcement",
                "{g}Draft a warm, inclusive team announcement introducing Sofia Alvarez, our new HR Coordinator starting "
                "next Monday, and her first-week plan{/g}, {s}using onboarding-checklist.docx{/s}. {e}Save it as an Outlook email "
                "draft addressed to me{/e}; {c}don\u2019t send it.{/c}"],
        prompt_size=11.5,
        workflow=[("Ground", "Checklist, handbook, benefits"), ("Build", "Orientation deck (PowerPoint)"),
                  ("Schedule", "Optional: kickoff with a Teams link"), ("Communicate", "Optional: announcement draft")],
        sources=["onedrive", "m365"],
        discuss='What else belongs in a new-hire pack at your organization — and who should review it?',
        steps=["**Task 5a:** attach the checklist, handbook, and benefits files; build a 6\u20138 slide orientation deck.",
               "**Optional 5b:** schedule a 30-minute kickoff with a Teams link \u2014 invite **only yourself**.",
               "**Optional 5c:** draft a warm team announcement and save it as an Outlook draft to yourself.",
               "**Review** each artifact at its checkpoint."],
        watch=["**PowerPoint**, **Scheduling/Calendar**, and **Communications** chips",
               "Your real calendar: invite only yourself", "5a is the must-do; 5b and 5c are optional"],
        checkpoint="A 6\u20138 slide orientation deck for Sofia Alvarez built only from the Zava files (plus the optional "
                   "kickoff invite and announcement draft).",
        stretch="Turn the orientation deck into a one-page PDF handout.",
        notes_card="EXERCISE 5 CARD (1:35-1:45, 10 min). SAY: 'Sofia Alvarez accepted the HR Coordinator role and starts next Monday. Let's get her first day ready.' This is the story arc from Ex 1 (interview) and Ex 4 (posting). Several built-in skills chain together: PowerPoint, Scheduling, Communications. Call out each new skill chip.",
        notes_hands="EXERCISE 5 HANDS-ON. DO: 5a is the must-do (the deck takes longest); 5b and 5c are OPTIONAL for fast finishers, or demo them while the deck builds. WATCH FOR: PowerPoint, Scheduling/Calendar, and Communications chips; an approval dialog before the invite is sent; the announcement saved as a draft, not sent. SAFETY: invite yourself only; Sofia is fictional and has no account. IF STUCK: no Teams link -> ask Cowork to add one before approving. TIME CHECK: at 1:45 move on, even if only 5a is done. NEXT: 'Now let's stop re-asking for the same work.'",
    ),
    dict(
        num=6, pill="Ex 06", title="Automate & Share", short="Automate & Share", function="HR \u00b7 Operations",
        minutes="15 min",
        goal="Stop re-asking for the same work \u2014 put it on a schedule and share what you built.",
        output="An active weekly automation (Monday HR-ticket digest) and a Daily Briefing; if time allows, your "
               "custom skill shared (or kept private) and re-shared after an edit.",
        why="Recurring work belongs on autopilot. Automations run prompts on a schedule or on events, Daily Briefing "
            "pulls your day together, and sharing turns a personal skill into a team asset.",
        prompt=["## Task 6a \u2014 Automations \u2192 Create",
                "{e}Every Monday at 8:00 AM{/e}, {s}read hr-tickets-sample.xlsx in my OneDrive folder Documents/ai_hr_cowork_workshop{/s}, {g}summarize "
                "open tickets by category and priority{/g}, {e}list high-priority open tickets first, and put it in a short "
                "report.{/e} {c}Don\u2019t email anyone.{/c}",
                "",
                "Choose Activate and run now to see the first run in class.",
                "",
                "## Task 6b \u2014 New task",
                "{g}Give me a Daily Briefing{/g} {s}focused on my HR tasks and meetings for today{/s}. {e}List the most urgent items first.{/e}",
                "",
                "## Task 6c \u2014 Optional: share your skill",
                "Open HR Policy Answer on the Customize page \u2192 Share. Keep it \u201cOnly you\u201d or share to one "
                "colleague (add your initials first). Make a small edit, then Re-share."],
        prompt_size=12.5,
        workflow=[("Automations", "Create a weekly schedule"), ("Monitor", "Runs and Manage schedules"),
                  ("Brief", "Daily Briefing for today"), ("Share", "Optional: share / re-share your skill")],
        sources=["m365", "onedrive"],
        discuss='Which report do you rebuild every week that should become an automation?',
        steps=["**Automations \u2192 Create:** paste the digest prompt \u2014 it names the exact file and folder.",
               "Choose **Activate and run now**, then check the **Runs** tab for today\u2019s run.",
               "**New task:** ask for a Daily Briefing on your HR tasks and meetings.",
               "**Optional:** **Customize \u2192 Skills \u2192 HR Policy Answer \u2192 Share;** make an edit, then Re-share."],
        watch=["Where to pause, edit, or delete a schedule", "The **Daily Briefing** skill chip",
               "Share etiquette: \u201cOnly you\u201d or initialed names"],
        checkpoint="An active weekly schedule with a completed run naming T-2008, and a Daily Briefing (plus the "
                   "optional share / re-share).",
        stretch="Send the Monday digest as an email draft to your manager instead of a report.",
        notes_card="EXERCISE 6 CARD (1:45-2:00, 15 min). SAY: 'You built a skill and a report. Now put recurring work on a schedule and share what you built.' This is their first scheduled workflow; show where schedules live and how to control them.",
        notes_hands="EXERCISE 6 HANDS-ON. DO: create the Automation live; choose 'Activate and run now'; show Runs vs Manage schedules (edit, pause, resume, delete). Demo a Daily Briefing, then Share / Re-share on the Ex 3 skill. WATCH FOR: an Active schedule and a completed run naming T-2008. IF STUCK: run can't find the file -> the prompt must name the exact file and folder. Sharing stays inside the attendee tenant: 'Only you' or initialed names. TIME CHECK: 6a is the must-do; 6b is quick; 6c is OPTIONAL, so demo it. NEXT: Agent Builder, the non-Cowork policy-agent exercise.",
    ),
    dict(
        num=7, pill="Ex 07", title="HR Policy Agent with Agent Builder", short="HR Policy Agent", not_cowork=True,
        function="Agent Builder", minutes="15 min", why_label="Agent Builder",
        goal="Stand up a reusable Q&A agent employees can chat with to get sourced policy answers.",
        output="A working \u201cHR Policy Agent\u201d in Microsoft 365 Copilot, grounded in Zava\u2019s HR documents, that "
               "cites sources and declines out-of-scope questions.",
        why="A Cowork skill helps you in your own tasks. An agent is a standalone helper other people use directly in "
            "Copilot \u2014 built with no code via Describe \u2192 Configure \u2192 Try it, then shared or published.",
        prompt=["## Describe tab",
                "{g}Create an HR Policy Agent that answers Zava employees\u2019 questions about Zava\u2019s policies and benefits \u2014 "
                "PTO, remote/hybrid work, benefits enrollment, overtime, and the code of conduct{/g} \u2014 {s}using only "
                "Zava\u2019s HR documents{/s}, {e}in a warm, professional tone. Always cite the source document and remind "
                "the reader that HR should confirm.{/e} "
                "{c}Politely decline questions about individual pay, performance, legal, or medical matters and "
                "redirect them to HR.{/c}",
                "",
                "## Configure tab",
                "- Name: HR Policy Agent",
                "- Knowledge: employee-handbook-excerpt.docx and benefits-summary.docx (upload, or pick from OneDrive)",
                "- Only use specified sources: On \u00b7 Search all websites: Off",
                "- Suggested prompts: \u201cHow much PTO do I get at Zava?\u201d \u00b7 \u201cWhen is Zava\u2019s open enrollment?\u201d \u00b7 "
                "\u201cWhat are Zava\u2019s anchor office days?\u201d"],
        prompt_size=11.5,
        workflow=[("Describe", "Define the agent in plain language"), ("Configure", "Name, instructions, knowledge, prompts"),
                  ("Try it", "Test in-scope and out-of-scope"), ("Share", "Share or publish (optional)")],
        sources=["sharepoint"],
        discuss='Who would use a policy agent in your org, and which questions should it always hand to a human?',
        steps=["**Microsoft 365 Copilot \u2192 Create agent** (desktop or web).",
               "**Describe** the HR Policy Agent in plain language.",
               "**Configure:** name, instructions, the Zava Word files; **Only use specified sources** on, **Search all websites** off.",
               "**Try it:** \u201cAt Zava, when is open enrollment\u2026?\u201d gets a sourced answer; a salary question is declined.",
               "**Share or publish** (optional)."],
        watch=["This is **Agent Builder** \u2014 not Cowork", "Knowledge must be **.docx/.pdf/.xlsx** \u2014 not .md or .csv",
               "Skill (Ex 3) helps you; this agent helps others", "New files show \u201cPreparing\u201d for a few minutes"],
        checkpoint="A working HR Policy Agent that gives grounded, sourced answers and declines out-of-scope questions.",
        stretch="Add the onboarding checklist as a third knowledge source and a new-hire suggested prompt.",
        notes_card="EXERCISE 7 CARD (2:00-2:15, 15 min) - NON-COWORK EXERCISE. SAY: 'Everything so far helped YOU. Now we build something OTHER people can use: an agent, in Microsoft 365 Copilot's Agent Builder.' Same no-code spirit, different tool: a persistent, shareable agent grounded in the same Zava files.",
        notes_hands="EXERCISE 7 HANDS-ON. DO: build live via Describe -> Configure -> Try it; add the two Zava Word files as KNOWLEDGE; in Knowledge turn ON 'Only use specified sources' and OFF 'Search all websites'; test 'At Zava, when is open enrollment...?' (sourced answer) and the salary question (declines). WATCH FOR: files showing 'Preparing' for a few minutes; .md or .csv files are rejected. IF STUCK: answers ignore the files -> wait, or refresh Knowledge in Configure; answers about the attendee's own company benefits (seen in the dry run) -> check those two settings and the 'At Zava' wording; Agent Builder prioritizes your sources but can't fully block general knowledge (Copilot Studio can); no Create agent -> desktop/web Microsoft 365 Copilot with a license. External ACTIONS need Copilot Studio (out of scope). TIME CHECK: if behind, run it as a demo and have attendees build it after class. Detail: reference/08-agent-builder-policy-agent.md. NEXT: return to Cowork for the Executive Command Center capstone.",
    ),
    dict(
        num=8, pill="Ex 08", title="Executive Command Center", short="Executive Command Center", function="Executive",
        minutes="15 min",
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
        steps=["Fill **[Priority Folder]** (a OneDrive folder of your priority documents, or the Zava folder) and **[time]** (e.g., 8:00 AM).",
               "**New task** \u2192 paste the Executive Command Center prompt.",
               "**Side panel \u2192 Output folder \u2192 Preview** the HTML dashboard (use the Output folder workflow from Ex 1).",
               "Check the top summary, the three views, the action labels, and the links.",
               "Answer any **questions** in chat; **approve** the skill and schedule cards one at a time; skip suggested follow-ups.",
],
        watch=["Work IQ gathering calendar, mail, chats, and files",
               "Labels: Lean in \u00b7 Delegate \u00b7 Re-engage \u00b7 Protect time",
               "Focus on workstreams \u2014 not on evaluating people",
               "**Your own** work, not Zava: private to you, no screen sharing"],
        checkpoint="An HTML command center opened from the Output folder and found in OneDrive \u2192 Cowork, a "
                   "saved skill, and a weekday schedule. Pause it after class.",
        stretch="Make an HR Leader variant with a view for open requisitions and HR ticket trends.",
        notes_card="EXERCISE 8 CARD (2:15-2:30, 15 min). SAY: 'Watch one prompt gather signals, build a dashboard, save itself as a skill, and schedule itself.' APPROVAL REMINDER: review the permissions Cowork asks for (saving the skill, creating the schedule), one at a time, no Approve All. The detailed approvals slide is in the Appendix after this exercise. It combines the skills from Ex 3 and schedules from Ex 6. Read the guardrail in the prompt aloud: workstreams, not people.",
        notes_hands="EXERCISE 8 HANDS-ON. DO: show how to fill [Priority Folder] (their own priority-documents folder, or Documents/ai_hr_cowork_workshop) and [time] (e.g., 8:00 AM), then start your demo. SET EXPECTATIONS: this is the only exercise on their OWN mail, calendar, and Teams, so the dashboard shows their real work, not Zava (the dry run flagged this). Tell them what Cowork will ask: clarifying questions (answer in chat), two approval cards near the end (save the skill, create the schedule; one at a time), and suggested follow-ups when it finishes (skip for now). WATCH FOR: Work IQ gathering; the HTML file in the Output folder; in YOUR seeded demo, the Thursday conflict and T-2008 (seed-content.md). Attendees run it on their own mail, calendar, and Teams: results vary and stay private, so debrief on the pattern, never ask them to share screens; a quiet week gives a light dashboard. REVISIT step 3: use the Output folder workflow introduced in Ex 1. CLEANUP: skill stays 'Only you'; pause or delete the weekday schedule after class. NEXT: wrap-up and schedule cleanup.",
    ),
]
