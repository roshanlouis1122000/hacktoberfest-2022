import requests
import json

bob=requests.get("https://api.coingecko.com/api/v3/simple/price?ids=eth&vs_currencies=usd", headers = {"accept": "application/json"})
print("The current price of TITANO is \t" + str(bob.json()))