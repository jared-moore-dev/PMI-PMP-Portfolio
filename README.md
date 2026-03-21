# PMP Project Management Portfolio

This repository documents my project management experience as part of my application for the **Project Management Professional (PMP)** certification through PMI. Each entry maps to PMBOK 7th Edition terminology and the 2021 PMP Examination Content Outline.

---

## Background

I have a 4-year degree, so PMI requires 36 non-overlapping months of project leadership experience within the last 8 years. The six projects here get me there across healthcare, AI, and marketing — spanning roles from Project Manager and Product Owner to technical lead and program-level governance.

Each project file has everything PMI wants to see: the standard application fields, process group and knowledge area coverage, a stakeholder map, a risk register, tools used, lessons learned, and a 200-500 word narrative written for the application itself.

---

## Experience Summary

| # | Project | Organization | Role | Methodology | Dates | Months |
|---|---|---|---|---|---|---|
| 1 | [My Cigna Chef — Healthy Eating Rewards App](/Projects/2022_06_cigna-my-cigna-chef.md) | Cigna | Project Manager | Agile / Scrum | 06/2022 – 08/2022 | 3 |
| 2 | [Circle of Care — Healthcare Blockchain Platform](/Projects/2022_09_evernorth-circle-of-care-blockchain.md) | Evernorth Health Services | Technical Workstream Lead | Agile / Scrum | 09/2022 – 01/2023 | 5 |
| 3 | [Droogle — Drug Research & Contracting Intelligence](/Projects/2023_06_cigna-droogle-drug-research-platform.md) | Cigna | Product Owner | Agile / Scrum | 06/2023 – 08/2023 | 3 |
| 4 | [AI Vendor Evaluation Program — Cigna Ventures](/Projects/2024_01_cigna-ventures-vendor-vetting.md) | Cigna / Cigna Ventures | Technical Due Diligence Lead | Structured Evaluation | 01/2024 – 07/2024 | 7 |
| 5 | [MDLive Virtual Care AI Automation](/Projects/2024_08_cigna-mdlive-virtual-care-ai-automation.md) | Cigna | Technical Project Lead | Hybrid Agile / Compliance-Gated | 08/2024 – 03/2025 | 8 |
| 6 | [Enterprise AI Enablement Program](/Projects/2025_04_cigna-ai-enablement-program.md) | Cigna | AI Enablement Engineer | Program Management | 04/2025 – 03/2026 | 12 |
| | | | | | **Total** | **38** |

---

## Project Timeline

![PMP Portfolio Timeline](./timeline.png)

*No two projects overlap. All experience falls within the 8-year PMI eligibility window (March 2018 – March 2026).*

---

## Domain and Methodology Coverage

| | Healthcare IT | Healthcare Analytics | Healthcare Data | AI Governance | Clinical AI | Ventures / Procurement |
|---|---|---|---|---|---|---|
| **Agile / Scrum** | My Cigna Chef | Droogle | Circle of Care | | | |
| **Hybrid** | | | | | MDLive | |
| **Structured Evaluation** | | | | | | Vendor Vetting |
| **Program Management** | | | | AI Enablement | | |

---

## PMI Process Group Coverage

All five PMBOK process groups are represented in every project entry.

| Process Group | Coverage |
|---|---|
| Initiating (IN) | All 6 projects |
| Planning (PL) | All 6 projects |
| Executing (EX) | All 6 projects |
| Monitoring & Controlling (MC) | All 6 projects |
| Closing (CL) | All 6 projects |

---

## Projects

### 1. My Cigna Chef
**[View full project file](/Projects/2022_06_cigna-my-cigna-chef.md)**

| Field | Detail |
|---|---|
| Organization | Cigna |
| Role | Project Manager |
| Dates | 06/2022 – 08/2022 |
| Budget | Nominal (internal tools / AWS via approval) |
| Team Size | 11 |
| Methodology | Agile / Scrum, 3 sprints |

Part of Cigna's Summer Innovation Program. The ask was to find a way to encourage healthier eating in insured populations. Our team of 11 interns built a recipe sharing app that let users set personal health goals, earn points for hitting them, and apply those points toward lower premiums. I ran the project: organized the team into workstreams, set up our Agile ceremonies, managed the backlog, and led the final presentation to Cigna executives.

The tricky part was defining what "healthy" actually meant for a diverse user base. We solved it by letting users define their own goals and building pre-approved reward tracks around those, rather than forcing a one-size-fits-all approach.

**Outcome:** Shipped a working full-stack app with Okta auth, a payment processor integration, and a custom REST API in 11 weeks.

---

### 2. Circle of Care
**[View full project file](/Projects/2022_09_evernorth-circle-of-care-blockchain.md)**

| Field | Detail |
|---|---|
| Organization | Evernorth Health Services |
| Role | Technical Workstream Lead |
| Dates | 09/2022 – 01/2023 |
| Budget | Nominal (internal infrastructure) |
| Team Size | ~4 |
| Methodology | Agile / Scrum |

A blockchain platform that gave patients control over who could see their health records and for how long. The idea was simple: you grant a provider access, they get a window to view your consolidated record, and when that window closes, so does their access automatically. No persistent exposure, no manual revocation required.

I led the blockchain workstream, which meant owning the architecture and the implementation. I designed the smart contract logic that handled the full access lifecycle: grant, active, expired, revoked. Business requirements came from senior leads; how we built it was mine to figure out.

**Outcome:** A working POC privacy-by-design health data exchange platform, built to Evernorth's enterprise architecture standards.

---

