# Tanzania legal practice workflow lab

This document identifies practical service opportunities, not a survey proving how many firms experience each problem. It is grounded in the digital systems available to Tanzanian practitioners.

| Workflow | Proposed tool or service | Verification point |
|---|---|---|
| Legal research | Authority register and citation extraction | Compare full judgment, pinpoint and latest treatment |
| Litigation | Matter chronology and filing readiness checklist | Court rules, live e-CMS status and official receipt |
| Corporate work | Compliance register for returns and changes | Current legislation and BRELA portal |
| Contracts | Version register and clause review checklist | Governing law, instructions and supervising lawyer |
| Legal publishing | DOCX checks and multi-format publication | Source verification, permissions and proofread |
| Client confidentiality | Local processing and synthetic fixtures | Firm's privacy and security requirements |

## Digital source directory

- TanzLII: https://tanzlii.org/ — judgments, legislation, Gazette and practice resources.
- Attorney General legislation catalogue: https://oagmis.oag.go.tz/public — revised Acts and amendments.
- Judiciary portal: https://portal.judiciary.go.tz/ — case details, e-filing, cause lists and virtual courts.
- Judiciary library: https://emaktaba.judiciary.go.tz/ — judicial materials and Gazettes.
- BRELA Business Online Services: https://bos.brela.go.tz/ — company registration, changes and returns.

## Research opportunities

Study [eyecite](https://github.com/freelawproject/eyecite) for citation-parser design and [docassemble](https://github.com/jhpyle/docassemble) for guided document workflows. Evaluate licensing before adapting any code. Attribute upstream projects and contribute genuine fixes where appropriate. Do not copy an entire project's code or data without checking its licence and applicable source terms.

## Service model

Offer source-backed legal writing, manuscript editing, research register setup, document template preparation and workflow training. Use a synthetic matter to demonstrate the system. Avoid acting as the client firm's lawyer or making filings unless separately authorised and appropriately qualified.

## Filing-readiness record

Record the matter identifier, court, jurisdiction, proceeding, verified rule, deadline and source, responsible reviewer, documents, filing receipt and outstanding issues. Never compute or rely on a legal time limit without checking current procedural law and the court's orders.

## Confidentiality and deployment

No production client data belongs in a public repository, shared Codespace or issue. The demonstration uses fictional records. Production systems need authentication, access controls, backups and client-specific review before use.
