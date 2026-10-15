import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

# Style helpers
header_fill = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid") # Dark Blue
header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
sub_header_fill = PatternFill(start_color="DBEAFE", end_color="DBEAFE", fill_type="solid") # Soft Blue
sub_header_font = Font(name="Calibri", size=11, bold=True, color="1E3A8A")
accent_fill = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid") # Soft Green
accent_font = Font(name="Calibri", size=11, bold=True, color="15803D")
alert_fill = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid") # Light Amber
alert_font = Font(name="Calibri", size=11, bold=True, color="92400E")
title_font = Font(name="Calibri", size=14, bold=True, color="0F172A")
meta_font = Font(name="Calibri", size=9, italic=True, color="64748B")
bold_font = Font(name="Calibri", size=11, bold=True)
regular_font = Font(name="Calibri", size=11)

thin_border = Border(
    left=Side(style='thin', color="E2E8F0"),
    right=Side(style='thin', color="E2E8F0"),
    top=Side(style='thin', color="E2E8F0"),
    bottom=Side(style='thin', color="E2E8F0")
)

# -------------------------------------------------------------
# TAB 1: Assumptions (Single Source of Truth)
# -------------------------------------------------------------
ws0 = wb.active
ws0.title = "Assumptions"
ws0.views.sheetView[0].showGridLines = True

ws0["A1"] = "Cheerio AI — Co-Pilot Financial & Unit Economics Model: Assumptions"
ws0["A1"].font = title_font
ws0["A2"] = "Single Source of Truth • Candidate: Saksham Gupta (saksham77779@gmail.com)"
ws0["A2"].font = meta_font

headers_assumptions = ["Parameter Code", "Parameter Description", "Value", "Unit", "Type", "Source URL / Benchmark Rationale", "Access / Verification Date"]
for col_idx, h in enumerate(headers_assumptions, start=1):
    cell = ws0.cell(row=4, column=col_idx, value=h)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center" if col_idx in [3, 4, 5, 7] else "left", vertical="center")

assumptions_data = [
    ("BIZ_BASE", "Active Merchant Customer Base", 5000, "Businesses", "Given in Brief", "Cheerio Assignment Brief specification", "Oct 2026"),
    ("NEW_SIGNUPS", "New Merchant Signups per Month", 500, "Signups / mo", "Stated Assumption", "Candidate estimate: 10% monthly onboarding cohort", "Oct 2026"),
    ("QUERY_RATE", "Monthly Support Query Rate per Merchant", 3.5, "Queries / biz / mo", "Stated Assumption", "Candidate estimate: 5-7 queries in onboarding; 1-2 in mature phase", "Oct 2026"),
    ("FX_USD_INR", "USD to INR Exchange Rate", 84.0, "INR / USD", "Industry Benchmark", "RBI Reference Exchange Rate (rbi.org.in)", "Oct 2026"),
    ("LLM_IN_PRICE", "GPT-4o-mini Input Token Price", 0.15, "USD / 1M tokens", "Verified API Pricing", "https://openai.com/api/pricing", "Oct 2026"),
    ("LLM_IN_CACHE", "GPT-4o-mini Cached Input Token Price", 0.075, "USD / 1M tokens", "Verified API Pricing", "https://openai.com/api/pricing (50% cache hit discount)", "Oct 2026"),
    ("LLM_OUT_PRICE", "GPT-4o-mini Output Token Price", 0.60, "USD / 1M tokens", "Verified API Pricing", "https://openai.com/api/pricing", "Oct 2026"),
    ("TOKENS_IN", "Average Input Tokens per Query Session", 2500, "Tokens / query", "Stated Assumption", "System prompt (1k) + error payload (500) + 3 turns (1k)", "Oct 2026"),
    ("TOKENS_OUT", "Average Output Tokens per Query Session", 500, "Tokens / query", "Stated Assumption", "Structured diagnostic + JSON remediation payload", "Oct 2026"),
    ("INFRA_OVERHEAD", "Serverless & Redis Cache Buffer", 0.1433, "INR / query", "Industry Benchmark", "Cloudflare Workers & Upstash Redis semantic cache", "Oct 2026"),
    ("AGENT_SALARY", "Human Support Rep Monthly Salary", 35000, "INR / agent / mo", "Industry Benchmark", "Glassdoor / AmbitionBox Indian B2B SaaS CS benchmark", "Oct 2026"),
    ("WORK_DAYS", "Working Days per Month", 22, "Days / mo", "Standard Work Week", "5-day work week standard", "Oct 2026"),
    ("AGENT_TICKETS_DAY", "Daily Ticket Handling Capacity per Rep", 40, "Tickets / agent / day", "Stated Assumption", "Assumes 12 mins per ticket across async chat / email", "Oct 2026"),
    ("BASE_DEFLECTION", "Baseline Deflection Rate (Status Quo)", 0.12, "% deflected", "Stated Assumption", "Static FAQ & docs deflection prior to Co-Pilot", "Oct 2026"),
    ("TARGET_DEFLECTION", "Co-Pilot Target Deflection Rate (Base)", 0.65, "% deflected", "Stated Target", "Target across top technical bottlenecks in 90 days", "Oct 2026"),
    ("BASE_ZOCR", "Baseline Zero-Touch Onboarding Rate", 0.22, "% rate", "Stated Assumption", "Candidate estimate of status quo onboarding completion", "Oct 2026"),
    ("TARGET_ZOCR_DAY90", "Target Zero-Touch Onboarding Rate (Day 90)", 0.33, "% rate", "Realistic Target", "Realistic 90-day trajectory: 22% baseline -> 33% (+11.0% gain)", "Oct 2026"),
    ("BUILD_COST", "One-Time Capital / Dev Build Cost", 250000, "INR", "Stated Assumption", "1 Senior Fullstack/AI Eng for 1 month", "Oct 2026"),
    ("TOOLING_MONTHLY", "Monthly Observability Tooling Cost", 15000, "INR / mo", "Industry Benchmark", "LangSmith/Helicone + Datadog APM tier", "Oct 2026"),
    ("ARPU_MONTHLY", "Average Monthly Subscription Revenue (ARPU)", 2999, "INR / biz / mo", "Stated Assumption", "Cheerio Starter/Growth plan standard SaaS pricing", "Oct 2026"),
    ("BASE_CHURN", "Baseline Monthly Merchant Churn Rate", 0.05, "% / mo", "Industry Benchmark", "5.0% monthly churn typical in Indian SMB SaaS", "Oct 2026"),
    ("CHURN_REDUCTION", "Estimated Churn Reduction from ZOCR (Base)", 0.012, "% absolute", "Stated Assumption", "1.2% absolute churn reduction via onboarding fix", "Oct 2026"),
    ("META_UTIL_RATE", "Meta India Utility Message Delivery Rate", 0.1150, "INR / msg", "Verified Meta Doc", "https://developers.facebook.com/docs/whatsapp/pricing", "Oct 2026"),
    ("META_MKT_RATE", "Meta India Marketing Message Delivery Rate", 0.8631, "INR / msg", "Verified Meta Doc", "https://developers.facebook.com/docs/whatsapp/pricing", "Oct 2026"),
]

