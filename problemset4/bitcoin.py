import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Missing command line argument")
try:
    sys.argv[1] = float(sys.argv[1])
except:
    sys.exit("this value is not convertable to float")    
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    print("Request not found!")
    
o = response.json()
bitcoin = (float(o['bpi']['USD']['rate_float']))
# print(p *  2)
amount = (bitcoin * sys.argv[1])
print(f"${amount:,.4f}")
