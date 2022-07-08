import json
import sys
import requests

if len(sys.argv) == 2:
   try:
      n = float(sys.argv[1])
      # sys.exit()
   except ValueError:
      print("Command-line argument is not a number")
else:
   sys.exit()


try:
   response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
   sys.exit()

coin_desk = response.json()


price_USD = coin_desk["bpi"]["USD"]

rate = price_USD["rate_float"]

amount = n * float(rate)

print(f"${amount:,.4f}")