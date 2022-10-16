import csv

# sorted by user defined function
def get_value(title):
    return titles[title]

with open("CSV (raw data).csv", "r") as file:
    # Read as a list
    # reader = csv.reader(file)
    # next(reader)
    # for rows in reader:
    #     print(rows[1], rows[2])

    # Read as a dictionary
    # reader = csv.DictReader(file)
    # for row in reader:
    #     print(row['Title'])

    # Remove Duplicate
    # Strip function, forcing case into uppercase
    # reader = csv.DictReader(file)
    # oricount = 0
    # titles = []
    # for row in reader:
    #     oricount += 1
    #     if not row['Title'] in titles:
    #         titles.append(row["Title"])
    
    # print(f"Original Count: {oricount}")
    # print(f"Removed Duplicate Count: {len(titles)}")

    # Using a set to remove duplicate
    # titles = set()
    # reader = csv.DictReader(file)
    # for row in reader:
    #     title = row["Title"].strip().upper()
    #     titles.add(title)
    
    # print(len(titles))
    # for title in sorted(titles):
    #     print(title)

    # counting the frequency of the data
    # titles = dict()

    # reader = csv.DictReader(file)
    # for row in reader:
    #     title = row['Title'].strip().upper()
    #     if title in titles:
    #         titles[title] += 1
    #     else:
    #         titles[title] = 1

    # # sorted by user defined function
    # for title in sorted(titles, key = get_value, reverse =True):
    #     print(title, titles[title])
    
    # # sorted by user defined function using anonymous function
    # for title in sorted(titles, key = lambda title: titles[title], reverse =True):
    #     print(title, titles[title])

    # Sorting data
    counter = 0
    reader = csv.DictReader(file)
    for row in reader:
        title = row["Title"].strip().upper()
        if "THOR" in title:
            counter += 1
    print(counter)