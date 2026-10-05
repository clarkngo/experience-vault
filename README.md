# experience-vault

Interview story library in STAR format. Live site: https://clarkngo.github.io/experience-vault/

- `stories/*.json`: one story per file (title, category, tags, relatedProject, situation, task, action, result)
- `stories.json`: combined index used by the site; rebuild with `python3 scripts/build_index.py`
- Text marked `[confirm: ...]` is a draft detail still to be verified; the site highlights it.
