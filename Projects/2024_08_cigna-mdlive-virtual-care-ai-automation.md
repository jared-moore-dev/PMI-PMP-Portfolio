# PMP Portfolio — Project Entry
> File: `2024_08_cigna-mdlive-virtual-care-ai-automation.md`

---

## PROJECT OVERVIEW

| Field | Value |
|---|---|
| **Project Title** | MDLive Virtual Primary Care AI Automation — SOAP Note Generation & Clinical Quality Review Platform |
| **Organization** | Cigna |
| **Your Job Title** | Lead Developer / Technical Project Lead |
| **Functional Reporting Area** | AICOE & Digital Health |
| **Organization Primary Focus** | Health Insurance / Virtual Primary Care / Clinical AI |
| **Approach / Methodology** | Hybrid — Agile iterative development with structured Dev/Prod release pipeline and formal compliance gates |
| **Project Team Size** | 4 (self as sole initial developer; scaled to 3 with 2 HIH team members; plus clinical stakeholder Dr. Steven Perez, Head MD of MDLive) |
| **Project Budget** | $500,000–$1,000,000 USD (estimated — engineering labor, Azure OpenAI API consumption, DevOps infrastructure, and compliance overhead across 14-month active delivery period) |
| **Project Start Date** | 08/2024 |
| **Project End Date** | 03/2025 (MVP + full delivery; 6-month advisory/transition to HIH team follows) |
| **Duration (months)** | 8 (active lead delivery; advisory transition period not counted to avoid inflation) |
| **Counts Toward PMP Months** | Yes — 8 months (no overlap with other documented projects) |

---

## PROJECT OBJECTIVE & OUTCOME

**Objective:**
MDLive had a basic NLP transcription tool. It produced summaries of virtual care consults but did nothing beyond that. During an investor call, Cigna's CIO described the service as having AI-powered SOAP note generation and automated physician quality review. It did not. I was brought in to build what had been described, quickly, and to do it in a way that would actually hold up in a clinical environment with real compliance requirements.

**Outcome:**
Delivered a production-grade clinical AI platform now used as the default workflow across MDLive's entire physician network. Key results:
- 400+ physicians onboarded; platform is the default for all virtual primary care consults
- 10,000+ consults processed through the AI pipeline in the first year of production
- Replaced a manual quarterly quality review process where a licensed physician listened to and graded 200+ transcripts per quarter at low accuracy
- Estimated $600,000+ in business savings from automation of physician quality assurance
- Reduced clinical risk through dynamic patient-appropriate prompting (pregnancy and breastfeeding questions surfaced only for applicable patients; dedicated question sets for minors)
- Platform ran through four model generations: GPT-3.5, GPT-4, GPT-4o, GPT-o1 via Azure OpenAI and Cigna's internal AI gateway, with zero production disruptions across all transitions
- Successfully transitioned to a permanent HIH engineering team in Hyderabad after a 6-month advisory handoff

---

## YOUR ROLE & RESPONSIBILITIES

**Role:** Lead Developer / Technical Project Lead

**Responsibilities:**
- Sole developer and technical project lead during the initial scoping and MVP build phase; owned architecture decisions, requirements definition, and delivery timeline under an urgent executive mandate
- Worked with my manager and cross-functional stakeholders to scope the solution from scratch: what SOAP note generation, automated quality review, and clinical compliance checking would actually require to build and operate
- Designed and built a dynamic prompt engineering pipeline with patient-context-aware clinical questioning: gender-appropriate, age-appropriate, drug interaction-aware prompting logic
- Built and maintained REST API endpoints integrating the AI pipeline with EHR and patient data systems for real-time clinical context injection
- Established a formal Dev/Prod DevOps workflow with environment separation and an automated testing suite that all feature changes had to pass before production deployment
- Built model drift monitoring to detect output quality degradation across model versions; designed and ran the model upgrade pipeline through four LLM generations without production disruption
- Engaged directly with Dr. Steven Perez, Head MD of MDLive, and the broader physician network to gather clinical feedback and translate it into prompt refinements and backlog items
- Documented HITL compliance standards and escalation pathways for model failure scenarios before any clinical deployment
- Transitioned the platform to a permanent HIH engineering team in Hyderabad; provided 6 months of advisory support for knowledge transfer