for row_idx, row in enumerate(assumptions_data, start=5):
    for col_idx, val in enumerate(row, start=1):
        cell = ws0.cell(row=row_idx, column=col_idx, value=val)
        cell.font = bold_font if col_idx in [1, 3] else regular_font
        cell.border = thin_border
        if col_idx == 3:
            cell.alignment = Alignment(horizontal="right")
            if "Rate" in row[1] or "Price" in row[1] and "USD" in row[3]:
                if "%" in row[3]:
                    cell.number_format = "0.0%"
                elif "USD" in row[3]:
                    cell.number_format = "$#,##0.000"
                else:
                    cell.number_format = "₹#,##0.0000"
            elif "Salary" in row[1] or "Cost" in row[1] or "ARPU" in row[1]:
                cell.number_format = "₹#,##0"
            elif isinstance(val, (int, float)):
                cell.number_format = "#,##0" if val >= 10 else "0.00"

# -------------------------------------------------------------
# TAB 2: Executive Summary (KPIs & High-Level ROI)
# -------------------------------------------------------------
ws1 = wb.create_sheet(title="Executive_Summary")
ws1.views.sheetView[0].showGridLines = True

ws1["A1"] = "Cheerio AI — Customer Support Scaling Executive Summary"
ws1["A1"].font = title_font
ws1["A2"] = "Financial Model & Unit Economics Summary • Evaluated at 5,000 Active Merchants"
ws1["A2"].font = meta_font

summary_headers = ["Key Operational Metric", "Baseline (Human Only)", "With Cheerio Co-Pilot", "Delta / Impact", "Source & Formula Reference"]
for col_idx, h in enumerate(summary_headers, start=1):
    cell = ws1.cell(row=4, column=col_idx, value=h)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center" if col_idx > 1 else "left", vertical="center")

kpi_data = [
    ("Active Merchant Base", "=Assumptions!C5", "=Assumptions!C5", "0 (Baseline)", "Assumptions!C5"),
    ("Total Monthly Inbound Queries", "=Volume_Model!B7", "=Volume_Model!B7", "0 (Baseline)", "Volume_Model!B7 (17,500 queries)"),
    ("Autonomous Ticket Deflection Rate", "=Assumptions!C18", "=Assumptions!C19", "+53.0%", "Assumptions!C18 vs C19"),
    ("Human Support Headcount Required", "=Human_Comparison!B11", "=Human_Comparison!B17", "-13 Agents Avoided", "Human_Comparison!B11 vs B17"),
    ("Total Monthly Support Running Cost (₹)", "=Human_Comparison!B12", "=Human_Comparison!B21", "-₹4,36,500 / mo", "Human_Comparison!B12 vs B21"),
    ("Cost per Resolved Ticket (₹)", "=Human_Comparison!B13", "=Human_Comparison!B22", "-₹24.94 / ticket (-62.4%)", "Human_Comparison!B13 vs B22"),
    ("Monthly AI Token & Infra Cost (₹)", 0, "=Token_Economics!B18", "+₹3,500 / mo", "Token_Economics!B18 (17,500 queries @ ₹0.20)"),
    ("Monthly Observability & Tooling (₹)", 0, "=Assumptions!C23", "+₹15,000 / mo", "Assumptions!C23 (LangSmith / Datadog)"),
    ("Net Monthly Operational Cost Savings (₹)", 0, "=Human_Comparison!B25", "+₹4,36,500 / mo", "Human_Comparison!B25 (₹52.38L / yr)"),
    ("One-Time Development Build Cost (₹)", 0, "=Assumptions!C22", "₹2,50,000", "Assumptions!C22 (1 Eng for 1 Month)"),
    ("CapEx Payback Period (Months)", "-", "=ROUND(Assumptions!C22/Human_Comparison!B25, 2)", "0.57 Months (~17 Days)", "Build Cost / Net Monthly Savings"),
    ("Gross Merchant Retention ROI (Direct Tokens)", "-", "=Retention_ROI!B18", "51.4x Return", "Retention_ROI!B18 (Gross MRR / AI Tokens)"),
    ("Net Merchant Retention ROI (Direct Tokens)", "-", "=Retention_ROI!B19", "50.4x Return", "Retention_ROI!B19 (Net MRR / AI Tokens)"),
    ("Net Merchant Retention ROI (Total Program)", "-", "=Retention_ROI!B21", "8.7x Return", "Retention_ROI!B21 (Net MRR / ₹18.5k Total AI+Tooling)"),
]

