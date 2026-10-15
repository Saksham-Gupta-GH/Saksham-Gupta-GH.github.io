# Cheerio AI — Product Intern Take-Home Prompt Log
**Candidate:** Saksham Gupta (`saksham77779@gmail.com`)  
**Assignment:** Assignment A — Customer Support Scaling for Non-Technical Users  
**Role:** Product Intern (APM Track)  
**Date:** October 2026  
**Artifact Repository:** [GitHub Repository Source](https://github.com/Saksham-Gupta-GH/Saksham-Gupta-GH.github.io/tree/main/cheerio/assignment)

---

## 1. Candidate Plain-Voice Reflection & Strategy Retrospective

> *"When I first approached Cheerio's support bottleneck, my initial instinct was to explore an AI support chatbot or even a monetization model charging merchants ₹5 per automated resolution. 
> 
> However, when I modeled the unit economics and reflected on Cheerio's user persona—non-technical SMB merchants in India like retail jewelers and clinics—I realized that charging for support creates immediate friction during onboarding, causing churn that far outweighs any micro-fee revenue. 
> 
> Furthermore, merchants don't want to chat about API errors; they want their campaigns to launch. That realization led me to pivot from a conversational bot to an **in-app, deterministic Co-Pilot** that lints inputs on the frontend before calling Meta's API. Subsidizing this as a 100% free core feature delivers a 50.4x net return through preserved MRR, making it a powerful growth engine rather than a support cost center."*

---

## 2. AI Tools Utilized & Workflow Distribution
* **Claude 3.5 Sonnet / Antigravity Agent:** Product architecture, Meta Business Solution Provider API error taxonomy verification, failure mode edge-case stress-testing, and financial modeling.
* **Cursor / HTML / Tailwind CSS:** Prototyping of the interactive Google Workspace Material 3 in-app Cheerio Co-Pilot UI.
* **ChatGPT (GPT-4o):** Sanity checking SaaS support benchmarks (40 tickets/day Indian CS capacity) and token economics calculations.

---

## 3. Prompts That Worked Well

### Prompt 1: Meta Business API Failure Taxonomy & Error Verification
* **Prompt:**
  > *"Act as an engineering lead at an official Meta Business Solution Provider like Cheerio. Break down the top technical failure codes that non-technical SMB merchants trigger when submitting WhatsApp templates and registering phone numbers on the WhatsApp Cloud API (specifically INCORRECT_CATEGORY with tag TAG_CONTENT_MISMATCH, Error 133010 for unregistered phone numbers, and Error 132015 for paused templates). For each, explain why the user triggered it in plain business terms and what programmatic action can fix it."*
* **Why it worked:**
  * Grounded the solution in verified Meta Cloud API taxonomies rather than generic chatbot advice.
  * Provided the exact technical foundation for our pre-flight linter, 1-click remediation, and WABA phone binding diagnostics.
* **Chat Verification Link:**  
  `[PASTE CHAT LINK]` *(e.g. https://chatgpt.com/share/... or https://claude.ai/share/...)*
* **Raw Chat Screenshot:**  
  `[PASTE SCREENSHOT]`

### Prompt 2: Financial Unit Economics & Avoided Headcount Model
* **Prompt:**
  > *"Calculate the exact token cost for an AI support copilot serving 5,000 active businesses with 17,500 queries/month using GPT-4o-mini pricing ($0.15/1M input, $0.60/1M output, $0.075 cached input, USD:INR=84). Model average 3-turn sessions with 2,500 input and 500 output tokens. Frame support cost savings as avoided hiring as Cheerio scales against Indian customer support rep salaries (₹35,000/mo) at 40 tickets/day. Separate support headcount savings from retention revenue to prevent double counting. Show explicit formulas."*
* **Why it worked:**
  * Generated defensible unit economics, avoided headcount math, and realistic agent productivity numbers without hand-waving.
* **Chat Verification Link:**  
  `[PASTE CHAT LINK]`

### Prompt 3: Prototype Component Architecture & 4 Core Scenarios
* **Prompt:**
  > *"Create a single-page interactive HTML/Tailwind demo representing Cheerio's template creation and campaign hub UI. Include four testable scenarios: (1) Happy path 1-click auto-fix for promotional content in utility templates, (2) Human escalation after 2 failed attempts with pre-filled Diagnostic Packet, (3) Refusal guardrail for billing and account suspensions, and (4) WABA phone binding error 133010 with guided PIN handshake. Use Google Material 3 styling with zero emojis."*
* **Why it worked:**
  * Produced clean, interactive UI states covering both the core journey and non-happy path failure edge cases.
* **Chat Verification Link:**  
  `[PASTE CHAT LINK]`

---

## 4. Prompts That Failed & What Was Changed

### Failed Prompt 1: Unrealistic Agent Capacity & Gross vs. Net ROI Confabulation
* **Initial Prompt:**
  > *"Calculate the ROI of Cheerio using AI to replace support agents."*
* **Why it failed:**
  * The model output assumed a single support rep can handle 100 tickets/day (2.5x the realistic Indian B2B SaaS benchmark of 40 tickets/day).
  * It divided gross retained revenue directly by token costs, calling it "Net ROI" without subtracting AI spend, producing an unscientific 51.4x gross metric labeled as net.
* **What I Changed (Refined Prompt):**
  * Constrained the prompt to verified industry benchmarks: 40 tickets/day, 22 working days/month (880 tickets/rep/mo).
  * Mandated explicit separation of Gross ROI (Gross Preserved MRR / Cost = 51.4x) and Net ROI ((Gross Preserved MRR - Cost) / Cost = 50.4x).
  * Framed savings as avoided hiring as volume scales rather than firing existing staff.

### Failed Prompt 2: Generic Solution Brainstorming
* **Initial Prompt:**
  > *"How can Cheerio AI use AI to reduce customer support tickets?"*
* **Why it failed:**
  * Produced superficial, textbook chatbot ideas ("Build an FAQ search bot, send automated email responses, analyze user sentiment").
  * Ignored Cheerio's user reality: non-technical Indian SMBs getting blocked on third-party Meta developer policies, not a lack of text FAQs.
* **What I Changed:**
  * Switched to a persona-anchored prompt: *"Cheerio's users are non-technical SMB owners in India. How do we build an embedded in-app copilot that inspects DOM state and offers 1-click auto-fixes?"*

---

## 5. Hallucinations & Factual Errors Caught

1. **Meta Cloud API Error Code Hallucination:**
   * *Hallucination:* The model initially cited `Code 132015` as a "Category Mismatch" error.
   * *How I Caught It:* Cross-checked against Meta's WhatsApp Cloud API Error Documentation. Error `132015` actually indicates *"Template paused due to low quality"*. The real Meta rejection reason is `INCORRECT_CATEGORY` (paired with tag `TAG_CONTENT_MISMATCH`). Phone number registration failure is Error `133010`.
   * *Correction:* Updated the prototype and memo with verified Meta error codes and official India rate cards (Utility ₹0.1150/msg vs. Marketing ₹0.8631/msg).

2. **Backend Override Hallucination:**
   * *Hallucination:* The model suggested: *"Have the AI automatically override Meta's classification and approve the template directly on WhatsApp's backend."*
   * *How I Caught It:* As an official BSP, Cheerio has zero power to bypass Meta's automated compliance reviews without risking its BSP license.
   * *Correction:* Architected the solution strictly as a **client-side pre-flight linter** that intercepts and rephrases copy *before* calling Meta's API.

---

## 6. What Was Done Manually (Without AI)
1. **Product Judgment & Problem Selection:** Evaluated Assignment A vs. B; selected A because support bottlenecks directly cap merchant time-to-value and gross margins.
2. **North Star Metric Formulation:** Formulated **Zero-Touch Onboarding Completion Rate (ZOCR)** and modeled a realistic 90-day trajectory from 22% baseline to 33%.
3. **Strict Deflection Quality Standard:** Enforced the 7-day no-reopen criteria to ensure abandoned workflows are never counted as successful deflections.
4. **Monetization Trade-off Analysis:** Analyzed 4 pricing options and chose to subsidize Co-Pilot as a free core feature to maximize merchant retention ROI.
