#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Table, Spacer
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()





def generate_report(title):
    report = SimpleDocTemplate("processed.pdf")
    report_title = Paragraph(title, styles["h1"])
    report.build([report_title])
