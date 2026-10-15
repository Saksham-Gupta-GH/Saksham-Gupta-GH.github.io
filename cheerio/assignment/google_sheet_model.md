# Cheerio AI — Unit Economics & Cost Model (Spreadsheet Guide)
**Assignment:** Assignment A — Customer Support Scaling for Non-Technical Users  
**Candidate:** Saksham Gupta (`saksham77779@gmail.com`)  
**Generated File:** `cheerio_cost_model.xlsx` (8-Tab Formulaic Financial Model)

---

## Google Sheet Live Access
The spreadsheet is available as `cheerio_cost_model.xlsx` in this repository and can be opened in Google Sheets or LibreOffice with zero formula errors. All outputs are dynamically linked to the central `Assumptions` tab.

---

## Structure of the Spreadsheet Model (8 Tabs)

### Tab 1: `Assumptions` (Single Source of Truth)
* Centralized input repository containing all parameters with explicit type labels (`Given in Brief`, `Verified API Pricing`, `Verified Meta Doc`, `Industry Benchmark`, or `Stated Assumption`).
* Includes exact source URLs and verification dates (OpenAI API Pricing for GPT-4o-mini, Meta Cloud API Pricing for India Utility ₹0.1150 and Marketing ₹0.8631, and RBI USD:INR exchange rate = 84.0).

### Tab 2: `Executive_Summary`
* High-level KPI scorecard comparing Baseline (Pure Human) vs. Cheerio Co-Pilot.
* Shows Avoided Headcount (-13 reps), Net Monthly Savings (₹4,36,500), Blended Ticket Cost drop from ₹40.00 to ₹15.06, CapEx Payback Period (0.57 months / ~17 days), and both Gross (51.4x) and Net (50.4x) Retention ROI.

### Tab 3: `Volume_Model`
* **Active Merchant Base:** 5,000 businesses (`=Assumptions!C5`).
* **Monthly Support Query Rate:** 3.5 queries/business/mo = **17,500 queries/month** (`=B5*B6`).
* **Autonomous Deflection Target:** 65% (`=ROUND(B7*B9, 0)` = 11,375 queries).
* **Human Escalated Queries:** 35% (`=B7-B10` = 6,125 queries).

### Tab 4: `Token_Economics` & Sensitivity Table
* **Model:** GPT-4o-mini (OpenAI API official pricing).
* **Pricing:** $0.15 / 1M input tokens, $0.60 / 1M output tokens (USD:INR = 84.0).
* **Tokens per Session:** 2,500 input tokens, 500 output tokens.
* **LLM Cost per Query:** `=(B9/1M)*B7 + (B10/1M)*B8` = $0.000675 (~₹0.057).
* **Overhead Buffer (Serverless + Redis cache):** ₹0.1433/query.
* **Total Operational Cost per Query:** **₹0.20** (`=B14+B15`).
* **Total Monthly AI Infrastructure Cost:** **₹3,500 / month** (`=B16*B17` — AI touches all 17,500 inbound queries).
* **AI Cost per Active Business / Month:** **₹0.70 / business / month** (`=B18/Volume_Model!B5`).
* **Stress-Test Sensitivity Matrix:** 3x3 table modeling Token Volume (1x/2x/3x) against API Price Surges (1x/3x/5x).

### Tab 5: `Human_Comparison` (Avoided Headcount & Payback)
* **Agent Salary:** ₹35,000/month (Indian B2B SaaS Support standard).
* **Agent Monthly Capacity:** 40 tickets/day × 22 workdays = **880 tickets/month** (`=B6*B7`).
* **Pure Human Model (Avoided Baseline):** 17,500 tickets ÷ 880 = **20 Agents** = **₹7,00,000/month** (Cost/ticket: ₹40.00).
* **Cheerio Co-Pilot Model:** 6,125 human tickets ÷ 880 = **7 Agents** (₹2,45,000 payroll) + ₹3,500 AI + ₹15,000 Observability Tooling (LangSmith/Datadog) = **₹2,63,500/month** (Blended Cost/ticket: ₹15.06).
* **Avoided Headcount:** 13 agents avoided as volume scales (`=B11-B17`).
* **Net Monthly Operational Savings:** **₹4,36,500 / month** (`=B12-B21`).
* **Net Annual Operational Savings:** **₹52.38 Lakhs / year** (`=B25*12`).
* **CapEx Build Cost:** ₹2,50,000 (1 engineer for 1 month).
* **Payback Period:** **0.57 months (~17 days)** (`=B27/B25`).
* **Deflection Scenario Sensitivity:** Conservative (45% deflection → ₹3.31L/mo savings), Expected (65% deflection → ₹4.36L/mo savings), Aggressive (75% deflection → ₹5.06L/mo savings).