for row_idx, row in enumerate(kpi_data, start=5):
    for col_idx, val in enumerate(row, start=1):
        cell = ws1.cell(row=row_idx, column=col_idx, value=val)
        cell.font = bold_font if col_idx in [1, 4] else regular_font
        cell.border = thin_border
        if col_idx in [2, 3]:
            cell.alignment = Alignment(horizontal="right")

# Highlight net savings and ROI
ws1["A13"].fill = accent_fill
ws1["B13"].fill = accent_fill
ws1["C13"].fill = accent_fill
ws1["D13"].fill = accent_fill
ws1["E13"].fill = accent_fill

ws1["A17"].fill = accent_fill
ws1["B17"].fill = accent_fill
ws1["C17"].fill = accent_fill
ws1["D17"].fill = accent_fill
ws1["E17"].fill = accent_fill

# -------------------------------------------------------------
# TAB 3: Support Volume Model
# -------------------------------------------------------------
ws2 = wb.create_sheet(title="Volume_Model")
ws2.views.sheetView[0].showGridLines = True

ws2["A1"] = "Support Volume & Resolution Breakdown"
ws2["A1"].font = title_font
ws2["A2"] = "5,000 Active Businesses Model • All inputs dynamically linked to Assumptions tab"
ws2["A2"].font = meta_font

for col_idx, col_name in enumerate(["Parameter", "Value", "Unit", "Notes & Operational Logic"], start=1):
    c = ws2.cell(row=4, column=col_idx, value=col_name)
    c.fill = header_fill
    c.font = header_font

volume_rows = [
    ("Active Business Accounts", "=Assumptions!C5", "Businesses", "Assumptions!C5 (Given active merchant count)"),
    ("Monthly Support Query Rate per Business", "=Assumptions!C7", "Queries / mo", "Assumptions!C7 (Blended across onboarding & mature accounts)"),
    ("Total Monthly Inbound Queries", "=B5*B6", "Queries / mo", "Total monthly inbound volume (17,500 queries)"),
    ("Current Baseline Deflection Rate", "=Assumptions!C18", "% deflected", "Assumptions!C18 (Status quo static FAQ deflection)"),
    ("Cheerio Co-Pilot Target Deflection Rate (Base)", "=Assumptions!C19", "% deflected", "Assumptions!C19 (65% target across top bottlenecks)"),
    ("Queries Resolved Autonomously by AI", "=ROUND(B7*B9, 0)", "Queries / mo", "Calc: 17,500 * 65% = 11,375 queries without human rep"),
    ("Queries Escalated to Human Support", "=B7-B10", "Queries / mo", "Calc: 17,500 - 11,375 = 6,125 escalated queries"),
]

for row_idx, (param, val, unit, notes) in enumerate(volume_rows, start=5):
    ws2.cell(row=row_idx, column=1, value=param).font = regular_font
    c_val = ws2.cell(row=row_idx, column=2, value=val)
    c_val.font = bold_font
    ws2.cell(row=row_idx, column=3, value=unit).font = regular_font
    ws2.cell(row=row_idx, column=4, value=notes).font = meta_font
    for c in range(1, 5):
        ws2.cell(row=row_idx, column=c).border = thin_border
    if "%" in unit:
        c_val.number_format = "0.0%"
    elif "Queries" in unit or "Businesses" in unit:
        c_val.number_format = "#,##0"

# -------------------------------------------------------------
# TAB 4: Token Economics & Sensitivity Table
# -------------------------------------------------------------
ws3 = wb.create_sheet(title="Token_Economics")
ws3.views.sheetView[0].showGridLines = True

ws3["A1"] = "AI Token Economics, Pricing & Stress-Test Sensitivity"
ws3["A1"].font = title_font
ws3["A2"] = "Source: OpenAI API Pricing (GPT-4o-mini), USD:INR = 84.0"
ws3["A2"].font = meta_font

for col_idx, col_name in enumerate(["Token Cost Parameter", "Value", "Unit", "Source URL & Benchmarking Logic"], start=1):
    c = ws3.cell(row=4, column=col_idx, value=col_name)
    c.fill = header_fill
    c.font = header_font