**Key Deliverables:**
- Initial solution scope and technical architecture (sole author)
- Dynamic prompt engineering pipeline with patient-context-aware clinical questioning logic
- SOAP note generation module (Subjective, Objective, Assessment, Plan)
- Automated physician quality review system with clinical compliance flags
- REST API layer integrating AI pipeline with EHR and patient data
- Dev/Prod DevOps workflow and automated testing suite
- Model drift monitoring system and multi-generation model upgrade pipeline
- HITL compliance documentation and escalation path framework
- Clinical stakeholder feedback integration process
- Knowledge transfer documentation and advisory support for HIH transition team

---

## PMI PROCESS GROUP COVERAGE

### Initiating (IN)
- Received executive mandate following the CIO investor call; worked with my manager to define project scope, success criteria, and delivery constraints under urgent timeline pressure
- Identified and engaged key stakeholders: direct manager, CIO/executive sponsor, Dr. Steven Perez (Head MD, MDLive), MDLive physician network, HIH engineering team, and Cigna clinical compliance function
- Defined the problem from first principles: MDLive had transcription only; SOAP note generation, automated quality review, and clinical compliance checking required a net-new AI pipeline architecture
- Established compliance and governance requirements as non-negotiable constraints from day one: HITL requirements, escalation documentation, and clinical accuracy standards

### Planning (PL)
- Scoped the full technical architecture solo: prompt engineering layer, API integration design, DevOps environment separation, drift monitoring approach, and model upgrade strategy
- Developed the phased delivery plan: MVP first, then clinical feedback integration, full feature build, Dev/Prod pipeline, model monitoring, and transition
- Planned the patient-context prompting framework to handle clinical edge cases before build: gender-specific questions, minor-specific question sets, drug interaction checks
- Planned HITL compliance framework and escalation pathways as a formal deliverable required before any clinical deployment
- Planned the model upgrade pipeline proactively, knowing LLM generations would evolve during the project; that assumption was validated across four transitions

### Executing (EX)
- Built the complete MVP solo: dynamic prompt pipeline, SOAP note generation, quality review flags, REST API layer integrated with EHR and patient data
- Once MVP was validated, onboarded 2 HIH engineers and established the Dev/Prod responsibility split: I built and tested on the dev side, HIH deployed to production after automated validation
- Ran clinical feedback sessions with Dr. Perez and MDLive physicians; turned physician input into prompt refinements and feature additions
- Executed four LLM generation upgrades using the purpose-built pipeline to validate each in Dev before promoting to production
- Documented and enforced all HITL compliance standards; trained the HIH team on compliance obligations before handoff

### Monitoring & Controlling (MC)
- Operated model drift monitoring continuously in production; detected and responded to output quality degradation across model transitions
- Managed the Dev/Prod pipeline as a hard quality gate: nothing reached production without passing the automated testing suite
- Brought physician feedback from Dr. Perez and the network into an ongoing backlog; prioritized by clinical impact and compliance risk
- Reported platform status and clinical adoption milestones to management and executive stakeholders throughout
- Monitored patient-context logic accuracy across edge cases: pregnancy flag suppression, minor-specific routing, drug interaction checks

### Closing (CL)
- Executed a structured 6-month advisory transition to the HIH Hyderabad team; produced knowledge transfer documentation covering architecture, prompt logic, DevOps workflow, compliance standards, and escalation procedures
- Obtained formal handoff acceptance from the HIH team and management
- Platform entered sustained operations under HIH ownership; now the default workflow for all MDLive consults
- Documented lessons learned on urgent project initiation, clinical AI governance, and scaling from solo to team delivery

---

## PMI KNOWLEDGE AREA COVERAGE

