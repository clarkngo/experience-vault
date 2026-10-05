"""Combine stories/*.json into stories.json for bulk import. Run: python3 scripts/build_index.py"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ["title", "category", "tags", "relatedProject", "situation", "task", "action", "result"]
CATEGORIES = {"Behavioral", "Technical", "System Design", "Leadership"}

stories = []
for path in sorted((ROOT / "stories").glob("*.json")):
    story = json.loads(path.read_text())
    missing = [k for k in REQUIRED if k not in story]
    if missing:
        raise SystemExit(f"{path.name}: missing {missing}")
    if story["category"] not in CATEGORIES:
        raise SystemExit(f"{path.name}: bad category {story['category']!r}")
    stories.append({"id": path.stem, **story})

(ROOT / "stories.json").write_text(json.dumps(stories, indent=2, ensure_ascii=False) + "\n")

unconfirmed = [s["id"] for s in stories if "[confirm:" in json.dumps(s)]
print(f"{len(stories)} stories -> stories.json ({len(unconfirmed)} still have [confirm: ...] markers)")