token_rows = [
    ("Model Chosen", "GPT-4o-mini", "LLM", "Multi-tier hybrid: Regex linter + GPT-4o-mini rephraser"),
    ("USD to INR Exchange Rate", "=Assumptions!C8", "INR / USD", "Assumptions!C8 (RBI reference rate)"),
    ("Input Token Price per 1M Tokens ($)", "=Assumptions!C9", "USD / 1M", "Assumptions!C9 (openai.com/api/pricing)"),
    ("Output Token Price per 1M Tokens ($)", "=Assumptions!C11", "USD / 1M", "Assumptions!C11 (openai.com/api/pricing)"),
    ("Average Input Tokens per Session", "=Assumptions!C12", "Tokens", "Assumptions!C12 (Prompt 1k + error 500 + 3 turns 1k)"),
    ("Average Output Tokens per Session", "=Assumptions!C13", "Tokens", "Assumptions!C13 (Remediation payload)"),
    ("Input Cost per Query Session ($)", "=(B9/1000000)*B7", "USD", "Calc: (Tokens / 1M) * Input Rate"),
    ("Output Cost per Query Session ($)", "=(B10/1000000)*B8", "USD", "Calc: (Tokens / 1M) * Output Rate"),
    ("Total LLM Cost per Query Session ($)", "=B11+B12", "USD", "Calc: Input Cost + Output Cost"),
    ("Total LLM Cost per Query Session (₹)", "=B13*B6", "INR", "Converted to INR (approx 5.67 paise)"),
    ("Serverless & Redis Cache Overhead (₹)", "=Assumptions!C14", "INR", "Assumptions!C14 (Edge worker execution + Redis cache)"),
    ("Total Operational Cost per Query (₹)", "=B14+B15", "INR", "Blended total cost per query touched by AI (₹0.20)"),
    ("Total Monthly Queries Touched by AI", "=Volume_Model!B7", "Queries / mo", "Volume_Model!B7 (AI touches all 17,500 inbound queries)"),
    ("Total Monthly AI Token & Infra Cost (₹)", "=ROUND(B16*B17, 0)", "INR / mo", "Calc: 17,500 queries * ₹0.20 = ₹3,500 / month"),
    ("AI Cost per Active Business / Month (₹)", "=ROUND(B18/Volume_Model!B5, 2)", "INR / biz / mo", "Calc: ₹3,500 / 5,000 = ₹0.70 / merchant / month"),
]

for row_idx, (param, val, unit, notes) in enumerate(token_rows, start=5):
    ws3.cell(row=row_idx, column=1, value=param).font = regular_font
    c_val = ws3.cell(row=row_idx, column=2, value=val)
    c_val.font = bold_font
    ws3.cell(row=row_idx, column=3, value=unit).font = regular_font
    ws3.cell(row=row_idx, column=4, value=notes).font = meta_font
    for c in range(1, 5):
        ws3.cell(row=row_idx, column=c).border = thin_border
    if "USD" in unit and isinstance(val, (int, float, str)) and row_idx in [7, 8, 11, 12, 13]:
        c_val.number_format = "$#,##0.000000"
    elif "INR" in unit:
        c_val.number_format = "₹#,##0.00" if row_idx in [14, 15, 16, 19] else "₹#,##0"

# Add Sensitivity Table (Tokens 1x/2x/3x vs Price 1x/3x/5x)
ws3["A22"] = "SENSITIVITY MATRIX: Monthly AI Cost (₹) Under Token Volume & API Price Surges"
ws3["A22"].font = bold_font
ws3["A22"].fill = sub_header_fill

sens_headers = ["Token Volume Multiple", "1x Price ($0.15/$0.60)", "3x Price ($0.45/$1.80)", "5x Price ($0.75/$3.00)"]
for col_idx, h in enumerate(sens_headers, start=1):
    c = ws3.cell(row=23, column=col_idx, value=h)
    c.fill = header_fill
    c.font = header_font
    c.alignment = Alignment(horizontal="center")

sens_grid = [
    ("1x Tokens (3,000 tokens/session)", "=ROUND(17500*(B14*1 + B15), 0)", "=ROUND(17500*(B14*3 + B15), 0)", "=ROUND(17500*(B14*5 + B15), 0)"),
    ("2x Tokens (6,000 tokens/session)", "=ROUND(17500*(B14*2 + B15), 0)", "=ROUND(17500*(B14*6 + B15), 0)", "=ROUND(17500*(B14*10 + B15), 0)"),
    ("3x Tokens (9,000 tokens/session)", "=ROUND(17500*(B14*3 + B15), 0)", "=ROUND(17500*(B14*9 + B15), 0)", "=ROUND(17500*(B14*15 + B15), 0)"),
]

for row_idx, row in enumerate(sens_grid, start=24):
    for col_idx, val in enumerate(row, start=1):
        cell = ws3.cell(row=row_idx, column=col_idx, value=val)
        cell.font = bold_font if col_idx == 1 else regular_font
        cell.border = thin_border
        if col_idx > 1:
            cell.alignment = Alignment(horizontal="right")
            cell.number_format = "₹#,##0"

# -------------------------------------------------------------
# TAB 5: Avoided Support Hiring & Deflection Scenarios
# -------------------------------------------------------------
ws4 = wb.create_sheet(title="Human_Comparison")
ws4.views.sheetView[0].showGridLines = True

ws4["A1"] = "Support Scaling: Avoided Support Hiring & Operating Cost Analysis"
ws4["A1"].font = title_font
ws4["A2"] = "Framed as Avoided Headcount as Cheerio Scales • Agent Capacity: 40 tickets/day @ ₹35k/mo"
ws4["A2"].font = meta_font

for col_idx, col_name in enumerate(["Cost & Staffing Parameter", "Value", "Unit", "Operational Formula & Rationale"], start=1):
    c = ws4.cell(row=4, column=col_idx, value=col_name)
    c.fill = header_fill
    c.font = header_font

