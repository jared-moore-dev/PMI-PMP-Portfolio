# PMP Portfolio — Project Entry
> File: `2025_04_cigna-mdlive-bh-psychiatry-billing.md`
---

## PROJECT OVERVIEW

| Field                          | Value                                                                                                                                       |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Project Title**              | MDLive Behavioral Health Psychiatry Billing Categorization — Automated MDM-Based Consult Coding                                              |
| **Organization**               | Cigna                                                                                                                                       |
| **Your Job Title**             | Engineering Project Management Lead                                                                                                          |
| **Functional Reporting Area**  | AI Center of Excellence / Digital Health                                                                                                     |
| **Organization Primary Focus** | Health Insurance / Virtual Behavioral Health / Clinical AI                                                                                   |
| **Approach / Methodology**     | Hybrid, iterative POC development followed by compliance-gated production rollout                                                            |
| **Project Team Size**          | 3 (self as project lead plus two engineers, with clinical and billing stakeholders)                                                         |
| **Project Budget**             | Internal labor and AI gateway consumption; no discrete capital budget                                                                        |
| **Project Start Date**         | 04/2025                                                                                                                                      |
| **Project End Date**           | 08/2025                                                                                                                                      |
| **Duration (months)**          | 5                                                                                                                                            |
| **Counts Toward PMP Months**   | Yes, 5 months (no overlap with other documented projects)                                                                                    |

---

## PROJECT OBJECTIVE & OUTCOME

**Objective:** MDLive's behavioral health psychiatry consults were being billed through a manual coding process. Correct billing under Medical Decision Making (MDM) standards depends on factors like the complexity of the patient's history and the time spent in the consult, and getting it wrong creates both compliance and revenue risk. The objective was to build a system that could categorize a psychiatry consult to the correct MDM-based billing level automatically. A key constraint shaped the whole design: unlike the earlier virtual care work, this system could not use the consult transcript. It had to reach the right billing category from metadata alone, specifically the patient's prior history and the time spent in the meeting.

**Outcome:** Delivered a working backend categorization system, validated as a pilot and then rolled out to physicians. Key results:

- Automated MDM-based billing categorization for behavioral health psychiatry consults using only prior history and consult duration, with no reliance on transcript content
- Validated the approach as a POC before any production exposure, then rolled out to the physician base
- Backend-only footprint made the rollout cleaner and lower-risk than transcript-dependent systems
- Reduced manual billing-coding effort and the associated risk of miscategorization under MDM standards
- Built within the same human-in-the-loop and compliance expectations as other clinical AI at Cigna

---

## YOUR ROLE & RESPONSIBILITIES

**Role:** Engineering Project Management Lead

**Responsibilities:**

- Led the project end to end, from POC scoping through pilot validation and physician rollout
- Defined the core technical constraint with stakeholders, that categorization had to work from prior history and consult time without the transcript, and scoped the solution around it
- Coordinated a three-person team building the categorization logic against MDM billing standards
- Worked with clinical and billing stakeholders to confirm the categorization logic matched real MDM coding rules
- Ran the pilot, reviewed results against expected billing categories, and managed the move from POC to production
- Managed the physician rollout once the backend system was validated
- Inventoried risks and confirmed stakeholder sign-off before the system went live

**Key Deliverables:**

- POC categorization system mapping consults to MDM billing levels from metadata
- Validation results comparing system output against correct billing categories
- Production-ready backend categorization service
- Physician rollout and supporting documentation
- Risk inventory and stakeholder sign-off prior to go-live

---

## PMI PROCESS GROUP COVERAGE

### Initiating (IN)

- Defined the problem and its hard constraint with billing and clinical stakeholders, that the system had to categorize consults without access to the transcript
- Confirmed scope as a single deliverable: an MDM-based billing categorization system for behavioral health psychiatry consults
- Identified stakeholders, including the engineering team, billing function, and the MDLive physician base who would use the output

### Planning (PL)

- Planned a POC-first approach to prove the metadata-only categorization was viable before committing to production
- Mapped the MDM billing standards the system had to satisfy and planned the categorization logic around prior history and consult time
- Planned the validation method, comparing system output against known-correct billing categories
- Planned the production rollout, scoped as a backend change to keep the footprint simple

### Executing (EX)

- Built the POC with the three-person team, implementing the categorization logic against MDM standards
- Worked with clinical and billing stakeholders to confirm the logic reflected real coding rules
- Moved the validated POC into a production-ready backend service
- Rolled the system out to physicians once validated

### Monitoring & Controlling (MC)

- Validated POC output against expected billing categories before any production exposure
- Reviewed categorization accuracy with billing stakeholders during the pilot
- Managed the controlled transition from POC to production
- Tracked open risks through to resolution before go-live

### Closing (CL)

- Completed the rollout to the physician base and confirmed the system was operating in production
- Obtained stakeholder sign-off with risks inventoried and accounted for
- Documented the approach and handed the running system to operational ownership
- Captured lessons learned on building clinical categorization from constrained inputs

---

## PMI KNOWLEDGE AREA COVERAGE

