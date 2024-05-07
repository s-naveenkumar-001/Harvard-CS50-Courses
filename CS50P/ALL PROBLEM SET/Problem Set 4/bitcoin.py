# import requests library to get the web data.import sys to use the command line arguments.exit
# use try and except to handle the errors and in try convert input into float value.
# if any error occurs usin except catch the error and give instruction and using sys.exit() exit the program.
# if command line not equal to two give instruction and exit te program.
# Usin request get web data and chane into json format. get specific data from json.
# multiply the bitcoin rate and user enter value with float and add commma to the amount.
import requests
import sys

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print("Command-line argument is not a number ")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = r.json()
    bitcoin_to_USD = response['bpi']['USD']['rate']
    bitcoin_to_USD = bitcoin_to_USD.replace(",","")
    amount = float(bitcoin_to_USD) * float(sys.argv[1])
    print(f"${amount:,.4f}")
# if any error occurs usin except catch the error.
except requests.RequestException:
    print("RequestException")
    sys.exit(1)