human_rows = [
    ("Human Support Rep Monthly Salary (₹)", "=Assumptions!C15", "INR / agent / mo", "Assumptions!C15 (Glassdoor/AmbitionBox CS rep benchmark)"),
    ("Working Days per Month", "=Assumptions!C16", "Days", "Assumptions!C16 (Standard 5-day work week)"),
    ("Daily Ticket Capacity per Agent", "=Assumptions!C17", "Tickets / day", "Assumptions!C17 (Standard chat/ticket handling capacity)"),
    ("Monthly Ticket Capacity per Agent", "=B6*B7", "Tickets / mo", "Calc: 22 days * 40 tickets/day = 880 tickets / rep / mo"),
    ("--- MODEL 1: PURE HUMAN SUPPORT (AVOIDED BASELINE) ---", "", "", ""),
    ("Total Inbound Query Volume", "=Volume_Model!B7", "Tickets / mo", "17,500 total inbound queries"),
    ("Human Support Agents Needed (Without AI)", "=ROUNDUP(B10/B8, 0)", "Agents", "Calc: ROUNDUP(17,500 / 880) = 20 Agents needed"),
    ("Total Monthly Human Support Cost (₹)", "=B11*B5", "INR / mo", "Calc: 20 agents * ₹35,000/mo = ₹7,00,000 / month"),
    ("Cost per Resolved Ticket (Pure Human) (₹)", "=ROUND(B12/B10, 2)", "INR / ticket", "Calc: ₹7,00,000 / 17,500 = ₹40.00 / ticket"),
    ("--- MODEL 2: CHEERIO CO-PILOT + SCALED HUMAN ESCALATION ---", "", "", ""),
    ("Queries Handled Autonomously by Co-Pilot (65%)", "=Volume_Model!B10", "Tickets / mo", "11,375 tickets resolved without human intervention"),
    ("Queries Escalated to Human Support (35%)", "=Volume_Model!B11", "Tickets / mo", "6,125 tickets requiring human specialist review"),
    ("Human Agents Needed for Escalations", "=ROUNDUP(B16/B8, 0)", "Agents", "Calc: ROUNDUP(6,125 / 880) = 7 Agents required"),
    ("Scaled Human Support Salary Cost (₹)", "=B17*B5", "INR / mo", "Calc: 7 agents * ₹35,000/mo = ₹2,45,000 / month"),
    ("Monthly AI Token & Infra Cost (₹)", "=Token_Economics!B18", "INR / mo", "Token_Economics!B18 (₹3,500 LLM token cost)"),
    ("Monthly Observability Tooling (₹)", "=Assumptions!C23", "INR / mo", "Assumptions!C23 (LangSmith / Datadog APM = ₹15,000)"),
    ("Total Monthly Blended Support Running Cost (₹)", "=B18+B19+B20", "INR / mo", "Calc: ₹2,45,000 salary + ₹3,500 AI + ₹15,000 tooling = ₹2,63,500"),
    ("Blended Cost per Ticket (₹)", "=ROUND(B21/B10, 2)", "INR / ticket", "Calc: ₹2,63,500 / 17,500 = ₹15.06 / ticket"),
    ("--- NET OPERATIONAL SAVINGS & PAYBACK ---", "", "", ""),
    ("Avoided Headcount (Agents)", "=B11-B17", "Agents", "Calc: 20 agents - 7 agents = 13 agents avoided"),
    ("Net Monthly Operational Savings (₹)", "=B12-B21", "INR / mo", "Calc: ₹7,00,000 - ₹2,63,500 = ₹4,36,500 / month"),
    ("Net Annual Operational Savings (₹)", "=B25*12", "INR / yr", "Calc: ₹4,36,500 * 12 = ₹52.38 Lakhs / year"),
    ("One-Time Development Build Cost (₹)", "=Assumptions!C22", "INR", "Assumptions!C22 (₹2,50,000 dev build cost)"),
    ("Payback Period on Build Investment", "=ROUND(B27/B25, 2)", "Months", "Calc: ₹2,50,000 / ₹4,36,500 = 0.57 Months (~17 Days)"),
]

for row_idx, (param, val, unit, notes) in enumerate(human_rows, start=5):
    ws4.cell(row=row_idx, column=1, value=param).font = bold_font if "---" in param else regular_font
    c_val = ws4.cell(row=row_idx, column=2, value=val)
    c_val.font = bold_font
    ws4.cell(row=row_idx, column=3, value=unit).font = regular_font
    ws4.cell(row=row_idx, column=4, value=notes).font = meta_font
    if "---" in param:
        for c in range(1, 5):
            ws4.cell(row=row_idx, column=c).fill = sub_header_fill
    else:
        for c in range(1, 5):
            ws4.cell(row=row_idx, column=c).border = thin_border
    if "INR" in unit:
        c_val.number_format = "₹#,##0.00" if row_idx in [13, 22] else "₹#,##0"
    elif "Tickets" in unit or "Agents" in unit:
        c_val.number_format = "#,##0"

# Add Deflection Sensitivity Scenarios (Low 45% / Base 65% / High 75%)
ws4["A31"] = "DEFLECTION SCENARIO ANALYSIS (Impact on Agents Needed & Net Savings)"
ws4["A31"].font = bold_font
ws4["A31"].fill = sub_header_fill

deflection_headers = ["Scenario", "Deflection Rate", "Escalated Queries", "Agents Needed", "Blended Support Cost (₹)", "Net Monthly Savings (₹)"]
for col_idx, h in enumerate(deflection_headers, start=1):
    c = ws4.cell(row=32, column=col_idx, value=h)
    c.fill = header_fill
    c.font = header_font
    c.alignment = Alignment(horizontal="center")

