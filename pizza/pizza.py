import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few comand-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many comand-line arguments")

elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    test = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("No such file")

test.close()

table = []
headers = []
flaga = True
with open(sys.argv[1]) as csvfile:
    plik = csv.reader(csvfile)
    for row in plik:
        if flaga:
            headers = row
            flaga = False
        else:
            table.append(row)

print(tabulate(table, headers, tablefmt="grid"))