| Knowledge Area | Involved? | Brief Note |
|---|---|---|
| Scope Management | Yes | Scoped the full solution from zero under an urgent mandate; managed scope evolution across 4 model generations and physician feedback cycles |
| Schedule Management | Yes | Delivered MVP under urgent executive timeline; managed phased delivery across 8-month active period |
| Cost Management | Yes | Managed Azure OpenAI API consumption and infrastructure spend; delivered $600K+ in documented business savings |
| Quality Management | Yes | Built and operated automated testing suite as quality gate; managed clinical output accuracy through drift monitoring and HITL compliance framework |
| Resource Management | Yes | Scaled team from solo to 3; defined Dev/Prod responsibility split with HIH team; managed 6-month knowledge transfer |
| Communications Management | Yes | Managed communications across physicians, executive sponsor, HIH team, and compliance stakeholders across a 14-month engagement |
| Risk Management | Yes | Managed clinical AI risk via HITL requirements and escalation paths; proactively built model upgrade pipeline to mitigate model obsolescence risk |
| Procurement Management | Yes | Managed Azure OpenAI and AI gateway consumption; coordinated with internal platform teams for model access and infrastructure provisioning |
| Stakeholder Engagement | Yes | Directly engaged CIO/executive sponsor, Head MD of MDLive, 400+ physician user base, HIH engineering team, and clinical compliance function |
| Integration Management | Yes | Integrated prompt pipeline, EHR/patient data, REST APIs, DevOps workflow, drift monitoring, and HITL compliance into a single production system |

---

## STAKEHOLDERS & GOVERNANCE

**Stakeholders:**
- **Executive Sponsor / CIO:** Originating stakeholder whose investor call created the project mandate; recipient of delivery outcomes
- **Direct Manager:** Day-to-day project sponsor; co-scoped the solution and provided the escalation path for executive alignment
- **Dr. Steven Perez — Head MD, MDLive:** Primary clinical stakeholder; provided physician network feedback that shaped prompt engineering and feature prioritization throughout the project
- **MDLive Physician Network (400+):** End users of the platform; feedback incorporated through Dr. Perez and direct physician engagement sessions
- **HIH Engineering Team (Hyderabad):** Production deployment team during active delivery; permanent owners post-transition
- **Cigna Clinical Compliance Function:** Defined HITL requirements, escalation standards, and clinical AI governance constraints

**Reporting Structure:**
Reported directly to my manager throughout the project. Provided executive-level updates on platform status and clinical adoption milestones. Engaged Dr. Perez and the physician network directly for clinical requirements and feedback. Coordinated with the HIH team on production deployment decisions and transition planning.

**Governance:**
Technical architecture and prompt engineering decisions owned by me. Clinical requirements validated through Dr. Perez and the physician feedback loop. Compliance standards set by Cigna's clinical governance function as non-negotiable constraints. Production deployments gated by the automated testing suite — nothing deployed without passing validation.

---

## RISKS & ISSUES

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Clinical AI output inaccuracy causing patient safety issues | Low | Critical | HITL compliance framework with documented escalation paths; automated testing gates; physician review of all output types before production rollout |
| LLM model deprecation disrupting production service | High | High | Proactively designed model upgrade pipeline; validated each new generation in Dev before promoting to Prod; drift monitoring to detect degradation early |
| Solo developer as single point of failure on urgent mandate | High | High | Prioritized MVP delivery to reduce exposure window; scaled to 3-person team as soon as MVP was validated; documented architecture throughout |
| Dynamic prompting logic failing on clinical edge cases | Medium | High | Extensively built and tested patient-context-aware routing logic; edge case scenarios included in automated testing suite |
| Knowledge loss during HIH team transition | Medium | High | Structured 6-month advisory transition with formal documentation; did not disengage until HIH team demonstrated independent operational capability |
| Regulatory / compliance gap in clinical AI deployment | Medium | Critical | Engaged compliance function from initiation; HITL requirements and escalation paths defined as project constraints from the start |

**Issues Resolved:**
- Investor call gap: delivered a fully functional SOAP note generation and quality review platform from zero within the urgent MVP window
- Quarterly quality review bottleneck: replaced a manual, low-accuracy licensed physician QA process with an automated AI pipeline
- Model upgrade continuity: navigated 4 LLM generations (GPT-3.5, 4, 4o, o1) in production without service disruption

---

## TOOLS & TECHNOLOGIES