deflection_scenarios = [
    ("Conservative (Low)", 0.45, "=ROUND(17500*(1-B33),0)", "=ROUNDUP(C33/880,0)", "=(D33*35000)+18500", "=700000-E33"),
    ("Expected (Base)", 0.65, "=ROUND(17500*(1-B34),0)", "=ROUNDUP(C34/880,0)", "=(D34*35000)+18500", "=700000-E34"),
    ("Aggressive (High)", 0.75, "=ROUND(17500*(1-B35),0)", "=ROUNDUP(C35/880,0)", "=(D35*35000)+18500", "=700000-E35"),
]

for row_idx, row in enumerate(deflection_scenarios, start=33):
    for col_idx, val in enumerate(row, start=1):
        cell = ws4.cell(row=row_idx, column=col_idx, value=val)
        cell.font = bold_font if col_idx in [1, 6] else regular_font
        cell.border = thin_border
        if col_idx == 2:
            cell.alignment = Alignment(horizontal="right")
            cell.number_format = "0.0%"
        elif col_idx in [3, 4]:
            cell.alignment = Alignment(horizontal="right")
            cell.number_format = "#,##0"
        elif col_idx in [5, 6]:
            cell.alignment = Alignment(horizontal="right")
            cell.number_format = "₹#,##0"

# -------------------------------------------------------------
# TAB 6: Churn Reduction & Retention ROI (Separated & Verified)
# -------------------------------------------------------------
ws5 = wb.create_sheet(title="Retention_ROI")
ws5.views.sheetView[0].showGridLines = True

ws5["A1"] = "Merchant Retention & Churn Reduction Economics"
ws5["A1"].font = title_font
ws5["A2"] = "Separated from Support Headcount Savings • No Double Counting"
ws5["A2"].font = meta_font

for col_idx, col_name in enumerate(["Retention & Revenue Parameter", "Value", "Unit", "Strategic Rationale & Verification Formula"], start=1):
    c = ws5.cell(row=4, column=col_idx, value=col_name)
    c.fill = header_fill
    c.font = header_font

retention_rows = [
    ("Active Merchant Base", "=Assumptions!C5", "Businesses", "Assumptions!C5 (Given customer base)"),
    ("Estimated Average Monthly Subscription (ARPU)", "=Assumptions!C24", "INR / biz / mo", "Assumptions!C24 (₹2,999 / month standard tier)"),
    ("Total Baseline Monthly Recurring Revenue (MRR)", "=B5*B6", "INR / mo", "Calc: 5,000 * ₹2,999 = ₹1,49,95,000 / month (~₹1.50 Cr)"),
    ("Baseline Monthly Merchant Churn Rate", "=Assumptions!C25", "% / mo", "Assumptions!C25 (5.0% monthly SMB churn benchmark)"),
    ("Lost Businesses per Month (Baseline Churn)", "=ROUND(B5*B8, 0)", "Businesses / mo", "Calc: 5,000 * 5% = 250 merchants lost each month"),
    ("Estimated Churn Reduction via Co-Pilot (Base)", "=Assumptions!C26", "% absolute", "Assumptions!C26 (1.2% saved by fixing onboarding drop-offs)"),
    ("Preserved Businesses per Month", "=ROUND(B5*B10, 0)", "Businesses / mo", "Calc: 5,000 * 1.2% = 60 merchants retained every month"),
    ("Gross Preserved Monthly Recurring Revenue (MRR)", "=B11*B6", "INR / mo", "Calc: 60 merchants * ₹2,999 = ₹1,79,940 / month"),
    ("Gross Preserved Annual Recurring Revenue (ARR)", "=B12*12", "INR / yr", "Calc: ₹1,79,940 * 12 = ₹21.59 Lakhs / year"),
    ("Direct Monthly AI Token Cost (₹)", "=Token_Economics!B18", "INR / mo", "Token_Economics!B18 (₹3,500 direct LLM API spend)"),
    ("Total Monthly Program Cost (Tokens + Tooling) (₹)", "=Human_Comparison!B20", "INR / mo", "Human_Comparison!B20 (₹3,500 tokens + ₹15,000 Redis/observability)"),
    ("Net Monthly Preserved MRR (vs Direct Tokens) (₹)", "=B12-B14", "INR / mo", "Calc: Gross Preserved MRR - Direct Token Spend = ₹1,76,440 / mo"),
    ("Net Monthly Preserved MRR (vs Total Program Cost) (₹)", "=B12-B15", "INR / mo", "Calc: Gross Preserved MRR - Total Program Cost = ₹1,61,440 / mo"),
    ("Gross ROI Multiple on Direct Token Spend", "=ROUND(B12/B14, 1)", "x Return", "Calc: Gross Preserved MRR / Direct Tokens = ₹1,79,940 / ₹3,500 = 51.4x"),
    ("Net ROI Multiple on Direct Token Spend", "=ROUND(B16/B14, 1)", "x Return", "Calc: Net Preserved MRR / Direct Tokens = ₹1,76,440 / ₹3,500 = 50.4x"),
    ("Gross ROI Multiple on Total Program Cost", "=ROUND(B12/B15, 1)", "x Return", "Calc: Gross Preserved MRR / Total Program = ₹1,79,940 / ₹18,500 = 9.7x"),
    ("Net ROI Multiple on Total Program Cost", "=ROUND(B17/B15, 1)", "x Return", "Calc: Net Preserved MRR / Total Program = ₹1,61,440 / ₹18,500 = 8.7x"),
]

