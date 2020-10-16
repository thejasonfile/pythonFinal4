#!/usr/bin/env python3

import reports, os, datetime

date = datetime.datetime.now()
date = date.strftime("%m-%d-%Y")
title = "Processed Update on {}".format(date)

reports.generate_report(title)

if __name__ == "__main__":
    reports.generate_report
