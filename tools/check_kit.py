"""Check the kit: Markdown links and anchors, Word hyperlinks, and stale text.

Usage:  python tools/check_kit.py
Extra stale terms (for example, the source template's name) can be passed in the
KIT_STALE_TERMS environment variable, separated by semicolons. Exits 1 on any problem.
"""
import os
import pathlib
import re
import sys
import zipfile
from urllib.parse import unquote

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKIP_DIRS = {".build", ".git", "tools"}

STALE = [re.compile(r"Getting This Done", re.I),
         # The sample folder moved to Documents/ai_hr_cowork_workshop; only custom skills stay under Cowork.
         re.compile(r"Documents[/\\]Cowork(?![/\\]skills)")]
STALE += [re.compile(re.escape(t.strip()), re.I)
          for t in os.environ.get("KIT_STALE_TERMS", "").split(";") if t.strip()]


def kit_files(*patterns):
    for pattern in patterns:
        for p in sorted(ROOT.rglob(pattern)):
            rel = p.relative_to(ROOT)
            if not SKIP_DIRS.intersection(rel.parts) and not p.name.startswith("~$"):
                yield p


def slug(heading):
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", heading)  # links -> label
    text = re.sub(r"<[^>]+>|[*_`]", "", text).strip().lower()
    return re.sub(r"[^\w\- ]", "", text).replace(" ", "-")


def anchors(md_path, cache={}):
    if md_path not in cache:
        found, seen, in_code = set(), {}, False
        for line in md_path.read_text(encoding="utf-8").splitlines():
            if line.lstrip().startswith("```"):
                in_code = not in_code
            if in_code:
                continue
            m = re.match(r"#{1,6}\s+(.+?)\s*#*\s*$", line)
            if m:
                base = slug(m.group(1))
                n = seen.get(base, 0)
                seen[base] = n + 1
                found.add(base if n == 0 else f"{base}-{n}")
            found.update(re.findall(r"<a\s+(?:id|name)=\"([^\"]+)\"", line))
        cache[md_path] = found
    return cache[md_path]


def strip_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def check_markdown(problems):
    count = 0
    for md in kit_files("*.md"):
        text = strip_code(md.read_text(encoding="utf-8"))
        for target in re.findall(r"\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)", text):
            if re.match(r"[a-z]+:", target, re.I):
                continue
            count += 1
            path, _, anchor = unquote(target).partition("#")
            dest = (md.parent / path).resolve() if path else md
            where = f"{md.relative_to(ROOT)} -> {target}"
            if not dest.exists():
                problems.append(f"missing link target: {where}")
            elif anchor and dest.suffix == ".md" and anchor.lower() not in anchors(dest):
                problems.append(f"missing anchor: {where}")
    return count


def check_docx(problems):
    count = 0
    for doc in kit_files("*.docx"):
        with zipfile.ZipFile(doc) as z:
            rels = z.read("word/_rels/document.xml.rels").decode("utf-8")
        for target in re.findall(r'Target="([^"]+)"[^>]*TargetMode="External"', rels):
            if re.match(r"[a-z]+:", target, re.I):
                continue
            count += 1
            if not (doc.parent / unquote(target.partition("#")[0])).resolve().exists():
                problems.append(f"missing Word link target: {doc.relative_to(ROOT)} -> {target}")
    return count


def check_stale(problems):
    count = 0
    for f in kit_files("*.md", "*.docx", "*.pptx", "*.xlsx"):
        if f.suffix == ".md":
            texts = {"": f.read_text(encoding="utf-8")}
        else:
            with zipfile.ZipFile(f) as z:
                texts = {n: z.read(n).decode("utf-8", "replace") for n in z.namelist()
                         if n.endswith((".xml", ".rels"))}
        count += 1
        for part, text in texts.items():
            for rx in STALE:
                for m in rx.finditer(text):
                    problems.append(f"stale text {m.group(0)!r}: {f.relative_to(ROOT)} {part}".rstrip())
    return count


def main():
    problems = []
    n_md = check_markdown(problems)
    n_docx = check_docx(problems)
    n_files = check_stale(problems)
    print(f"checked {n_md} Markdown links, {n_docx} Word links, {n_files} files for stale text "
          f"({len(STALE)} patterns)")
    for p in problems:
        print("  " + p)
    print("OK" if not problems else f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