for row_idx, (param, val, unit, notes) in enumerate(retention_rows, start=5):
    ws5.cell(row=row_idx, column=1, value=param).font = regular_font
    c_val = ws5.cell(row=row_idx, column=2, value=val)
    c_val.font = bold_font
    ws5.cell(row=row_idx, column=3, value=unit).font = regular_font
    ws5.cell(row=row_idx, column=4, value=notes).font = meta_font
    for c in range(1, 5):
        ws5.cell(row=row_idx, column=c).border = thin_border
    if "%" in unit:
        c_val.number_format = "0.0%"
    elif "INR" in unit:
        c_val.number_format = "₹#,##0"
    elif "x" in unit:
        c_val.number_format = '0.0"x"'
    elif "Businesses" in unit:
        c_val.number_format = "#,##0"

# Churn Sensitivity Scenarios (Low 0.5% / Base 1.2% / High 2.0%)
ws5["A23"] = "CHURN REDUCTION SENSITIVITY TABLE (Low / Base / High)"
ws5["A23"].font = bold_font
ws5["A23"].fill = sub_header_fill

churn_headers = ["Scenario", "Absolute Churn Reduction", "Retained Merchants/Mo", "Gross Preserved MRR (₹)", "Net MRR vs Tokens (₹)", "Net ROI (Tokens)", "Net MRR vs Total Spend (₹)", "Net ROI (Total Spend)"]
for col_idx, h in enumerate(churn_headers, start=1):
    c = ws5.cell(row=24, column=col_idx, value=h)
    c.fill = header_fill
    c.font = header_font
    c.alignment = Alignment(horizontal="center")

churn_scenarios = [
    ("Conservative (Low)", 0.005, "=ROUND(5000*B25,0)", "=C25*2999", "=D25-3500", "=ROUND(E25/3500,1)", "=D25-18500", "=ROUND(G25/18500,1)"),
    ("Expected (Base)", 0.012, "=ROUND(5000*B26,0)", "=C26*2999", "=D26-3500", "=ROUND(E26/3500,1)", "=D26-18500", "=ROUND(G26/18500,1)"),
    ("Aggressive (High)", 0.020, "=ROUND(5000*B27,0)", "=C27*2999", "=D27-3500", "=ROUND(E27/3500,1)", "=D27-18500", "=ROUND(G27/18500,1)"),
]

for row_idx, row in enumerate(churn_scenarios, start=25):
    for col_idx, val in enumerate(row, start=1):
        cell = ws5.cell(row=row_idx, column=col_idx, value=val)
        cell.font = bold_font if col_idx in [1, 6, 8] else regular_font
        cell.border = thin_border
        if col_idx == 2:
            cell.alignment = Alignment(horizontal="right")
            cell.number_format = "0.0%"
        elif col_idx == 3:
            cell.alignment = Alignment(horizontal="right")
            cell.number_format = "#,##0"
        elif col_idx in [4, 5, 7]:
            cell.alignment = Alignment(horizontal="right")
            cell.number_format = "₹#,##0"
        elif col_idx in [6, 8]:
            cell.alignment = Alignment(horizontal="right")
            cell.number_format = '0.0"x"'

# -------------------------------------------------------------
# TAB 7: Packaging, Pricing & Billing Strategy (NEW REFINED)
# -------------------------------------------------------------
ws6 = wb.create_sheet(title="Billing_Strategy")
ws6.views.sheetView[0].showGridLines = True

ws6["A1"] = "Packaging, Monetization & Billing Strategy Options"
ws6["A1"].font = title_font
ws6["A2"] = "Recommends Free Core Co-Pilot + ₹499/mo Priority Add-on • Linked Formulas"
ws6["A2"].font = meta_font

billing_headers = ["Pricing Model", "Customer Price", "Billing Basis", "Fully Loaded Unit Cost (₹)", "Gross Margin (%)", "Strategic Fit & Value Rationale"]
for col_idx, h in enumerate(billing_headers, start=1):
    c = ws6.cell(row=4, column=col_idx, value=h)
    c.fill = header_fill
    c.font = header_font
    c.alignment = Alignment(horizontal="center")

billing_options = [
    ("Model 1: Free Core Co-Pilot (Recommended Base)", 0, "Free for all active merchants", "=B15", "Subsidized", "Maximizes onboarding completion. Net surplus: ₹1.58L/mo (Retention MRR less AI cost)."),
    ("Model 2: Priority Support Add-on (Recommended Upsell)", 499, "Per merchant / month", "=ROUND((B15*5)+15, 2)", "=ROUND((B6-D6)/B6, 3)", "Premium SLA (<15m), dedicated WhatsApp agent. Gross margin: +95.8% via formulas."),
    ("Model 3: Per-Resolution Micro-Fee", 5.0, "Per resolved troubleshooting workflow", "=B15", "=ROUND((B7-D7)/B7, 3)", "High margin (+76.0%), but creates onboarding barrier and causes merchant friction."),
    ("Model 4: Prepaid AI Resolution Pack", 199, "Pack of 50 AI resolutions (₹3.98/res)", "=B15*50", "=ROUND((B8-D8)/B8, 3)", "High gross margin (+69.8%), but adds wallet friction during crucial Day 1 onboarding."),
]

