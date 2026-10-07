#!/usr/bin/env python
"""Build the training overview deck (communication/training-overview.pptx).

A short deck for HR leaders, managers, and prospective attendees: what the training is, who it's for, the
agenda and exercises, what to prepare, and download links. It reuses build_deck.py's template, helpers, and
the shared slides (agenda, objectives, workshop-kit links) so the two decks never drift apart.
"""
import os

_SRC = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_deck.py"), encoding="utf-8").read()
_HEAD, _, _REST = _SRC.partition("# 1 \u2014 Title\n")
_, _, _TAIL = _REST.partition("# ---------------------------------------------------------------- remove template slides")
exec(compile(_HEAD, "build_deck.py", "exec"))

OUT = os.environ.get("OVERVIEW_OUT", os.path.join(ROOT, "communication", "training-overview.pptx"))
DECK_SUBJECT = "Training overview"

# 1 — Title
mark_section("Overview")
s = title_slide("Getting Things Done with Copilot Cowork for HR Tasks",
                "Training overview \u00b7 a 2\u00bd-hour, hands-on workshop for HR teams", title_size=40,
                lines=["Getting Things Done with Copilot Cowork", "for HR Tasks"])
notes(s, "TRAINING OVERVIEW. Use this short deck to introduce the workshop to HR leaders, managers, and people "
         "thinking about attending. The instructor deck (instructor/instructor-deck.pptx) is what's presented on "
         "the day.")

# 2 — About the training
s = white_slide("About the training", "Hands-on practice with Microsoft Copilot Cowork on everyday HR work. No code required.")
wcard(s, 0.55, 1.6, 3.95, 3.35, BLUE, "WHO IT\u2019S FOR",
      bullets(["HR practitioners doing day-to-day operations", "No-code and beginner-friendly",
               "About **25 attendees** per session"], size=15))
wcard(s, 4.69, 1.6, 3.95, 3.35, PURPLE, "FORMAT",
      bullets(["**2\u00bd hours**, instructor-led and hands-on", "**Eight** scenario-based exercises, one 15-minute break",
               "Your **own work account**: your real calendar and mail for Ex 1, fictional Zava files for the rest"], size=15))
wcard(s, 8.83, 1.6, 3.95, 3.35, GREEN, "THREE TOOLS",
      bullets(["**Copilot Chat** for quick answers", "**Cowork** for multi-step work that ends in a deliverable",
               "**Agent Builder** for a reusable helper others can use"], size=15))
band(s, 0.55, 5.25, 12.23, 1.5,
     "**One habit all day: draft \u2192 review \u2192 approve.** Cowork pauses before it sends or shares anything, "
     "so HR stays accountable for every output.", fill=PLUM, color="FFFFFF", size=16)
notes(s, "ABOUT. Who it's for, the format, and the three tools. Attendees use their own work accounts: Exercise 1 "
         "builds a private dashboard from their own mail and calendar, and every other exercise uses fictional Zava "
         "sample files. Everything Cowork produces is a draft to review.")

# 3 — Learning objectives
s = objectives_slide()
notes(s, "LEARNING OBJECTIVES. The six outcomes attendees leave with. They mirror the README and the participant "
         "workbook, and the workshop closes with a quick knowledge check against them.")

# 4 — Agenda
s = agenda_slide()
notes(s, "AGENDA. Two and a half hours: framing and a UI tour with setup, then eight hands-on exercises with one 15-minute break. "
         "Exercise 4 (a custom skill) is the centerpiece; Exercise 8 builds a no-code agent in Agent Builder.")

# 5 — The eight exercises
s = white_slide("Eight hands-on exercises", "Each one starts from a real HR scenario and ends in a finished draft.")
for i, ex in enumerate(EXERCISES):
    x, y = 0.55 + (i % 4) * 3.1, 1.6 + (i // 4) * 2.6
    acc = (BLUE, PURPLE, GREEN, RED)[i % 4]
    box(s, x, y, 2.93, 2.42, "FFFFFF", line=W_LINE, shadow=True)
    box(s, x, y, 2.93, 0.045, acc)
    art = os.path.join(os.path.dirname(os.path.abspath(__file__)), "art", f"ex{ex['num']}.png")
    if os.path.exists(art):
        pic = s.shapes.add_picture(art, Inches(x + 2.18), Inches(y + 0.18), width=Inches(0.58))
        pic.name = f"Picture Exercise {ex['num']}"
        pic._element.nvPicPr.cNvPr.set("descr", DIVIDER_ALT.get(ex["num"], ex["title"]))
    text(s, x + 0.16, y + 0.16, 1.9, 0.3, [{"runs": [(f"EXERCISE {ex['num']} \u00b7 {ex['minutes'].upper()}",
                                                     {"size": 10, "bold": True, "color": acc})]}])
    text(s, x + 0.16, y + 0.46, 2.0, 0.6, [{"runs": [(ex["short"], {"size": 14, "bold": True, "color": W_TITLE})]}],
         line_spacing=0.95)
    text(s, x + 0.16, y + 1.05, 2.62, 1.3, [{"runs": rich(ex["goal"], 10.5, W_SUB)}], line_spacing=1.0)
notes(s, "EXERCISES. Walk the eight scenarios: an executive command center, Deep Research, Cowork driving a "
         "browser, a custom skill, recruiting and reporting, an onboarding pack, automations, and a policy agent. "
         "Each one ends in a draft the attendee reviews.")

# 6 — Before the session
s = white_slide("Before the session", "What attendees bring, and what the host sets up in advance.")
wcard(s, 0.55, 1.6, 5.98, 3.45, BLUE, "FOR ATTENDEES",
      bullets(["A **laptop or desktop** (not a phone) with **Microsoft Edge** 152 or later",
               "Your **own work account** (Microsoft 365 Copilot licensed)",
               "No prep needed; optional five-minute pre-read: **Copilot vs. Cowork**",
               "Real data stays private; exercise files are fictional"], size=15))
wcard(s, 6.8, 1.6, 5.98, 3.45, PURPLE, "FOR HOSTS (START 3 WEEKS OUT)",
      bullets(["**Microsoft 365 Copilot** licenses and usage-based billing",
               "A **Cowork spending policy** (grants access) with **Cowork Browsing** allowed",
               "Attendees in the workshop group, plus 1\u20132 spare accounts",
               "Follow the **readiness checklist** for the full timeline and Plan B"], size=15))
band(s, 0.55, 5.3, 12.23, 1.45,
     "**Instructors:** start with the readiness checklist and the facilitator guide, then do a full dry run against "
     "the answer key. The instructor deck\u2019s speaker notes carry the run sheet.", size=15)
notes(s, "BEFORE THE SESSION. Attendees need only a laptop with Edge and their own work account; nothing to provision. Hosts set up "
         "licenses, the Cowork spending policy, and browser access; the facilitator seeds only their own demo account. The readiness checklist has the "
         "timeline, cost planning, and Plan B.")

# 7 — Download links
mark_section("Workshop kit")
s = kit_links_slide()
notes(s, "DOWNLOAD LINKS. Everything participants and instructors need; the Zava sample data is one zip. The links "
         "point to the kit's private GitHub repo: give people access, or post the files in a shared Teams/SharePoint "
         "folder and share that link instead.")

# 8 — Close
s = title_slide("Ready to join?", "Ask your workshop host for the next session date.")
notes(s, "CLOSE. Invite questions. The paste-ready invitation emails in communication/ carry the same links.")

exec(compile("# ---------------------------------------------------------------- remove template slides" + _TAIL,
             "build_deck.py", "exec"))
