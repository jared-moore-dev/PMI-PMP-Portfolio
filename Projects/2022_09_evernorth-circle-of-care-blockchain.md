# PMP Portfolio — Project Entry
> File: `2022_09_evernorth-circle-of-care-blockchain.md`

---

## PROJECT OVERVIEW

| Field | Value |
|---|---|
| **Project Title** | Circle of Care — Healthcare Blockchain Platform for Secure Provider Data Exchange |
| **Organization** | Evernorth Health Services (Cigna subsidiary) |
| **Your Job Title** | TECDP Intern — Enterprise Architect |
| **Functional Reporting Area** | Enterprise Architecture / Digital Health Innovation |
| **Organization Primary Focus** | Health Services / Pharmacy Benefits / Healthcare Data Exchange |
| **Approach / Methodology** | Agile — Scrum with defined sprints; Enterprise Architecture delivery model |
| **Project Team Size** | ~4 (self plus co-intern on blockchain workstream; upstream stakeholder and technical leads Jon Unger, Kirsten Reid, Hal Chernoff) |
| **Project Budget** | Nominal — internal infrastructure and tooling; no formal capital budget assigned |
| **Project Start Date** | 05/2022 |
| **Project End Date** | 05/2023 |
| **Duration (months)** | 12 (full internship tenure) |
| **Counts Toward PMP Months** | 5 months (09/2022–01/2023) — summer months allocated to My Cigna Chef (06/2022–08/2022); only non-overlapping fall/winter period credited here |

---

## PROJECT OBJECTIVE & OUTCOME

**Objective:**
Healthcare data sharing is messy — providers often lack access to the full picture, and patients have little control over who sees what. Circle of Care was built to fix that within Evernorth's ecosystem. The platform let patients grant providers time-bound access to a consolidated view of their health records, with access automatically expiring at the end of the defined window. No persistent exposure, no manual revocation required.

**Outcome:**
Delivered a working blockchain-based data exchange platform with smart contract-enforced access control. Patients could grant access, providers could view a unified record during the active window, and access expired automatically when the period ended. The solution was validated within the internship program and contributed to Evernorth's enterprise architecture strategy for secure health data interoperability.

---

## YOUR ROLE & RESPONSIBILITIES

**Role:** Technical Workstream Lead — Blockchain Architecture & Delivery

**Responsibilities:**
- Co-led the blockchain workstream with one other intern; owned the architectural decisions, implementation approach, and technical delivery within that layer
- Selected the distributed ledger approach, designed the smart contract structure, and built the data model to support time-bound, patient-controlled provider access
- Made the implementation calls — smart contract logic for access grant and automatic revocation, data storage design, integration patterns
- Facilitated technical working sessions within the workstream; kept alignment with my co-intern and made sure the codebase stayed consistent
- Business requirements and stakeholder engagement came from senior leads (Jon Unger, Kirsten Reid, Hal Chernoff); my job was to translate those into something buildable
- Participated in sprint ceremonies and presented workstream progress at sprint reviews

**Key Deliverables:**
- Blockchain platform architecture — ledger approach, data model, integration patterns
- Smart contract implementation for time-bound access control (grant, active, expired, revoked states)
- Secure healthcare data exchange layer enabling provider access to consolidated patient records
- Technical documentation supporting the enterprise architecture record

---

## PMI PROCESS GROUP COVERAGE

### Initiating (IN)
- Received business requirements from senior leads and translated the organizational need into a technical problem statement and blockchain architecture scope
- Evaluated available blockchain technologies and approaches; defined the workstream scope with my co-intern
- Identified technical stakeholders and integration dependencies within the broader Circle of Care project team

### Planning (PL)
- Designed the full blockchain architecture: ledger selection, smart contract structure, data model, access control logic, and integration approach
- Defined the smart contract state machine during planning — mapped out the grant, active, expired, and revoked states and the transition logic between them before writing a line of code
- Sequenced implementation across sprints; coordinated with my co-intern to manage parallel development tracks without blocking each other

### Executing (EX)
- Built the blockchain platform and smart contract layer; implemented time-bound access control logic with automatic expiration
- Built the data consolidation and provider access layer — unified patient records accessible to authorized providers within their active window
- Ran technical working sessions, directed implementation tasks, kept the codebase architecturally consistent
- Presented workstream progress at sprint reviews and incorporated senior lead feedback into subsequent iterations

### Monitoring & Controlling (MC)
- Tracked workstream progress against sprint commitments; surfaced blockers and technical risks to senior leads as they came up
- Validated smart contract behavior against access control requirements — specifically tested grant, expiration, and revocation logic under edge cases before each sprint review
- Kept the implementation aligned with the privacy-by-design requirements throughout; checked architectural integrity across iterations

### Closing (CL)
- Delivered the completed blockchain platform and smart contract implementation as the workstream's formal output
- Produced technical documentation for knowledge transfer and future development
- Participated in internship closeout and the enterprise architecture review of the completed solution

---

## PMI KNOWLEDGE AREA COVERAGE

