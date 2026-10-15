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

double_bottom = Border(
    bottom=Side(style='double', color="1E293B"),
    top=Side(style='thin', color="E2E8F0")
)

# -------------------------------------------------------------
# TAB 1: Executive Summary
# -------------------------------------------------------------
ws1 = wb.active
ws1.title = "Executive_Summary"
ws1.views.sheetView[0].showGridLines = True

ws1["A1"] = "Cheerio AI — Customer Support Scaling (Assignment A)"
ws1["A1"].font = title_font
ws1["A2"] = "Financial Model & Unit Economics • Candidate: Saksham Gupta (saksham77779@gmail.com)"
ws1["A2"].font = meta_font

summary_headers = ["Key Metric", "Baseline (Human Only)", "With Cheerio Co-Pilot", "Delta / Impact", "Formula / Source"]
for col_idx, h in enumerate(summary_headers, start=1):
    cell = ws1.cell(row=4, column=col_idx, value=h)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center" if col_idx > 1 else "left", vertical="center")

kpi_data = [
    ("Active Merchant Base", 5000, 5000, "0", "Assignment Brief specification"),
    ("Monthly Support Queries", 17500, 17500, "0", "Volume_Model!B6"),
    ("Autonomous Ticket Deflection Rate", 0.12, 0.65, "+53.0%", "Target deflection across 5 bottlenecks"),
    ("Human Support Headcount Needed", 20, 7, "-13 Agents", "Human_Comparison!B11 vs B16"),
    ("Total Monthly Support Cost (₹)", 700000, 248500, "-₹4,51,500", "Human_Comparison!B12 vs B19"),
    ("Cost per Resolved Ticket (₹)", 40.00, 14.20, "-₹25.80 (-64.5%)", "Human_Comparison!B13 vs B20"),
    ("Monthly AI Infrastructure Cost (₹)", 0, 3500, "+₹3,500", "Token_Economics!B16"),
    ("AI Cost per Active Business / Month (₹)", 0, 0.70, "₹0.70 / mo", "Token_Economics!B17"),
    ("Net Monthly Operational Savings (₹)", 0, 451500, "+₹4,51,500 / mo", "Human_Comparison!B21 (₹54.18L / yr)"),
    ("Merchant Churn Reduction ROI", "-", "51.4x", "51.4x Return", "Retention_ROI!B12 (1.2% churn saved)"),
]

for row_idx, row in enumerate(kpi_data, start=5):
    for col_idx, val in enumerate(row, start=1):
        cell = ws1.cell(row=row_idx, column=col_idx, value=val)
        cell.font = bold_font if col_idx in [1, 4] else regular_font
        cell.border = thin_border
        if col_idx in [2, 3]:
            cell.alignment = Alignment(horizontal="right")
            if "Rate" in row[0]:
                cell.number_format = "0.0%"
            elif "Cost" in row[0] or "Savings" in row[0]:
                cell.number_format = "₹#,##0"
            elif isinstance(val, (int, float)):
                cell.number_format = "#,##0" if val >= 10 else "0.00"

# Highlight net savings
ws1["A13"].fill = accent_fill
ws1["B13"].fill = accent_fill
ws1["C13"].fill = accent_fill
ws1["D13"].fill = accent_fill
ws1["E13"].fill = accent_fill

# -------------------------------------------------------------
# TAB 2: Support Volume Model
# -------------------------------------------------------------
ws2 = wb.create_sheet(title="Volume_Model")
ws2.views.sheetView[0].showGridLines = True

ws2["A1"] = "Support Volume & Resolution Breakdown"
ws2["A1"].font = title_font
ws2["A2"] = "5,000 Active Businesses Guesstimate Model"
ws2["A2"].font = meta_font

ws2["A4"] = "Parameter"
ws2["B4"] = "Value"
ws2["C4"] = "Unit"
ws2["D4"] = "Notes / Rationale"
for col in ["A4", "B4", "C4", "D4"]:
    ws2[col].fill = header_fill
    ws2[col].font = header_font

