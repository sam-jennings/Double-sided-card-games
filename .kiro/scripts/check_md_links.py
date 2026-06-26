#!/usr/bin/env python3
"""Check internal cross-references in all Markdown files.

Validates two kinds of internal reference and reports any that point at a file
which does not exist on disk:

  1. Markdown links / images:           [text](relative/path)  ![alt](path)
  2. Kiro steering/spec file refs:      #[[file:relative/path]]

External links (http, https, mailto, tel), pure anchors (#section), and empty
targets are ignored. Anchor fragments (path#section) and URL-encoded spaces are
handled. Paths are resolved relative to the directory of the file that contains
the reference.

Exit code 0 = clean, 1 = at least one broken reference found.
"""
from __future__ import annotations

import glob
import os
import re
import sys
from urllib.parse import unquote

REPO_ROOT = os.getcwd()
MD_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FILE_REF = re.compile(r"#\[\[file:([^\]]+)\]\]")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "#", "//")


def clean_target(raw: str) -> str | None:
    """Normalise a link target, or return None if it should be skipped."""
    t = raw.strip()
    # Strip an optional markdown title:  (path "Title")
    if " " in t and (t.endswith('"') or t.endswith("'")):
        t = t.rsplit(" ", 1)[0].strip()
    # Angle-bracket form: [x](<path with spaces>)
    if t.startswith("<") and t.endswith(">"):
        t = t[1:-1].strip()
    if not t or t.startswith(SKIP_PREFIXES):
        return None
    # Drop anchor fragment, decode %20 etc.
    t = t.split("#", 1)[0]
    t = unquote(t)
    return t or None


def check_file(md_path: str) -> list[tuple[int, str]]:
    base = os.path.dirname(md_path)
    broken: list[tuple[int, str]] = []
    with open(md_path, encoding="utf-8", errors="replace") as fh:
        for lineno, line in enumerate(fh, 1):
            targets = [clean_target(m) for m in MD_LINK.findall(line)]
            targets += [clean_target(m) for m in FILE_REF.findall(line)]
            for t in targets:
                if t is None:
                    continue
                resolved = os.path.normpath(os.path.join(base, t))
                if not os.path.exists(resolved):
                    broken.append((lineno, t))
    return broken


def main() -> int:
    md_files = [
        f for f in glob.glob("**/*.md", recursive=True)
        if ".git" not in f.split(os.sep)
    ]
    total_broken = 0
    for md in sorted(md_files):
        broken = check_file(md)
        for lineno, target in broken:
            total_broken += 1
            print(f"{md}:{lineno}: broken reference -> {target}")
    if total_broken:
        print(f"\nFAIL: {total_broken} broken internal reference(s) "
              f"across {len(md_files)} markdown file(s).")
        return 1
    print(f"OK: no broken internal references in {len(md_files)} markdown file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
