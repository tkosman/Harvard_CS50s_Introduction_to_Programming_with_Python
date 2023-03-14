import requests
import sys
import json

try:
    amount = float(sys.argv[1])
except IndexError:
    print("Missing command-line argument")
except ValueError:
    print("Command-line argument is not a number")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
value = response.json()["bpi"]["USD"]["rate"]
value = value.replace(",","")
value = float(value) * amount

print(f"${value:,.4f}")