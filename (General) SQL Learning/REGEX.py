import csv
import re

counter = 0

with open("CSV (raw data).csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["Title"].strip().upper()
        # if re.search("THOR", title):
        if re.search("^(THOR|MORBIUS)$", title):
            print(title)
            counter += 1
        
    print(counter)