### Tab 6: `Retention_ROI` (Separated Churn Economics)
* **Average Plan Price (ARPU):** ₹2,999 / month.
* **Baseline Monthly Churn:** 5.0% (250 churning businesses/month).
* **Estimated Churn Reduction via Zero-Touch Onboarding (ZOCR):** 1.2% absolute (60 businesses saved/month).
* **Gross Preserved Recurring Revenue (MRR):** 60 × ₹2,999 = **₹1,79,940 / month** (`=B11*B6`).
* **Monthly AI Operating Cost:** **₹3,500 / month**.
* **Net Monthly Retained Value:** **₹1,76,440 / month** (`=B12-B14`).
* **Gross ROI on AI Spend:** **51.4x Return** (`=B12/B14`).
* **Net ROI on AI Spend:** **50.4x Return** (`=B15/B14`).
* **Churn Sensitivity Table:** Low (0.5% saved → 20.4x Net ROI), Base (1.2% saved → 50.4x Net ROI), High (2.0% saved → 84.7x Net ROI).

### Tab 7: `Billing_Strategy` (Pricing & Margins)
* Evaluates 4 monetization options with fully-loaded unit costs:
  1. **Model 1: Free Core Co-Pilot (Recommended Base):** Price = ₹0. Fully Loaded AI Cost/Query = ₹1.20 (LLM ₹0.20 + Cache ₹0.14 + Tooling ₹0.86). Delivers **₹1,57,940/month net surplus** (Net Retention MRR ₹1.76L minus AI cost ₹18.5k).
  2. **Model 2: Priority Support Add-on (Recommended Upsell):** Price = ₹499/mo for priority routing, SLA < 15 mins, and dedicated agent support. Cost to serve = ₹21.00. **Gross Margin = +95.8%** (`=ROUND((B6-D6)/B6, 3)`).
  3. **Model 3: Per-Resolution Micro-Fee:** Price = ₹5.00/resolution. Cost = ₹1.20. Gross Margin = +76.0%.
  4. **Model 4: Prepaid AI Resolution Pack:** Price = ₹199 for 50 resolutions. Cost = ₹60.00. Gross Margin = +69.8%.
* Amortized Human Escalation Share (₹14.00/query) is displayed as a separate operational line to avoid double-charging payroll.

### Tab 8: `Audit_Governance` (Observability Checklist & Owners)
* Defines monthly operational audit checks, alert thresholds, assigned owners, and automated remediation triggers across:
  - Cost per Resolved Query (>2x baseline, Alert: High, Owner: Lead APM / ML Eng)
  - Session Token Expansion (>140% 7-day avg, Alert: Medium, Owner: Backend Lead)
  - Single-Merchant Session Spikes (>50 sessions / 24h, Alert: High, Owner: SecOps / Support Lead)
  - **Deflection Rate (7-day verified):** Target 65%, Alert: <40%, Severity: Critical, Owner: Product Manager
  - **Zero-Touch Onboarding Rate (ZOCR):** Target 33% at Day 90, Alert: <25%, Severity: High, Owner: Onboarding & Growth Lead
  - 7-Day Ticket Reopen Rate (>5.0% of deflections, Alert: High, Owner: QA Lead / Support Lead)
  - Monthly Token Invoice Reconciliation (variance > ±2%, Alert: Medium, Owner: Finance / Tech Lead)
