# Legal Research Register

A local CSV validator and Tanzanian legal research workflow for recording authorities, pinpoints, legal propositions and manual verification dates.

```sh
python register.py example.csv
python -m unittest -v
```

A row marked verified must contain the jurisdiction, citation, pinpoint, proposition, HTTPS source and verification date. This is a completeness check, not independent proof of legal accuracy.

Read [the Tanzanian legal writing and verification skill](skills/tanzanian-legal-research/SKILL.md). It draws on the editorial methods of *Commercial Law in Tanzania* without reproducing the book.

Never add client files or live case details. Use synthetic examples.

MIT licence for software.