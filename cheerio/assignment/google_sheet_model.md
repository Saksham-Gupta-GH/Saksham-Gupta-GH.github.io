# Cheerio AI — Unit Economics & Cost Model (Spreadsheet Guide)
**Assignment:** Assignment A — Customer Support Scaling for Non-Technical Users  
**Candidate:** Saksham Gupta (`saksham77779@gmail.com`)  
**Generated File:** `cheerio_cost_model.xlsx` (Generated directly in the workspace)

---

## How to Deploy to Google Sheets (30 seconds)
1. Open Google Drive: [drive.google.com](https://drive.google.com).
2. Click **New > File upload** and select `cheerio_cost_model.xlsx`.
3. Open the uploaded file in Google Sheets.
4. Click **Share** (top-right) → Under *General access*, change to **"Anyone with the link can view"**.
5. Copy the link and paste it into the Google submission form and into `solution_doc.html`.

---

## Structure of the Spreadsheet Model (5 Tabs)

### Tab 1: `Executive_Summary`
* High-level KPI scorecard comparing Baseline (Pure Human) vs. Cheerio Co-Pilot.
* Shows Net Monthly Savings (₹4,51,500), Blended Ticket Cost drop from ₹40.00 to ₹14.20, and Churn Retention ROI (51.4x).

### Tab 2: `Volume_Model`
* **Active Merchant Base:** 5,000 businesses.
* **Monthly Support Query Rate:** 3.5 queries/business/mo = **17,500 queries/month** (`=B5*B6`).
* **Autonomous Deflection Target:** 65% (`=ROUND(B7*B9, 0)` = 11,375 queries).
* **Human Escalated Queries:** 35% (`=B7-B10` = 6,125 queries).

### Tab 3: `Token_Economics`
* **Model:** GPT-4o-mini (OpenAI API official pricing).
* **Pricing:** $0.15 / 1M input tokens, $0.60 / 1M output tokens (USD:INR = 84.0).
* **Tokens per Session:** 2,500 input tokens, 500 output tokens.
* **LLM Cost per Query:** `=(B9/1M)*B7 + (B10/1M)*B8` = $0.000675 (~₹0.057).
* **Overhead Buffer (Serverless + Redis cache):** ₹0.1433/query.
* **Blended Cost per Query:** **₹0.20** (`=B14+B15`).
* **Total Monthly AI Infrastructure Cost:** **₹3,500 / month** (`=B16*B17`).
* **AI Cost per Active Business / Month:** **₹0.70 / business / month** (`=B18/Volume_Model!B5`).

### Tab 4: `Human_Comparison`
* **Agent Salary:** ₹35,000/month (Indian B2B SaaS Support standard).
* **Agent Monthly Capacity:** 40 tickets/day × 22 workdays = **880 tickets/month**.
* **Pure Human Model:** 17,500 tickets ÷ 880 = **20 Agents** = **₹7,00,000/month** (Cost/ticket: ₹40.00).
* **Cheerio Co-Pilot Model:** 6,125 human tickets ÷ 880 = **7 Agents** (₹2,45,000 payroll) + ₹3,500 AI = **₹2,48,500/month** (Cost/ticket: ₹14.20).
* **Net Monthly Savings:** **₹4,51,500 / month** (`=B12-B20`).
* **Annualized Savings:** **₹54.18 Lakhs / year** (`=B23*12`).

### Tab 5: `Retention_ROI`
* **Average Plan Price (ARPU):** ₹2,999 / month.
* **Baseline Monthly Churn:** 5.0% (250 churning businesses/month).
* **Churn Reduction via Zero-Touch Onboarding (ZOCR):** 1.2% absolute (60 businesses saved/month).
* **Preserved Recurring Revenue:** 60 × ₹2,999 = **₹1,79,940 / month** (`=B11*B6`).
* **Monthly AI Operating Cost:** **₹3,500 / month**.
* **Net Financial Value Generated:** **₹1,76,440 / month**.
* **ROI on AI Spend:** **51.4x Return** (`=B12/B14`).
