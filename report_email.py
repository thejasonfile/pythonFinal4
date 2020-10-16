#!/usr/bin/env python3

import reports, os, datetime

date = datetime.datetime.now()
date = date.strftime("%m-%d-%Y")
title = "Processed Update on {}".format(date)
data = [[""], ["name:", "Apple"], ["weight:", "500lbs"], [""], ["name:", "Avocado"], ["weight:", "200lbs"]]

reports.generate_report(title, data, "processed.pdf")

if __name__ == "__main__":
    reports.generate_report
