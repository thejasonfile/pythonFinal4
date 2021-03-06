#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Table, Spacer
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()

def generate_report(title, table_data, file):
    report = SimpleDocTemplate(file)
    report_title = Paragraph(title, styles["h1"])
    report_table = Table(data=table_data, hAlign="LEFT")
    report.build([report_title, report_table])
