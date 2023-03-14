import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few comand-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many comand-line arguments")

elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    test = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("No such file")

after = []

input_file = csv.DictReader(open(sys.argv[1]))
for row in input_file:
    first_name, last_name = row["name"].split(",")
    house = row["house"]
    slownik = {"first": first_name.strip(), "last": last_name.strip(), "house": house}
    after.append(slownik)

with open(sys.argv[2], 'w', newline='') as file:
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in after:
        writer.writerow(row)