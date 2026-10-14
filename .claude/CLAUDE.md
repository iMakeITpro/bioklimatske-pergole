# Git workflow

- Work branch is `dev`. Commit and push only to `dev` (`git push origin dev`).
- `main` is the live, client-facing branch: GitHub Pages publishes it. Never push, merge or fast-forward to `origin/main` unless the user explicitly says so in the current conversation (e.g. "go to main", "release"). An earlier approval does not carry over.
- When the user asks for a release: `git push origin dev:main` (fast-forward only, `main` must be an ancestor of `dev`), then check that the Pages build is `built` and the live URL returns 200.
- Before deleting or renaming any remote branch, check the Pages config (`gh api repos/iMakeITpro/bioklimatske-pergole/pages`). Deleting the Pages source branch unpublishes the site.
- Commit only after explicit user approval, and never add Co-Authored-By lines.