| Category | Tools |
|---|---|
| AI / LLM Platform | Azure OpenAI (GPT-3.5, GPT-4, GPT-4o, GPT-o1) via Cigna internal AI gateway |
| Prompt Engineering | Dynamic prompt pipeline (custom-built); patient-context-aware prompting framework |
| API Development | REST API endpoints; EHR and patient data integration layer |
| DevOps | Dev/Prod environment separation; automated testing suite; CI/CD pipeline |
| Model Monitoring | Custom drift monitoring system; model upgrade pipeline |
| Clinical Standards | SOAP note framework; HITL compliance documentation; clinical escalation path design |
| Project Management | Agile backlog management; physician feedback integration cycle |
| Methodology Frameworks | Hybrid Agile / compliance-gated release model; CPMAI AI project lifecycle principles |

---

## LESSONS LEARNED

1. When a project starts as a reaction to something urgent, the first thing to do is slow down long enough to define scope properly. The temptation is to start building immediately. Taking time to define what the system needed to do, what the compliance constraints were, and what done actually looked like saved far more time than it cost.
2. Clinical AI governance is not a phase you get to later. HITL requirements, escalation paths, and patient safety edge cases have to be in the architecture from the beginning. Trying to retrofit compliance after the fact would have meant rebuilding core parts of the system. Treating it as a constraint from day one meant it was never a problem.
3. Model obsolescence in AI projects is not a risk to plan for someday — it is a certainty to plan for now. Building the model upgrade pipeline before we needed it meant that four LLM generation transitions happened without a single production incident. If we had handled upgrades ad hoc, at least one of those would have caused a disruption.

---

## PMI APPLICATION NARRATIVE

This project started with an investor call. Cigna's CIO publicly described MDLive as having AI-powered SOAP note generation and automated physician quality review. The problem was that MDLive did not have those things. What existed was a basic NLP transcription tool that produced summaries. I was brought in to build what had been described, and to do it fast enough that the gap did not stay open long.

I started alone in August 2024. My first job was scoping the problem before writing any code. What would SOAP note generation actually require? What would automated quality review look like in a clinical setting? What compliance constraints applied before any of this could touch a real patient consult? I worked through those questions with my manager and Cigna's clinical governance function and came out with a clear architecture and a set of non-negotiable requirements: human-in-the-loop standards, documented escalation paths for model failures, and patient-context-aware prompting logic that handled clinical edge cases correctly.

The core system I built had three parts. First, a dynamic prompt engineering pipeline that pulled patient context from EHR and patient data systems and used it to generate clinically appropriate questions. The prompting logic was patient-specific: different question sets for minors, pregnancy and breastfeeding questions surfaced only for applicable patients, drug interaction checks built in. Second, structured SOAP note generation from the consult output. Third, an automated quality review layer with clinical compliance flags that checked whether the right questions had been asked for the right patient type. All of it ran through a formal Dev/Prod pipeline with an automated testing suite that every change had to pass before reaching production.

Once the MVP was validated I brought in two HIH engineers. I kept the development and testing side; they handled production deployments after automated validation. I ran regular feedback sessions with Dr. Steven Perez, Head MD of MDLive, and used what I heard from him and the broader physician network to drive prompt refinements and feature prioritization. I also built model drift monitoring and a structured upgrade pipeline, which ended up handling four LLM generation transitions from GPT-3.5 through GPT-o1 without a single production incident.

The platform is now the default for all MDLive virtual primary care consults. Over 400 physicians use it. It processed more than 10,000 consults in its first year and replaced a quarterly manual review process that had a licensed physician listening to and grading over 200 transcripts per quarter at low accuracy. Estimated business savings came in at over $600,000. I closed the project with a six-month structured advisory transition to the permanent HIH team in Hyderabad.

---

## TAGS
`#pmp-portfolio` `#healthcare` `#clinical-ai` `#llm` `#azure-openai` `#devops` `#virtual-care` `#cigna` `#mdlive` `#2024` `#prompt-engineering` `#hitl` `#model-monitoring` `#soap-notes`

---
*Aligned to PMBOK 7th Edition & PMI PMP Examination Content Outline (ECO) 2021*