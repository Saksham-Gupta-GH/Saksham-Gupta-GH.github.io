# Cheerio AI — Product Intern Take-Home Submission (Assignment A)
**Candidate:** Saksham Gupta  
**Email:** [saksham77779@gmail.com](mailto:saksham77779@gmail.com)  
**Phone:** +91-9354369079  
**Role:** Product Intern (APM Track) — Assignment A: *Make Customer Support Scale for Non-Technical Users*  
**Date:** October 2026  

---

## 🔗 Key Deliverables & Live Links

| Deliverable | Description | Live Link / Access |
| :--- | :--- | :--- |
| **1. Clickable Prototype** | Live interactive Google Material 3 Co-Pilot prototype covering 4 core scenarios | [**saksham-gupta-gh.github.io/cheerio-copilot/**](https://saksham-gupta-gh.github.io/cheerio-copilot/) |
| **2. Financial Model (Google Sheet)** | 8-tab formulaic model (Volume, Tokens, Avoided Headcount, Churn ROI, Billing, Audit) | [**Google Sheets Live Formula Model**](https://docs.google.com/spreadsheets/d/1uVWQ07DMbBS1jfx3AAPk0cMrANQjfBIGgRCevV2Zgv8/edit?usp=sharing) |
| **3. Product Memo (PDF)** | 4-page executive solution doc (Taxonomy, 8 Alternatives, Guardrails, Economics) | [**View PDF in Repository**](Cheerio_Product_Intern_Assignment_Saksham_Gupta.pdf) |
| **4. Engineering Prompt Log** | Verifiable prompt iterations, hallucinations caught, session IDs, and retrospectives | [**prompt_log.md**](prompt_log.md) |
| **5. Clean Offline Bundle** | Complete assignment package with zero duplicates | [**assignment.zip**](../assignment.zip) |

---

## 🎯 Executive Summary & Strategic Rationale

Non-technical SMB merchants on Cheerio experience catastrophic onboarding friction when Meta’s WhatsApp Cloud API policies reject their initial campaign templates (category mismatches, utility vs. marketing tariff misclassifications, and phone binding errors). When a merchant's first broadcast fails, they raise support tickets, wait hours, and churn before month two.

Instead of building another generic FAQ chatbot that adds cognitive load, this submission presents the **Cheerio In-App Co-Pilot**: an embedded, state-aware assistant that inspects client-side DOM payloads, catches compliance errors pre-flight, and provides 1-click remediation directly inside the campaign builder.

### Key Financial & Operational Metrics (Evaluated at 5,000 Active Merchants):
* **Support Volume:** 17,500 inbound tickets/month (3.5 tickets/merchant/month).
* **Autonomous Deflection Target:** **65% autonomous deflection** (11,375 tickets resolved without human intervention, verified by a strict 7-day no-reopen quality standard).
* **Avoided Headcount:** At 40 tickets/rep/day (880 tickets/mo), scaling pure human support requires 20 agents (₹7.0L/mo). With Co-Pilot, support scales with only 7 agents, **avoiding 13 support hires**.
* **Net Operational Savings:** **₹4,36,500 / month net savings** (₹52.38 Lakhs/year), dropping blended cost per ticket from **₹40.00 to ₹15.06** (-62.4%).
* **Rapid Payback:** The one-time ₹2,50,000 engineering build CapEx achieves full breakeven in **0.57 months (~17 days)**.
* **Dual Retention ROI:** Powered by GPT-4o-mini + Redis semantic cache at ₹0.31 per resolved query, generating **50.4x Net Token ROI** and **8.7x Fully-Loaded Program ROI** against preserved merchant MRR.

---

## 🛠️ The 4 Interactive Prototype Scenarios

The live prototype is accessible at [https://saksham-gupta-gh.github.io/cheerio-copilot/](https://saksham-gupta-gh.github.io/cheerio-copilot/) and models 4 key scenarios:

1. **Scenario 1 — Pre-Flight Linter & 1-Click Fix (Happy Path):**  
   Intersects promotional copy placed in a Utility template. Highlights regex diff preview, calculates tariff impact (Utility ₹0.1150 vs. Marketing ₹0.8631), and applies sanitization in 1 click.
2. **Scenario 2 — Circuit Breaker & Structured Escalation (Failure State):**  
   Trips when a user rejects suggestions twice. Seamlessly opens a WhatsApp support thread and auto-populates a structured JSON Diagnostic Packet (error codes, payload diffs, merchant ID) for Tier-2 agents.
3. **Scenario 3 — Guardrail Refusal (Negative Boundary):**  
   Hard refusal for account suspensions and invoice/billing disputes. Explains why AI cannot guess and routes directly to Cheerio finance specialists.
4. **Scenario 4 — WABA Phone Binding (Meta Error 133010):**  
   Guides non-technical users through the Meta Cloud API 2-step verification PIN handshake to bind numbers without technical support.

---

## 📂 Repository Structure

```
cheerio/assignment/
├── Cheerio_Product_Intern_Assignment_Saksham_Gupta.pdf   # 4-page final solution memo (zero cutoffs)
├── cheerio_cost_model.xlsx                             # 8-tab offline Excel model (0 formula errors)
├── solution_doc.html                                   # Source HTML for memo layout
├── prompt_log.md                                       # Transparent prompt engineering log & session IDs
├── google_sheet_model.md                               # Financial model reference documentation
├── scratch_build_sheet.py                              # Automated openpyxl generation script
├── prototype/
│   └── index.html                                      # Interactive Google Material 3 prototype
├── screenshots/                                        # Scenario captures (Scenarios 1-4)
└── README.md                                           # This repository index
```
