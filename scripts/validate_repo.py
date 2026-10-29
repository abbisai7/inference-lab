"""Read-only foundation checks; not proof of runtime correctness or evidence truth."""
import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

LEGACY_RECORDS = {"0001-documentation-foundation.md", "0002-unified-change-workflow.md"}
REQUIRED = ["README.md", "AGENTS.md", "GOALS.md", "PLANS.md", "CHANGELOG.md",
            "docs/workflow.md", "docs/orchestration.md", "docs/skills.md",
            "harness/build/README.md", "harness/build/template.md", "harness/build-log.md",
            "harness/context/README.md", "harness/code_review/README.md"]
SKILLS = ["harness-author", "change-delivery", "workflow-retrospective"]


def prose(text):
    """Ignore fenced examples when checking links and completion statements."""
    result, marker = [], None
    for line in text.splitlines():
        fence = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if fence:
            token, rest = fence.groups()
            if marker is None:
                marker = token
            elif token[0] == marker[0] and len(token) >= len(marker) and not rest.strip():
                marker = None
            continue
        if marker is None:
            result.append(line)
    return "\n".join(result)


def check_record(path):
    """Check named requirements/coverage and conservative completion consistency."""
    text = prose(path.read_text())
    errors = []
    status = re.search(r"^Status: (.+)$", text, re.M)
    if not status or status.group(1).strip() not in {"Draft", "Ready", "In progress", "Complete", "Superseded"}:
        errors.append("missing or unsupported record Status")
    for heading in ["Summary", "Requirements and acceptance criteria", "Implementation plan", "Validation and coverage", "Operational impact", "Results and learning"]:
        if not re.search(r"^## " + re.escape(heading) + r"\s*$", text, re.M):
            errors.append("missing section: " + heading)
    definitions = re.findall(r"^\s*(?:[-*+]|\d+[.)])\s+(R\d+) — ([^:\n]+):?[^\n]*$", text, re.M)
    ids = [key for key, _ in definitions]
    if not ids:
        errors.append("no named requirement definitions (use '- R1 — Meaningful name: behavior')")
    if len(ids) != len(set(ids)):
        errors.append("duplicate requirement ID")
    coverage = {}
    for line in text.splitlines():
        if not re.match(r"^\| R\d+ — ", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 4:
            errors.append("coverage row must have four columns")
            continue
        key = cells[0].split(" — ", 1)[0]
        if key in coverage:
            errors.append("duplicate coverage row: " + key)
        coverage[key] = cells
        if cells[3] not in {"Pending", "Implemented", "Verified", "Blocked"}:
            errors.append("unsupported coverage status: " + key)
    if set(ids) != set(coverage):
        errors.append("requirement definitions and coverage rows must match")
    if status and status.group(1).strip() == "Complete":
        if re.search(r"^\s*(?:[-*+]|\d+[.)])\s+\[ \]", text, re.M):
            errors.append("Complete record contains unfinished steps")
        for key, cells in coverage.items():
            if cells[3] != "Verified":
                errors.append("Complete record has unverified requirement: " + key)
            for value in cells[1:3]:
                if value.lower().strip(".") in {"", "pending", "tbd", "todo", "none", "not implemented", "no checks run"}:
                    errors.append("Complete record lacks implementation/evidence: " + key)
    return errors


def validate(root):
    root = Path(root).resolve()
    errors, notes = [], []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append("missing required file: " + name)
    if (root / "PROMPTS.md").exists():
        errors.append("PROMPTS.md is superseded by repo skills")
    for name in SKILLS:
        folder = root / ".agents/skills" / name
        if not (folder / "SKILL.md").is_file() or not (folder / "agents/openai.yaml").is_file():
            errors.append("missing skill files: " + name)
    roots = [root / "docs", root / "harness", root / ".agents/skills"]
    markdown = list(root.glob("*.md"))
    for folder in roots:
        markdown.extend(folder.rglob("*.md"))
    links = 0
    for path in markdown:
        if not path.resolve().is_relative_to(root):
            errors.append("Markdown symlink escapes repository: " + str(path.relative_to(root)))
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", prose(path.read_text())):
            target = target.strip().strip("<>")
            parts = urlsplit(target)
            if parts.scheme or target.startswith("#"):
                continue
            links += 1
            destination = (path.parent / unquote(parts.path)).resolve()
            if not destination.is_relative_to(root):
                errors.append(str(path.relative_to(root)) + ": link escapes repository: " + target)
            elif not destination.exists():
                errors.append(str(path.relative_to(root)) + ": broken link: " + target)
    for record in sorted((root / "harness/build").glob("*.md")):
        if record.name in {"README.md", "template.md"}:
            continue
        if record.name in LEGACY_RECORDS:
            notes.append("Historical record: completion schema not retroactively enforced: " + record.name)
            continue
        errors.extend(str(record.relative_to(root)) + ": " + e for e in check_record(record))
    return {"ok": not errors, "markdown_files": len(markdown), "local_file_links": links,
            "errors": errors, "notes": notes,
            "limits": "Checks inline file links (not anchors/reference-style links), required files and named coverage structure. Does not prove evidence truth, test quality, skill routing, index status synchronization, or runtime behavior. Historical records retain their original schema."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = validate(args.root)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(("PASS" if result["ok"] else "FAIL") + ": %s Markdown files, %s local file links" % (result["markdown_files"], result["local_file_links"]))
        for item in result["errors"] + result["notes"]:
            print(item)
        print(result["limits"])
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
