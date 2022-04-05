#!/usr/bin/env python3

import csv,re,sys
from collections import defaultdict
from sys import argv

if len(argv)!=3:
    print("Usage: flex2cols.py INPUT_CSV OUTPUT_CSV\nINPUT_CSV should contain rows in the form of ID,KEY,VALUE.\nAlso use KEY,VALUE for GUID, CODE and other fixed fields.")
    sys.exit()    

encoding = "ISO-8859-1"
input_filename = argv[1]
output_filename = argv[2]
items = defaultdict(dict)
header = ["ID"]

for row in csv.DictReader(open(input_filename, encoding=encoding)):
    header.append(row["KEY"]) if row["KEY"] not in header else None
    row["VALUE"] = row["VALUE"].replace("\n"," ").replace("<ZR>","") 
    item = items[row["ID"]]
    item[row["KEY"]] = row["VALUE"]

# output to csv
writer = csv.DictWriter(open(output_filename,"w"), fieldnames=header, delimiter=",")
writer.writeheader()
writer.writerows(items.values())
