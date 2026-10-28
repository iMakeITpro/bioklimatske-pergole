# Git workflow

- Work branch is `dev`. Commit and push only to `dev` (`git push origin dev`).
- `main` is the live, client-facing branch: GitHub Pages publishes it. Never push, merge or fast-forward to `origin/main` unless the user explicitly says so in the current conversation (e.g. "go to main", "release"). An earlier approval does not carry over.
- When the user asks for a release: `git push origin dev:main` (fast-forward only, `main` must be an ancestor of `dev`), then check that the Pages build is `built` and the live URL returns 200.
- Before deleting or renaming any remote branch, check the Pages config (`gh api repos/iMakeITpro/bioklimatske-pergole/pages`). Deleting the Pages source branch unpublishes the site.
- Commit only after explicit user approval, and never add Co-Authored-By lines.

## Progress tracking
- Na početku svakog razgovora pročitaj PROGRESS.md.
- Ažuriraj ga samo kad: je zadatak/feature gotov, donesena je odluka, postoji blocker ili se promijenio sljedeći korak. "Now" i "Next" prepiši, ne dodaji. "Decisions" samo nadopunjuj.
- Sitne izmjene, refaktori, typo i mali fixevi ne idu u PROGRESS.md. Kad nisi siguran, preskoči.
- Najviše ~15 redaka ukupno.
- Kad commitaš završen dio posla, u istom commitu ažuriraj PROGRESS.md (Now/Next). Ako commit ne mijenja stanje projekta (sitni fix), preskoči.