| Knowledge Area | Involved? | Brief Note |
|---|---|---|
| Scope Management | Yes | Defined and managed technical workstream scope within project boundaries set by senior leads |
| Schedule Management | Yes | Planned and executed blockchain workstream delivery across Agile sprints within the internship timeline |
| Cost Management | No | No direct budget ownership; internal infrastructure managed through standard approval |
| Quality Management | Yes | Validated smart contract logic against access control requirements; tested edge cases for grant, expiration, and revocation |
| Resource Management | No | Directed implementation tasks and maintained alignment with best practices |
| Communications Management | Yes | Facilitated technical working sessions; presented progress at sprint reviews; translated business requirements into technical specs |
| Risk Management | Yes | Identified and mitigated technical risks in smart contract design, particularly around expiration edge cases and data integrity |
| Procurement Management | No | No external procurement; internal tooling managed through standard approval |
| Stakeholder Engagement | Yes | Engaged senior leads for requirements and feedback; managed technical stakeholder communication within the workstream |
| Integration Management | Yes | Integrated blockchain layer, data consolidation, provider access, and smart contract components into a single working platform |

---

## STAKEHOLDERS & GOVERNANCE

**Stakeholders:**
- **Senior Technical Leads — Jon Unger, Kirsten Reid, Hal Chernoff:** Provided business requirements, upstream decisions, and project oversight; primary audience for sprint reviews
- **Co-Intern (Blockchain Workstream):** Joint delivery partner on blockchain and smart contract implementation
- **Evernorth Enterprise Architecture Function:** Set the organizational standards and context within which the platform was designed
- **End Users (notional):** Patients wanting granular control over provider access to their records; providers needing consolidated patient data within defined access windows

**Reporting Structure:**
Reported to senior leads for requirements, feedback, and sprint reviews. Operated with significant technical autonomy within the workstream — architectural and implementation decisions were mine to make, escalated to senior leads only when business requirement clarification was needed.

**Governance:**
Business requirements and stakeholder engagement owned by senior leads. Technical architecture and implementation owned by the blockchain workstream. Sprint reviews served as the formal checkpoint for senior lead input and course correction.

---

## RISKS & ISSUES

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Smart contract logic failing on expiration edge cases | Medium | High | Designed and tested expiration and revocation logic against edge case scenarios before each sprint review |
| Blockchain approach misaligned with enterprise architecture standards | Medium | High | Validated technology selection with senior leads before committing to full implementation |
| Data model not supporting full patient record consolidation | Medium | Medium | Defined data model during planning against stated requirements; iterated based on sprint review feedback |
| Coordination gap between two co-intern developers | Low | Medium | Established clear ownership split; ran regular technical alignment sessions |

**Issues Resolved:**
- Time-bound access control in smart contracts does not have an obvious off-the-shelf pattern. I designed a custom state machine (grant → active → expired/revoked) to handle it correctly, which was the core technical challenge of the workstream.

---

## TOOLS & TECHNOLOGIES

| Category | Tools |
|---|---|
| Blockchain Platform | Distributed ledger technology; smart contract development framework |
| Smart Contracts | Time-bound access control logic; grant/expiration/revocation state machine |
| Data Architecture | Healthcare data consolidation model; provider access layer |
| Development | Enterprise architecture tooling; Evernorth internal infrastructure |
| Methodology Frameworks | Agile/Scrum sprint delivery; Enterprise Architecture design principles |

---

## LESSONS LEARNED

1. "Time-bound access" is simple to say and hard to implement correctly. The gap between a business requirement and a working smart contract is where the actual technical work lives. Getting the state machine right before writing implementation code saved significant rework.
2. Early architectural decisions constrain everything that follows. The ledger approach and smart contract design pattern I chose in sprint 1 shaped every subsequent decision. Validating those choices with senior leads before committing was worth the time.
3. Leading a workstream inside a larger project means managing in two directions at once — upward to senior leads for requirements and alignment, and laterally to my co-intern for implementation coordination. The accountability for outcomes is the same either way.

---

## PMI APPLICATION NARRATIVE

As a TECDP Enterprise Architect intern at Evernorth Health Services, I served as Technical Workstream Lead for the blockchain component of the Circle of Care initiative. The platform was designed to give patients secure, time-bound control over provider access to their health records. Patients could grant a provider access to their consolidated record for a defined period, and when that window closed, access expired automatically with no persistent data exposure beyond what the patient intended.

Working alongside a co-intern, I owned the technical architecture and implementation decisions for the blockchain layer. My first task was translating business requirements from senior leads Jon Unger, Kirsten Reid, and Hal Chernoff into a concrete architecture: selecting the distributed ledger approach, designing the data model for consolidated patient records, and defining the smart contract logic that would enforce time-bound access at the platform's core.

The central implementation challenge was the smart contract state machine. Time-bound access control does not have a standard off-the-shelf pattern, so I designed a custom one governing four states (granted, active, expired, revoked) with correct transition logic under edge case scenarios. I built and validated this iteratively across sprint cycles, presenting at sprint reviews and incorporating feedback before moving forward.

Throughout the workstream I ran technical working sessions, directed implementation tasks with my co-intern, and kept the codebase architecturally consistent across iterations. I tracked progress against sprint commitments and escalated to senior leads when business requirement clarification was needed, while keeping day-to-day technical decisions within the workstream.

The completed platform delivered smart contract-enforced time-bound access, a consolidated patient record layer, and automatic expiration. It was a functional, privacy-by-design healthcare data exchange system built to Evernorth's enterprise architecture standards.

---

## TAGS
`#pmp-portfolio` `#healthcare` `#blockchain` `#smart-contracts` `#enterprise-architecture` `#evernorth` `#cigna` `#2022` `#agile` `#data-privacy` `#health-data-exchange`

---
*Aligned to PMBOK 7th Edition & PMI PMP Examination Content Outline (ECO) 2021*