volume_rows = [
    ("Active Business Accounts", 5000, "Businesses", "Given in assignment brief"),
    ("Monthly Support Query Rate per Business", 3.5, "Queries / mo", "Assumed: 5-7 queries for new onboarding, 1-2 for mature accounts"),
    ("Total Monthly Inbound Queries", "=B5*B6", "Queries / mo", "Total query volume across all channels"),
    ("Current Baseline Deflection Rate", 0.12, "% deflected", "Current static FAQs / doc deflection"),
    ("Cheerio Co-Pilot Target Deflection Rate", 0.65, "% deflected", "Target across Top 5 bottlenecks within 90 days"),
    ("Queries Resolved Autonomously by AI", "=ROUND(B7*B9, 0)", "Queries / mo", "Zero human agent intervention"),
    ("Queries Escalated to Human Support", "=B7-B10", "Queries / mo", "Complex edge cases & policy disputes"),
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
# TAB 3: Token Economics
# -------------------------------------------------------------
ws3 = wb.create_sheet(title="Token_Economics")
ws3.views.sheetView[0].showGridLines = True

ws3["A1"] = "AI Token Economics & Infrastructure Running Cost"
ws3["A1"].font = title_font
ws3["A2"] = "Source: OpenAI API Pricing (GPT-4o-mini), USD:INR = 84.0"
ws3["A2"].font = meta_font

ws3["A4"] = "Token Cost Parameter"
ws3["B4"] = "Value"
ws3["C4"] = "Unit"
ws3["D4"] = "Source / Benchmark"
for col in ["A4", "B4", "C4", "D4"]:
    ws3[col].fill = header_fill
    ws3[col].font = header_font

token_rows = [
    ("Model Chosen", "GPT-4o-mini", "LLM", "Multi-tier hybrid: Regex for syntax + GPT-4o-mini for copy rephrasing"),
    ("USD to INR Exchange Rate", 84.0, "INR / USD", "Current Forex standard benchmark"),
    ("Input Token Price per 1M Tokens ($)", 0.15, "USD / 1M", "Official OpenAI API pricing (openai.com/pricing)"),
    ("Output Token Price per 1M Tokens ($)", 0.60, "USD / 1M", "Official OpenAI API pricing (openai.com/pricing)"),
    ("Average Input Tokens per Session", 2500, "Tokens", "System prompt (1k) + error JSON (500) + 3 user turns (1k)"),
    ("Average Output Tokens per Session", 500, "Tokens", "Diagnostic explanation + suggested template copy payload"),
    ("Input Cost per Query Session ($)", "=(B9/1000000)*B7", "USD", "= (Tokens / 1M) * Input Rate"),
    ("Output Cost per Query Session ($)", "=(B10/1000000)*B8", "USD", "= (Tokens / 1M) * Output Rate"),
    ("Total LLM Cost per Query Session ($)", "=B11+B12", "USD", "= Input Cost + Output Cost"),
    ("Total LLM Cost per Query Session (₹)", "=B13*B6", "INR", "Converted to INR (approx 5.7 paise)"),
    ("Serverless & Redis Cache Overhead (₹)", 0.1433, "INR", "Cloudflare Workers execution + Redis semantic cache buffer"),
    ("Total Operational Cost per Query (₹)", "=B14+B15", "INR", "Blended total cost per troubleshooting query"),
    ("Total Monthly Queries Handled", "=Volume_Model!B7", "Queries / mo", "Volume_Model!B7"),
    ("Total Monthly AI Infra Cost (₹)", "=ROUND(B16*B17, 0)", "INR / mo", "17,500 queries * ₹0.20"),
    ("AI Cost per Active Business / Month (₹)", "=ROUND(B18/Volume_Model!B5, 2)", "INR / biz / mo", "₹3,500 / 5,000 active businesses"),
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

# -------------------------------------------------------------
# TAB 4: Human vs AI Support Comparison
# -------------------------------------------------------------
ws4 = wb.create_sheet(title="Human_Comparison")
ws4.views.sheetView[0].showGridLines = True

ws4["A1"] = "Human Support vs. Cheerio Co-Pilot Cost Analysis"
ws4["A1"].font = title_font
ws4["A2"] = "Agent Capacity: 40 tickets/day • Indian B2B SaaS Salary: ₹35,000/month"
ws4["A2"].font = meta_font

ws4["A4"] = "Cost & Staffing Parameter"
ws4["B4"] = "Value"
ws4["C4"] = "Unit"
ws4["D4"] = "Formula / Rationale"
for col in ["A4", "B4", "C4", "D4"]:
    ws4[col].fill = header_fill
    ws4[col].font = header_font

human_rows = [
    ("Human Support Rep Monthly Salary (₹)", 35000, "INR / agent / mo", "Indian B2B SaaS customer support benchmark (Glassdoor/AmbitionBox)"),
    ("Working Days per Month", 22, "Days", "Standard 5-day work week"),
    ("Daily Ticket Capacity per Agent", 40, "Tickets / day", "Standard chat/ticket handling capacity"),
    ("Monthly Ticket Capacity per Agent", "=B6*B7", "Tickets / mo", "= 22 days * 40 tickets/day (880 tickets/mo)"),
    ("--- MODEL 1: PURE HUMAN SUPPORT ---", "", "", ""),
    ("Total Inbound Query Volume", "=Volume_Model!B7", "Tickets / mo", "17,500 total queries"),
    ("Human Support Agents Needed", "=ROUNDUP(B10/B8, 0)", "Agents", "= ROUNDUP(17,500 / 880) = 20 Agents"),
    ("Total Monthly Human Support Cost (₹)", "=B11*B5", "INR / mo", "20 agents * ₹35,000/mo = ₹7,00,000"),
    ("Cost per Resolved Ticket (Pure Human) (₹)", "=ROUND(B12/B10, 2)", "INR / ticket", "= ₹7,00,000 / 17,500 = ₹40.00"),
    ("--- MODEL 2: CHEERIO CO-PILOT + SCALED HUMAN ---", "", "", ""),
    ("Queries Handled by Co-Pilot (65% Deflection)", "=Volume_Model!B10", "Tickets / mo", "11,375 tickets resolved with zero human touch"),
    ("Queries Escalated to Human Support (35%)", "=Volume_Model!B11", "Tickets / mo", "6,125 tickets requiring human intervention"),
    ("Human Agents Needed for Escalations", "=ROUNDUP(B16/B8, 0)", "Agents", "= ROUNDUP(6,125 / 880) = 7 Agents"),
    ("Scaled Human Support Salary Cost (₹)", "=B17*B5", "INR / mo", "7 agents * ₹35,000/mo = ₹2,45,000"),
    ("Monthly AI Infrastructure Cost (₹)", "=Token_Economics!B18", "INR / mo", "₹3,500 (from Token_Economics)"),
    ("Total Blended Support Cost (₹)", "=B18+B19", "INR / mo", "₹2,45,000 human + ₹3,500 AI = ₹2,48,500"),
    ("Blended Cost per Ticket (₹)", "=ROUND(B20/B10, 2)", "INR / ticket", "= ₹2,48,500 / 17,500 = ₹14.20"),
    ("--- NET SAVINGS & ROI ---", "", "", ""),
    ("Net Monthly Operational Savings (₹)", "=B12-B20", "INR / mo", "= Pure Human Cost - Blended Cost"),
    ("Net Annual Operational Savings (₹)", "=B23*12", "INR / yr", "= Monthly Savings * 12 (₹54.18 Lakhs)"),
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
        c_val.number_format = "₹#,##0.00" if row_idx in [13, 21] else "₹#,##0"
    elif "Tickets" in unit or "Agents" in unit:
        c_val.number_format = "#,##0"

# Highlight final savings
ws4["A23"].fill = accent_fill
ws4["B23"].fill = accent_fill
ws4["C23"].fill = accent_fill
ws4["D23"].fill = accent_fill
ws4["A24"].fill = accent_fill
ws4["B24"].fill = accent_fill
ws4["C24"].fill = accent_fill
ws4["D24"].fill = accent_fill

# -------------------------------------------------------------
# TAB 5: Billing & Retention ROI
# -------------------------------------------------------------
ws5 = wb.create_sheet(title="Retention_ROI")
ws5.views.sheetView[0].showGridLines = True

ws5["A1"] = "Packaging, Billing Strategy & Churn Prevention ROI"
ws5["A1"].font = title_font
ws5["A2"] = "Justifying 100% Free Core In-App Feature via Retention Economics"
ws5["A2"].font = meta_font

ws5["A4"] = "Retention & Revenue Parameter"
ws5["B4"] = "Value"
ws5["C4"] = "Unit"
ws5["D4"] = "Strategic Rationale"
for col in ["A4", "B4", "C4", "D4"]:
    ws5[col].fill = header_fill
    ws5[col].font = header_font

retention_rows = [
    ("Cheerio Active Businesses", 5000, "Businesses", "Given active customer base"),
    ("Estimated Average Monthly Subscription (ARPU)", 2999, "INR / biz / mo", "Benchmark standard WhatsApp marketing SaaS subscription tier"),
    ("Total Monthly Recurring Revenue (MRR)", "=B5*B6", "INR / mo", "Estimated Cheerio baseline MRR (₹1.50 Crore / mo)"),
    ("Baseline Monthly Merchant Churn Rate", 0.05, "% / mo", "Estimated 5.0% monthly churn typical in Indian SMB SaaS"),
    ("Lost Businesses per Month (Baseline Churn)", "=ROUND(B5*B8, 0)", "Businesses / mo", "250 merchants churning each month"),
    ("Estimated Churn Reduction via Co-Pilot (ZOCR)", 0.012, "% absolute", "Saving 1.2% churn by eliminating onboarding drop-offs"),
    ("Preserved Businesses per Month", "=ROUND(B5*B10, 0)", "Businesses / mo", "60 businesses retained every month"),
    ("Preserved Recurring Revenue per Month (₹)", "=B11*B6", "INR / mo", "60 retained businesses * ₹2,999 ARPU = ₹1,79,940/mo"),
    ("Preserved Annual Recurring Revenue (ARR) (₹)", "=B12*12", "INR / yr", "= ₹1,79,940 * 12 = ₹21.59 Lakhs/yr"),
    ("Monthly Cheerio Co-Pilot AI Cost (₹)", "=Token_Economics!B18", "INR / mo", "₹3,500 total monthly AI infrastructure cost"),
    ("Monthly Net Financial Value Generated (₹)", "=B12-B14", "INR / mo", "Preserved Revenue - AI Operating Cost"),
    ("ROI on AI Infrastructure Spend", "=ROUND(B12/B14, 1)", "x Return", "₹1,79,940 preserved revenue / ₹3,500 spend = 51.4x ROI"),
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

ws5["A16"].fill = accent_fill
ws5["B16"].fill = accent_fill
ws5["C16"].fill = accent_fill
ws5["D16"].fill = accent_fill

# Adjust all column widths across sheets
for ws in wb.worksheets:
    for col in ws.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = get_column_letter(col[0].column)
        ws.column_dimensions[col_letter].width = max(max_len + 4, 12)

wb.save("/Users/sakshamgupta/Documents/resume/cheerio/assignment/cheerio_cost_model.xlsx")
print("Saved cheerio_cost_model.xlsx successfully!")
