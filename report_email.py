#!/usr/bin/env python3

import reports, os, datetime

date = datetime.datetime.now()
date = date.strftime("%m-%d-%Y")
title = "Processed Update on {}".format(date)

table_data = []
files_path = ("supplier-data/descriptions/")
files = os.listdir(files_path)

for file in files:
    file_data = []
    with open(files_path + file, 'r') as file:
        line1 = file.readline().rstrip('\n')
        line2 = file.readline().rstrip('\n')
        table_data.append([""])
        table_data.append(["name:", line1])
        table_data.append(["weight:", line2])

reports.generate_report(title, table_data, "processed.pdf")

if __name__ == "__main__":
    reports.generate_report
