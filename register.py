"""Validate a local CSV register of legal sources without deciding legal accuracy."""
import argparse
import csv
import json
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

FIELDS = ("id","jurisdiction","authority_type","citation","pinpoint","proposition","source_url","verified_on","status")
VALID_STATUS = {"pending", "verified", "conflict", "superseded"}

def check(rows):
    issues = []
    seen = set()
    for index, row in enumerate(rows, 2):
        def flag(message):
            issues.append({"row": index, "issue": message})
        for field in FIELDS:
            if field not in row:
                flag(f"missing column {field}")
        ident = (row.get("id") or "").strip()
        if not ident or ident in seen:
            flag("missing or duplicate id")
        seen.add(ident)
        status = row.get("status")
        if status not in VALID_STATUS:
            flag("invalid status")
        if status == "verified":
            for field in ("citation","pinpoint","proposition","source_url","verified_on","jurisdiction"):
                if not (row.get(field) or "").strip():
                    flag(f"verified row requires {field}")
            url = urlparse(row.get("source_url") or "")
            if url.scheme != "https" or not url.netloc:
                flag("verified row requires HTTPS source URL")
            try:
                if date.fromisoformat(row.get("verified_on") or "") > date.today():
                    flag("verification date is in the future")
            except ValueError:
                flag("invalid verification date")
    return issues

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("register", type=Path)
    args = parser.parse_args()
    with args.register.open(encoding="utf-8-sig", newline="") as source:
        issues = check(csv.DictReader(source))
    print(json.dumps(issues, indent=2))
    return bool(issues)

if __name__ == "__main__":
    raise SystemExit(main())
