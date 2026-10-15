# Cheerio AI — Product Intern Take-Home Prompt Log
**Candidate:** Saksham Gupta  
**Assignment:** Assignment A — Make Customer Support Scale for Non-Technical Users  
**Role:** Product Intern (APM Track)  
**Date:** October 2026  

---

## 1. AI Tools Utilized & Workflow Distribution
* **Claude 3.5 Sonnet:** Architecture modeling, Meta Business Solution Provider API error taxonomy extraction, failure mode edge-case stress-testing.
* **Cursor (IDE) / v0:** Rapid prototyping of the in-app interactive Cheerio Co-Pilot UI.
* **ChatGPT (GPT-4o):** Sanity checking initial SaaS support metric formulas and support agent ticket handling capacities.

---

## 2. Prompts That Worked Well

### Prompt 1: Meta Business API Failure Taxonomy
* **Prompt:**
  > *"Act as an engineering lead at an official Meta Business Solution Provider like Cheerio. Break down the top technical failure codes that non-technical SMB merchants trigger when submitting WhatsApp templates (such as Cloud API Code 132015 Category Mismatch, Code 132000 Parameter Count Mismatch, and REJECTED_CATEGORY_MISMATCH). For each, explain why the user triggered it in plain business terms and what programmatic action can fix it."*
* **Why it worked:**
  * Grounded the solution in verified Meta API taxonomies rather than generic chatbot advice.
  * Provided the exact technical foundation for our pre-flight linter and 1-click remediation.

### Prompt 2: Financial Unit Economics & Token Costing
* **Prompt:**
  > *"Calculate the exact token cost for an AI support copilot serving 5,000 active businesses with 17,500 queries/month using GPT-4o-mini pricing ($0.15/1M input, $0.60/1M output, USD:INR=84). Model average 3-turn sessions with 2,500 input and 500 output tokens. Compare this against Indian customer support rep salaries (₹35,000/mo) at 40 tickets/day. Show explicit formulas."*
* **Why it worked:**
  * Generated defensible unit economics and realistic agent productivity numbers without hand-waving.

### Prompt 3: Prototype Component Architecture & Edge Cases
* **Prompt:**
  > *"Create a single-page interactive HTML/Tailwind demo representing Cheerio's template creation UI. Include an AI Copilot side-drawer with three testable scenarios: (1) Happy path 1-click auto-fix for promotional content in utility templates, (2) Human escalation after 2 failed attempts with pre-filled Diagnostic Packet, and (3) Refusal guardrail for billing and account suspensions."*
* **Why it worked:**
  * Generated clean UI states covering both the core journey and required edge cases.

---

## 3. Prompts That Failed & What Was Changed

### Failed Prompt 1: Generic Solution Brainstorming
* **Initial Prompt:**
  > *"How can Cheerio AI use AI to reduce customer support tickets?"*
* **Why it failed:**
  * The response was superficial and generic ("Build an AI chatbot, create a better FAQ search, send automated email responses, analyze sentiment").
  * It failed to address the core issue: Cheerio's users are non-technical merchants who get blocked by Meta's strict developer policies and complex data formats, not a lack of text answers.
* **What I Changed (Refined Prompt):**
  * Shifted to a **persona-anchored, state-aware prompt**:
  > *"Cheerio AI's users are non-technical SMB business owners in India (jewellery retailers, coaching centers). They get stuck during onboarding on WhatsApp API verification, rejected templates, and CSV contact uploads. How do we build an embedded in-app copilot that inspects their live account state and provides 1-click auto-fixes rather than just text advice?"*
  * **Result:** Led directly to the winning "Cheerio Co-Pilot" concept with deterministic error interception.

---

## 4. Hallucinations & Weak Answers Caught

* **Hallucination Identified:** When analyzing how to resolve Meta template rejections, the AI suggested: *"Have the AI automatically override Meta's classification and approve the template directly on WhatsApp's backend."*
* **How I Caught It:** As an official Meta Business Solution Provider, Cheerio must adhere strictly to Meta's automated server-side policy reviews. Cheerio cannot arbitrarily override Meta's compliance servers without risking suspension of its BSP license.
* **The Manual Correction:** I pivoted the product architecture so that the Co-Pilot acts as a **pre-flight linter** on Cheerio's frontend—modifying promotional copy to comply with Meta's guidelines *before* calling Meta's API, thus preventing the rejection from ever happening.

---

## 5. What Was Done Manually (Without AI)
1. **Product Judgment & Problem Selection:** Chose Assignment A (Support Scaling) over Assignment B because support resolution directly unblocks Time-to-First-Campaign and enterprise expansion.
2. **North Star Metric Formulation:** Defined **Zero-Touch Onboarding Completion Rate (ZOCR)** uniting usability, third-party API reliability, and customer retention.
3. **Human Escalation Thresholds:** Architected the 2-attempt limit rule and the structured "Diagnostic Ticket Packet" handoff protocol to avoid user frustration.
4. **Economic Sanity Checks:** Validated support rep ticket throughput benchmarks (40 tickets/day in Indian B2B SaaS) against real-world operations.