| Knowledge Area            | Involved? | Brief Note                                                                                            |
| ------------------------- | --------- | ---------------------------------------------------------------------------------------------------- |
| Scope Management          | Yes       | Held scope to a single categorization deliverable built around the no-transcript constraint           |
| Schedule Management       | Yes       | Managed POC-to-production delivery across a 5-month span                                              |
| Cost Management           | Yes       | Managed labor and AI gateway consumption against an internal-funded effort                            |
| Quality Management        | Yes       | Validated categorization output against correct MDM billing categories before rollout                 |
| Resource Management       | Yes       | Led a 3-person engineering team plus clinical and billing stakeholders                                |
| Communications Management | Yes       | Coordinated across engineering, billing, and clinical stakeholders through pilot and rollout          |
| Risk Management           | Yes       | Inventoried and resolved risks before go-live; compliance risk central given billing accuracy stakes  |
| Procurement Management    | Limited   | Internal AI gateway consumption; no external procurement                                              |
| Stakeholder Engagement    | Yes       | Engaged billing function, clinical stakeholders, and the physician user base throughout               |
| Integration Management    | Yes       | Integrated categorization logic with backend systems and existing billing workflow                    |

---

## STAKEHOLDERS & GOVERNANCE

**Stakeholders:**

- **Billing / Coding Function:** Defined the MDM standards the system had to satisfy and validated categorization accuracy
- **Clinical Stakeholders:** Confirmed the categorization logic was clinically sound
- **Engineering Team (2):** Built the categorization system under my lead
- **MDLive Physician Base:** End users affected by the billing categorization output

**Reporting Structure:** Led the project and reported into the AI Center of Excellence. Coordinated directly with billing and clinical stakeholders for requirements and validation.

**Governance:** Billing standards set by the coding function as fixed requirements. Categorization accuracy validated against known-correct categories before production. Go-live gated by stakeholder sign-off and risk review.

---

## RISKS & ISSUES

| Risk                                                          | Likelihood | Impact   | Mitigation                                                                                          |
| ------------------------------------------------------------ | ---------- | -------- | -------------------------------------------------------------------------------------------------- |
| Incorrect billing categorization creating compliance exposure | Medium     | Critical | Validated output against known-correct MDM categories before rollout; billing stakeholder review    |
| Metadata-only inputs insufficient to categorize accurately    | Medium     | High     | Proved viability through POC before production commitment; reviewed edge cases with billing         |
| Rollout disruption to physician billing workflow             | Low        | Medium   | Backend-only footprint kept the change contained; staged rollout after pilot validation             |

**Issues Resolved:**

- Replaced manual MDM billing categorization with an automated, validated approach
- Proved that accurate categorization was achievable from history and consult time without transcript access

---

## TOOLS & TECHNOLOGIES

| Category               | Tools                                                                       |
| ---------------------- | -------------------------------------------------------------------------- |
| AI / LLM Platform      | Azure OpenAI via Cigna internal AI gateway                                  |
| Backend                | Categorization service integrated with billing workflow                     |
| Clinical Standards     | MDM (Medical Decision Making) billing standards                             |
| Project Management     | POC validation cycle; staged rollout                                        |
| Methodology Frameworks | Hybrid POC-to-production; CPMAI AI project lifecycle principles              |

---

## LESSONS LEARNED

1. A hard input constraint can clarify a project instead of crippling it. Being told the system could not use the transcript forced an early, honest conversation about what was actually possible from history and consult time, and that clarity made the build faster than if we had kept the door open to everything.
2. With anything that touches billing, validation is the project, not a step in it. Proving the categorization matched real MDM categories before rollout was where most of the value and most of the risk lived.
3. A backend-only change is a gift when you can get it. Keeping the footprint off the physician-facing surface made the rollout far simpler than the transcript-based work that came before it.

---

## PMI APPLICATION NARRATIVE

This project came out of a billing problem at MDLive. Behavioral health psychiatry consults were being categorized for billing manually, and correct billing under Medical Decision Making standards depends on things like how complex the patient's history is and how much time was spent in the consult. Getting that wrong carries real compliance and revenue consequences. The goal was to build something that could categorize a consult to the right MDM billing level automatically.

The constraint that defined the whole project was that we could not use the transcript. Everything had to come from the patient's prior history and the time spent in the meeting. I scoped the work with billing and clinical stakeholders around that limitation, and we agreed to prove it out as a POC before committing to anything production grade.

I led a team of three. We built the categorization logic against the MDM standards, and I worked with the billing function to make sure what we were building reflected the actual coding rules rather than our interpretation of them. Once we had a working POC, I validated its output against billing categories we knew to be correct, reviewed the results with stakeholders, and confirmed the approach held up.

From there the rollout was relatively clean. Because the system lived on the backend rather than in a physician-facing interface, we did not have the same change-management surface that a front-end system would have. We rolled it out to physicians the same way we had handled prior MDLive work, with risks inventoried and stakeholder sign-off in place before anything went live. I closed the project by confirming production operation and handing the running system to operational ownership.

---

## TAGS

`#pmp-portfolio` `#healthcare` `#clinical-ai` `#behavioral-health` `#billing` `#mdm` `#cigna` `#mdlive` `#2025` `#backend` `#poc`

---

*Aligned to PMBOK 7th Edition & PMI PMP Examination Content Outline (ECO) 2021*