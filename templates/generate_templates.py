#!/usr/bin/env python3
"""Generate branded PDF templates for Shepherd Networks LLC."""

import os
from fpdf import FPDF

# Branding
COMPANY = "Shepherd Networks LLC"
TAGLINE = "San Angelo's Trusted Network Companion"
EMAIL = "info@shepherdnetworks.com"
WEBSITE = "shepherdnetworks.com"
LOCATION = "San Angelo, TX"

# Colors (RGB)
NAVY = (29, 46, 71)       # #1d2e47
DARK = (19, 29, 46)       # #131d2e
GOLD = (184, 131, 74)     # #b8834a
TEXT = (44, 62, 80)        # #2c3e50
LIGHT_TEXT = (108, 122, 137)  # #6c7a89
WHITE = (255, 255, 255)
LIGHT_BG = (244, 246, 249)  # #f4f6f9
LINE_COLOR = (200, 210, 220)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(SCRIPT_DIR, "..", "assets", "images", "shepnet-logo-og.png")


class ShepherdPDF(FPDF):
    """Base PDF class with Shepherd Networks branding."""

    def __init__(self, title_text=""):
        super().__init__()
        self.title_text = title_text
        self.set_auto_page_break(auto=True, margin=25)

    def header(self):
        # Navy header bar
        self.set_fill_color(*NAVY)
        self.rect(0, 0, 210, 32, "F")

        # Logo
        if os.path.exists(LOGO_PATH):
            self.image(LOGO_PATH, 10, 4, 24)

        # Company name
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(*WHITE)
        self.set_xy(38, 7)
        self.cell(0, 8, COMPANY, new_x="LMARGIN", new_y="NEXT")

        # Tagline
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*GOLD)
        self.set_xy(38, 15)
        self.cell(0, 5, TAGLINE)

        # Contact info right-aligned
        self.set_font("Helvetica", "", 7)
        self.set_text_color(*WHITE)
        self.set_xy(130, 7)
        self.cell(70, 4, EMAIL, align="R")
        self.set_xy(130, 11)
        self.cell(70, 4, WEBSITE, align="R")
        self.set_xy(130, 15)
        self.cell(70, 4, LOCATION, align="R")

        # Gold accent line under header
        self.set_draw_color(*GOLD)
        self.set_line_width(0.8)
        self.line(0, 32, 210, 32)

        # Document title
        if self.title_text:
            self.set_xy(10, 37)
            self.set_font("Helvetica", "B", 18)
            self.set_text_color(*NAVY)
            self.cell(0, 10, self.title_text, new_x="LMARGIN", new_y="NEXT")
            self.ln(2)
        else:
            self.set_y(36)

    def footer(self):
        self.set_y(-20)
        # Gold line
        self.set_draw_color(*GOLD)
        self.set_line_width(0.4)
        self.line(10, self.get_y(), 200, self.get_y())

        self.set_font("Helvetica", "", 7)
        self.set_text_color(*LIGHT_TEXT)
        self.set_y(-16)
        self.cell(0, 4, f"{COMPANY}  |  {EMAIL}  |  {WEBSITE}", align="C",
                  new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 4, f"Page {self.page_no()}/{{nb}}", align="C")

    def section_heading(self, text):
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(*NAVY)
        self.cell(0, 8, text, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*GOLD)
        self.set_line_width(0.3)
        self.line(self.l_margin, self.get_y(), 200, self.get_y())
        self.ln(3)

    def label_value_row(self, label, value="", w_label=50, w_value=130):
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(*TEXT)
        self.cell(w_label, 7, label)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(*LIGHT_TEXT)
        self.cell(w_value, 7, value if value else "___________________________",
                  new_x="LMARGIN", new_y="NEXT")

    def table_header(self, cols):
        """cols: list of (label, width)"""
        self.set_fill_color(*NAVY)
        self.set_text_color(*WHITE)
        self.set_font("Helvetica", "B", 9)
        for label, w in cols:
            self.cell(w, 8, label, border=0, fill=True, align="C")
        self.ln()
        self.set_text_color(*TEXT)

    def table_row(self, cols, values, alternate=False):
        """cols: list of (label, width), values: list of strings"""
        if alternate:
            self.set_fill_color(*LIGHT_BG)
        else:
            self.set_fill_color(*WHITE)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(*TEXT)
        for i, (_, w) in enumerate(cols):
            val = values[i] if i < len(values) else ""
            self.cell(w, 7, val, border=0, fill=True, align="C" if i > 0 else "L")
        self.ln()

    def blank_table_rows(self, cols, count=6):
        for i in range(count):
            self.table_row(cols, [""] * len(cols), alternate=(i % 2 == 1))

    def notes_section(self, label="Notes"):
        self.section_heading(label)
        self.set_draw_color(*LINE_COLOR)
        self.set_line_width(0.2)
        for _ in range(5):
            y = self.get_y()
            self.line(self.l_margin, y, 200, y)
            self.ln(7)

    def signature_block(self):
        self.ln(5)
        y = self.get_y()
        self.set_font("Helvetica", "", 9)
        self.set_text_color(*TEXT)

        # Provider side
        self.set_xy(10, y)
        self.cell(85, 6, "Provider Signature: ___________________________")
        # Client side
        self.set_xy(110, y)
        self.cell(85, 6, "Client Signature: ___________________________")
        self.ln(8)

        y = self.get_y()
        self.set_xy(10, y)
        self.cell(85, 6, "Date: _______________")
        self.set_xy(110, y)
        self.cell(85, 6, "Date: _______________")
        self.ln(10)