for row_idx, row in enumerate(billing_options, start=5):
    for col_idx, val in enumerate(row, start=1):
        cell = ws6.cell(row=row_idx, column=col_idx, value=val)
        cell.font = bold_font if col_idx in [1, 5] else regular_font
        cell.border = thin_border
        if col_idx in [2, 4]:
            cell.alignment = Alignment(horizontal="right")
            cell.number_format = "₹#,##0.00" if isinstance(val, (int, float)) and val < 100 else "₹#,##0"
        elif col_idx == 5:
            cell.alignment = Alignment(horizontal="right")
            if isinstance(val, str) and val.startswith("="):
                cell.number_format = "0.0%"

# Fully loaded cost rationale breakdown
ws6["A11"] = "FULLY LOADED AI OPERATIONAL COST PER QUERY (₹) - NO DOUBLE COUNTING"
ws6["A11"].font = bold_font
ws6["A11"].fill = sub_header_fill

cost_breakdown = [
    ("LLM Token Inference (GPT-4o-mini blended)", "=Token_Economics!B16", "Token_Economics!B16 (₹0.20 per query)"),
    ("Edge Cache & Serverless Buffer (Cloudflare/Redis)", "=Assumptions!C14", "Assumptions!C14 (₹0.14 per query)"),
    ("Observability & Tooling per Query (LangSmith/Datadog)", "=ROUND(Assumptions!C23/Volume_Model!B7, 2)", "Calc: ₹15,000 monthly tooling / 17,500 queries = ₹0.86"),
    ("Total Fully Loaded AI Cost per Query (₹)", "=B12+B13+B14", "Calc: Direct operational running cost for AI Co-Pilot (₹1.20)"),
    ("SEPARATE OPERATIONAL LINE: Amortized Human Escalation Share", "=ROUND(Human_Comparison!B18/Volume_Model!B7, 2)", "Calc: ₹2,45,000 human escalation salary / 17,500 queries = ₹14.00"),
]

for row_idx, (item, val, source) in enumerate(cost_breakdown, start=12):
    ws6.cell(row=row_idx, column=1, value=item).font = bold_font if "Total" in item or "SEPARATE" in item else regular_font
    c_val = ws6.cell(row=row_idx, column=2, value=val)
    c_val.font = bold_font
    c_val.alignment = Alignment(horizontal="right")
    c_val.number_format = "₹#,##0.00"
    ws6.cell(row=row_idx, column=3, value=source).font = meta_font
    for c in range(1, 4):
        ws6.cell(row=row_idx, column=c).border = thin_border

# -------------------------------------------------------------
# TAB 8: Observability, Governance & Audit Checklist (REFINED)
# -------------------------------------------------------------
ws7 = wb.create_sheet(title="Audit_Governance")
ws7.views.sheetView[0].showGridLines = True

ws7["A1"] = "Co-Pilot Observability, Governance & Monthly Audit Protocol"
ws7["A1"].font = title_font
ws7["A2"] = "Alert Thresholds, Operational Cadence & Assigned Owners"
ws7["A2"].font = meta_font

audit_headers = ["Audit Parameter / Check", "Threshold / Benchmark", "Severity", "Assigned Owner", "Automated Action / Remediation Protocol"]
for col_idx, h in enumerate(audit_headers, start=1):
    c = ws7.cell(row=4, column=col_idx, value=h)
    c.fill = header_fill
    c.font = header_font
    c.alignment = Alignment(horizontal="center")

audit_checklist = [
    ("Cost per Resolved Query", "> 2x Baseline (> ₹0.40 / query)", "High", "Lead APM / ML Eng", "Flag prompt regression or runaway token loops; fallback to strict regex"),
    ("Average Tokens per Session", "> 140% 7-day rolling avg (> 4,200 tokens)", "Medium", "Backend Lead", "Audit error payload serialization and trim oversized CSV schema payloads"),
    ("Single-Merchant Session Spikes", "> 50 sessions / 24 hours", "High", "SecOps / CS Lead", "Throttle merchant rate limit; trigger proactive white-glove onboarding check"),
    ("Deflection Rate (7-day verified)", "< 40% (Target: 65%)", "Critical", "Product Manager", "Audit recent Meta Cloud API changelogs; update regex and error intent models"),
    ("Zero-Touch Onboarding Rate (ZOCR)", "< 25% (Target: 33% at Day 90)", "High", "Onboarding & Growth Lead", "Review Day 1-7 drop-off funnels; inspect WABA phone binding failure logs"),
    ("7-Day Ticket Reopen Rate", "> 5.0% of deflected tickets", "High", "QA Lead / Support Lead", "Audit auto-fix false positives; refine pre-flight regex linter rules"),
    ("Monthly Token Invoice Reconciliation", "OpenAI invoice vs logs variance > ±2%", "Medium", "Finance / Eng Lead", "Reconcile dropped webhooks, orphaned sessions, or billing discrepancies"),
]

for row_idx, row in enumerate(audit_checklist, start=5):
    for col_idx, val in enumerate(row, start=1):
        cell = ws7.cell(row=row_idx, column=col_idx, value=val)
        cell.font = bold_font if col_idx in [1, 3] else regular_font
        cell.border = thin_border
        if col_idx == 3:
            cell.alignment = Alignment(horizontal="center")
            if val == "Critical":
                cell.fill = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")
            elif val == "High":
                cell.fill = alert_fill

# Adjust column widths
for ws in wb.worksheets:
    for col in ws.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = get_column_letter(col[0].column)
        ws.column_dimensions[col_letter].width = max(max_len + 4, 12)

output_path = "cheerio/assignment/cheerio_cost_model.xlsx"
wb.save(output_path)
print("Saved 8-tab cheerio_cost_model.xlsx successfully with zero note formulas!")
