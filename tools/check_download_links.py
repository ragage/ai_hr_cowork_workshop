r"""Check the GitHub download links in the decks, the workbook, and the invitation emails.

For every link to the kit repo it checks that the file exists in this working copy and on the
published branch (origin/main by default), and warns when the published copy is older. With
--online it also opens each link anonymously, the way an attendee without repo access would.
Exit code 1 if any link is broken.

    .venv\Scripts\python tools\check_download_links.py [--online] [--ref origin/main]
"""
import argparse
import os
import pathlib
import re
import subprocess
import sys
import urllib.request
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO = os.environ.get("KIT_REPO", "https://github.com/cragage_microsoft/ai_hr_cowork_workshop").rstrip("/")
SOURCES = [
    "instructor/instructor-deck.pptx",
    "communication/training-overview.pptx",
    "communication/participant-email.html",
    "communication/instructor-email.html",
    "participant/participant-workbook.md",
    "participant/participant-workbook.docx",
    "participant/quick-reference-card.docx",
]


def text_of(path):
    if path.suffix in (".pptx", ".docx"):
        with zipfile.ZipFile(path) as z:
            return " ".join(z.read(n).decode("utf-8", "ignore") for n in z.namelist()
                            if n.endswith((".xml", ".rels")))
    return path.read_text(encoding="utf-8")


def find_links():
    """Return {url: [source files]} for every link into the kit repo."""
    pattern = re.compile(re.escape(REPO) + r"[^\s\"'<>)\]]*")
    links = {}
    for rel in SOURCES:
        for url in pattern.findall(text_of(ROOT / rel)):
            url = url.replace("&amp;", "&").rstrip(".,;")
            links.setdefault(url, []).append(rel)
    return links


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def check_repo(url, ref):
    """Return (status, note) for the file a link points to."""
    m = re.match(r"/(raw|blob|tree)/[^/]+/(.+)", url[len(REPO):])
    if not m:
        return "ok", "repo home page"
    path = m.group(2).split("?")[0].split("#")[0]
    if not (ROOT / path).exists():
        return "BROKEN", f"{path} is missing from this working copy"
    kind = git("cat-file", "-t", f"{ref}:{path}").stdout.strip()
    if not kind:
        return "BROKEN", f"{path} is not on {ref} yet (merge and push this branch)"
    if kind == "blob" and git("diff", "--quiet", ref, "--", path).returncode:
        return "warn", f"{ref} has an older copy of {path} (merge and push to update it)"
    return "ok", path


def check_online(url):
    """Open the link with no GitHub sign-in, as an attendee would."""
    req = urllib.request.Request(url, headers={"User-Agent": "kit-link-check"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            final, head = r.geturl(), r.read(4096)
    except Exception as e:  # report any network error as a failure
        return f"error: {e}"
    if "/sso" in final or "/login" in final or b"Sign in" in head:
        return "needs a GitHub sign-in"
    if "/raw/" in url and url.endswith((".docx", ".pptx", ".xlsx", ".zip")) and not head.startswith(b"PK"):
        return "not a file download"
    return "ok"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--ref", default="origin/main", help="published branch to compare with")
    ap.add_argument("--online", action="store_true", help="also open each link without signing in")
    args = ap.parse_args()
    git("fetch", "--quiet", "origin")
    links = find_links()
    broken = 0
    for url, where in sorted(links.items()):
        status, note = check_repo(url, args.ref)
        broken += status == "BROKEN"
        line = f"{status:6} {url[len(REPO):] or '/'}  ({note}; in {', '.join(sorted(set(where)))})"
        if args.online:
            line += f"  [online: {check_online(url)}]"
        print(line)
    print(f"{len(links)} links, {broken} broken")
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    main()