### 3. Droogle
**[View full project file](/Projects/2023_06_cigna-droogle-drug-research-platform.md)**

| Field | Detail |
|---|---|
| Organization | Cigna |
| Role | Product Owner |
| Dates | 06/2023 – 08/2023 |
| Budget | Nominal (internal tools / AWS via approval) |
| Team Size | ~10 |
| Methodology | Agile / Scrum, 3 sprints |

Cigna's contracting teams negotiate with drug manufacturers, and they were going in without great visibility into what competitors were paying. Droogle was a drug research and discovery platform that pulled public pricing data, modeled competitor discounts for biosimilars, and surfaced it all in a dashboard so our teams had real leverage at the table.

As Product Owner, my job was to stay close to the contracting stakeholders, understand what they actually needed (not just what they asked for), and make sure the dev team was building toward that. One of the bigger challenges was data: early on we realized the public sources we planned to use were not as clean or accessible as expected. Catching that early and resetting expectations before we were deep in build saved us significant rework.

**Outcome:** Won our prompt category at the 2023 TECDP Summer Innovation Presentations. Our application was used as the basis for a current solution which is running in production environments today.

---

### 4. AI Vendor Evaluation Program
**[View full project file](/Projects/2024_01_cigna-ventures-vendor-vetting.md)**

| Field | Detail |
|---|---|
| Organization | Cigna / Cigna Ventures |
| Role | Technical Due Diligence Lead |
| Dates | 01/2024 – 07/2024 |
| Budget | N/A (supported Ventures investment decisions) |
| Team Size | 3 |
| Methodology | Structured multi-gate evaluation framework |

Cigna Ventures was evaluating AI vendors for potential investment or partnership, and they needed someone who could actually stand the products up and test them, not just sit through demos. I was that person. For each vendor, I would deploy their product in our environment, run it against real scenarios, review their data handling and security practices, and assess whether what they claimed matched what the product actually did.

A fair number did not hold up. That was the point of the work.

**Outcome:** Delivered technical assessments with clear go/no-go recommendations, grounded in evidence rather than vendor pitch decks.

---

### 5. MDLive Virtual Care AI Automation
**[View full project file](/Projects/2024_08_cigna-mdlive-virtual-care-ai-automation.md)**

| Field | Detail |
|---|---|
| Organization | Cigna |
| Role | Technical Project Lead / Lead Developer |
| Dates | 08/2024 – 03/2025 |
| Budget | $500K – $1M (estimated) |
| Team Size | 4 |
| Methodology | Hybrid Agile / Compliance-Gated |

This one started with an investor call. Cigna's CIO referenced MDLive as having AI-powered SOAP note generation and automated physician quality review. The problem: it did not. What existed was a basic NLP transcription tool that produced summaries. I was brought in to build what had been described, fast.

I started as the sole developer, scoping the architecture and building the initial system from the ground up: a dynamic prompt pipeline that pulled in patient context (demographics, history, visit type), structured clinical SOAP notes, and automated quality review flags that checked for things like allergy screenings and pregnancy questions based on patient profile. Everything was built with human-in-the-loop compliance requirements and documented escalation paths for when the model got something wrong.

Once we hit MVP, two HIH engineers joined and we set up a proper Dev/Prod pipeline where I built and tested on the dev side and they handled production deployments after automated validation. We ran through four model generations (GPT-3.5, 4, 4o, o1) without any prolonged production outages. I eventually transitioned the system to a permanent HIH team in Hyderabad and spent six months advising during handoff.

**Outcomes:**
- 400+ physicians onboarded; now the default workflow for all MDLive consults
- 10,000+ consults processed in the first year
- Replaced a quarterly manual review process (200+ transcripts, low accuracy, expensive licensed resource time)
- Estimated **$600,000+ in business savings**
- Zero production incidents across four LLM generations

---

### 6. Enterprise AI Enablement Program
**[View full project file](/Projects/2025_04_cigna-ai-enablement-program.md)**

| Field | Detail |
|---|---|
| Organization | Cigna |
| Role | AI Enablement Engineer |
| Dates | 04/2025 – 03/2026 |
| Budget | N/A (enterprise risk mitigation program) |
| Team Size | 4 (covering 400+ projects enterprise-wide) |
| Methodology | Program Management / Hybrid compliance-gated |

Every AI solution that ships at Cigna has to pass through a governance pipeline before it goes to production. My job is to run that pipeline for my portion of the portfolio. That means kickoff calls with product teams, architecture reviews, vendor safety questionnaire coordination for anything with an external AI dependency, evidence review across end-to-end testing, safety and fairness, bias, adversarial, and load testing, and ultimately the production sign-off decision.

I have formal approval authority. Nothing in my portfolio goes to production without my sign-off, and everything that gets approved has a complete audit trail behind it in case something goes wrong down the road.

Over the last year I have managed about 130 of these across a 4-person team covering 400+ projects total. The work also started running into a gap in the existing framework: agentic AI does not fit neatly into the governance model built for traditional ML. I have been part of the team effort to adapt the framework to cover those cases.

**Outcomes:**
- 130+ AI projects approved through personal portfolio
- Complete audit trail maintained on all approvals
- Contributed to governance framework updates for agentic AI architectures

---

## Certifications

| Certification | Issuer | Status |
|---|---|---|
| PMP | PMI | In progress |
| CPMAI | PMI | Complete |

---

*Project details reflect my direct experience and leadership contributions. Proprietary and confidential information has been omitted or generalized.*

*Aligned to PMBOK 7th Edition and the PMI PMP Examination Content Outline (ECO) 2021.*