def generate_invoice():
    pdf = ShepherdPDF("INVOICE")
    pdf.alias_nb_pages()
    pdf.add_page()

    # Invoice metadata
    pdf.section_heading("Invoice Details")
    meta_cols = [
        ("Invoice #:", "INV-________"),
        ("Invoice Date:", "____/____/________"),
        ("Due Date:", "____/____/________"),
        ("Payment Terms:", "Due on Receipt"),
    ]
    for label, val in meta_cols:
        pdf.label_value_row(label, val)
    pdf.ln(4)

    # Bill To
    pdf.section_heading("Bill To")
    for label in ["Client Name:", "Business Name:", "Address:", "Phone:", "Email:"]:
        pdf.label_value_row(label)
    pdf.ln(4)

    # Line items
    pdf.section_heading("Services & Charges")
    cols = [("Description", 75), ("Qty / Hours", 25), ("Rate", 30), ("Amount", 30), ("Notes", 30)]
    pdf.table_header(cols)
    pdf.blank_table_rows(cols, count=8)
    pdf.ln(2)

    # Totals
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*TEXT)
    x_label = 130
    x_val = 170
    for label in ["Subtotal:", "Tax:", "Discount:"]:
        pdf.set_x(x_label)
        pdf.set_font("Helvetica", "", 9)
        pdf.cell(40, 7, label, align="R")
        pdf.cell(30, 7, "$_________", align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.set_x(x_label)
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(*NAVY)
    pdf.cell(40, 9, "TOTAL DUE:", align="R")
    pdf.cell(30, 9, "$_________", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    # Payment info
    pdf.section_heading("Payment Information")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(0, 5,
        "Payment Methods: Card on file, check, or other arrangement.\n"
        "Make checks payable to: Shepherd Networks LLC\n"
        "Questions? Contact info@shepherdnetworks.com")
    pdf.ln(4)

    pdf.notes_section()

    pdf.output(os.path.join(SCRIPT_DIR, "Invoice_Template.pdf"))
    print("  Generated: Invoice_Template.pdf")


def generate_quote():
    pdf = ShepherdPDF("QUOTE / ESTIMATE")
    pdf.alias_nb_pages()
    pdf.add_page()

    # Quote metadata
    pdf.section_heading("Quote Details")
    meta = [
        ("Quote #:", "QTE-________"),
        ("Date:", "____/____/________"),
        ("Valid Until:", "____/____/________"),
        ("Prepared By:", "Chas Rogers, Shepherd Networks LLC"),
    ]
    for label, val in meta:
        pdf.label_value_row(label, val)
    pdf.ln(4)

    # Prepared For
    pdf.section_heading("Prepared For")
    for label in ["Client Name:", "Business Name:", "Address:", "Phone:", "Email:"]:
        pdf.label_value_row(label)
    pdf.ln(4)

    # Project description
    pdf.section_heading("Project Description")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*LIGHT_TEXT)
    pdf.multi_cell(0, 5, "[Describe the project scope, goals, and any relevant context here.]")
    pdf.ln(6)

    # Line items
    pdf.section_heading("Itemized Estimate")
    cols = [("Item / Service", 70), ("Qty", 20), ("Unit Price", 30), ("Total", 30), ("Notes", 40)]
    pdf.table_header(cols)
    pdf.blank_table_rows(cols, count=8)
    pdf.ln(2)

    # Totals
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*TEXT)
    for label in ["Subtotal:", "Tax (if applicable):", "Discount:"]:
        pdf.set_x(130)
        pdf.cell(40, 7, label, align="R")
        pdf.cell(30, 7, "$_________", align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.set_x(130)
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(*NAVY)
    pdf.cell(40, 9, "ESTIMATED TOTAL:", align="R")
    pdf.cell(30, 9, "$_________", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    # Terms
    pdf.section_heading("Terms & Conditions")
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*TEXT)
    terms = [
        "1. This quote is valid for 30 days from the date above unless otherwise noted.",
        "2. Equipment costs are not included unless explicitly listed above.",
        "3. Payment terms: 50% due at project start, 50% due upon completion (for project work).",
        "4. Hourly services are billed at the rates listed above with a 2-hour minimum where applicable.",
        "5. Additional work beyond the scope described above will be quoted separately.",
    ]
    for t in terms:
        pdf.cell(0, 5, t, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    pdf.notes_section()
    pdf.signature_block()

    pdf.output(os.path.join(SCRIPT_DIR, "Quote_Template.pdf"))
    print("  Generated: Quote_Template.pdf")


def generate_bom():
    pdf = ShepherdPDF("BILL OF MATERIALS")
    pdf.alias_nb_pages()
    pdf.add_page()

    # Project info
    pdf.section_heading("Project Information")
    meta = [
        ("Project Name:", ""),
        ("Client Name:", ""),
        ("Prepared By:", "Chas Rogers, Shepherd Networks LLC"),
        ("Date:", "____/____/________"),
        ("Revision:", "1.0"),
    ]
    for label, val in meta:
        pdf.label_value_row(label, val)
    pdf.ln(4)

    # Network Equipment
    pdf.section_heading("Network Equipment")
    cols = [("Item", 55), ("Manufacturer / Model", 45), ("Qty", 15), ("Unit Cost", 25), ("Total", 25), ("Source / Notes", 25)]
    pdf.table_header(cols)
    pdf.blank_table_rows(cols, count=6)
    pdf.ln(2)

    # Cabling & Infrastructure
    pdf.section_heading("Cabling & Infrastructure")
    cols2 = [("Item", 55), ("Specification", 45), ("Qty / Length", 20), ("Unit Cost", 25), ("Total", 25), ("Notes", 20)]
    pdf.table_header(cols2)
    pdf.blank_table_rows(cols2, count=5)
    pdf.ln(2)

    # Accessories & Misc
    pdf.section_heading("Accessories & Miscellaneous")
    cols3 = [("Item", 65), ("Qty", 20), ("Unit Cost", 30), ("Total", 30), ("Notes", 45)]
    pdf.table_header(cols3)
    pdf.blank_table_rows(cols3, count=4)
    pdf.ln(2)

    # Summary
    pdf.section_heading("Cost Summary")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*TEXT)
    for label in ["Network Equipment:", "Cabling & Infrastructure:", "Accessories & Misc:", "Shipping (estimated):"]:
        pdf.set_x(100)
        pdf.cell(60, 7, label, align="R")
        pdf.cell(30, 7, "$_________", align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.set_x(100)
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(*NAVY)
    pdf.cell(60, 9, "TOTAL MATERIALS:", align="R")
    pdf.cell(30, 9, "$_________", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    # Disclaimer
    pdf.section_heading("Notes & Disclaimer")
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*TEXT)
    notes = [
        "- Prices are estimates based on current market rates and may vary at time of purchase.",
        "- Client is responsible for purchasing equipment unless otherwise agreed in writing.",
        "- Shepherd Networks can assist with sourcing and procurement upon request.",
        "- Installation labor is not included in this BOM (see separate quote or service agreement).",
        "- Substitutions may be recommended if listed items become unavailable.",
    ]
    for n in notes:
        pdf.cell(0, 5, n, new_x="LMARGIN", new_y="NEXT")

    pdf.output(os.path.join(SCRIPT_DIR, "Bill_of_Materials_Template.pdf"))
    print("  Generated: Bill_of_Materials_Template.pdf")


def generate_troubleshooting_info():
    pdf = ShepherdPDF("NETWORK ASSESSMENT REPORT")
    pdf.alias_nb_pages()
    pdf.add_page()

    # Client info
    pdf.section_heading("Client Information")
    for label in ["Client Name:", "Business Name:", "Address:", "Date of Visit:", "Technician:"]:
        val = "Chas Rogers" if label == "Technician:" else ""
        pdf.label_value_row(label, val)
    pdf.ln(4)

    # Issue summary
    pdf.section_heading("Reported Issue(s)")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*LIGHT_TEXT)
    pdf.multi_cell(0, 5, "[Describe the issue(s) reported by the client before the site visit.]")
    pdf.ln(8)

    # Network overview
    pdf.section_heading("Current Network Overview")
    overview_cols = [("Component", 50), ("Make / Model", 45), ("Location", 35), ("Status", 30), ("Notes", 30)]
    pdf.table_header(overview_cols)
    pdf.blank_table_rows(overview_cols, count=6)
    pdf.ln(4)

    # Test results
    pdf.section_heading("Diagnostic Results")

    # Speed tests
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(*NAVY)
    pdf.cell(0, 6, "Speed Tests", new_x="LMARGIN", new_y="NEXT")
    speed_cols = [("Location", 45), ("Download (Mbps)", 30), ("Upload (Mbps)", 30), ("Latency (ms)", 30), ("Connection", 30), ("Notes", 25)]
    pdf.table_header(speed_cols)
    pdf.blank_table_rows(speed_cols, count=4)
    pdf.ln(3)

    # WiFi analysis
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(*NAVY)
    pdf.cell(0, 6, "WiFi Analysis", new_x="LMARGIN", new_y="NEXT")
    wifi_cols = [("SSID / Band", 40), ("Channel", 20), ("Signal (dBm)", 25), ("Noise", 20), ("Clients", 20), ("Interference", 25), ("Notes", 40)]
    pdf.table_header(wifi_cols)
    pdf.blank_table_rows(wifi_cols, count=4)
    pdf.ln(4)

    # Findings
    pdf.section_heading("Findings & Root Cause")
    pdf.set_draw_color(*LINE_COLOR)
    pdf.set_line_width(0.2)
    for _ in range(6):
        y = pdf.get_y()
        pdf.line(pdf.l_margin, y, 200, y)
        pdf.ln(7)

    # Recommendations - new page
    pdf.add_page()
    pdf.section_heading("Actions Taken")
    pdf.set_draw_color(*LINE_COLOR)
    for _ in range(5):
        y = pdf.get_y()
        pdf.line(pdf.l_margin, y, 200, y)
        pdf.ln(7)
    pdf.ln(2)

    pdf.section_heading("Recommendations")
    rec_cols = [("Recommendation", 70), ("Priority", 25), ("Est. Cost", 30), ("Notes", 65)]
    pdf.table_header(rec_cols)
    pdf.blank_table_rows(rec_cols, count=5)
    pdf.ln(4)

    # Follow-up
    pdf.section_heading("Follow-Up")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*TEXT)
    followup = [
        ("Follow-up needed?", "Yes  /  No"),
        ("Recommended follow-up date:", ""),
        ("Additional services quoted?", "Yes  /  No"),
    ]
    for label, val in followup:
        pdf.label_value_row(label, val)
    pdf.ln(4)

    # Services callout
    pdf.set_fill_color(*LIGHT_BG)
    pdf.set_draw_color(*GOLD)
    pdf.set_line_width(0.3)
    y = pdf.get_y()
    pdf.rect(10, y, 190, 32, "FD")
    pdf.set_xy(15, y + 3)
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(*NAVY)
    pdf.cell(0, 6, "Ongoing Protection for Your Network", new_x="LMARGIN", new_y="NEXT")
    pdf.set_x(15)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(180, 4,
        "Shepherd Networks offers managed services to keep your network running smoothly:\n"
        "  - Network Monitoring ($75/mo) - 24/7 monitoring with proactive alerts\n"
        "  - DNS Security ($25/mo) - Block malware, phishing, and malicious sites network-wide\n"
        "  - Performance & Security Bundle ($150/mo) - Both services + 1 hr/mo remote support")
    pdf.ln(6)

    pdf.signature_block()

    pdf.output(os.path.join(SCRIPT_DIR, "Network_Assessment_Report_Template.pdf"))
    print("  Generated: Network_Assessment_Report_Template.pdf")


if __name__ == "__main__":
    print("Generating Shepherd Networks PDF templates...")
    generate_invoice()
    generate_quote()
    generate_bom()
    generate_troubleshooting_info()
    print("Done! All templates saved to the templates/ directory.")
