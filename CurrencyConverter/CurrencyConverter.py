import json
import requests  # requests module is necessary

code_from = input("Enter code of a currency to convert from: ").lower()
rates = dict()
rates["eur"] = json.loads(requests.get("http://www.floatrates.com/daily/eur.json").text)  # caches usd and eur as the
rates["usd"] = json.loads(requests.get("http://www.floatrates.com/daily/usd.json").text)  # most popular ones

while True:
    code_to = input("Enter code of a currency to convert to (or press enter to quit): ").lower()
    if not code_to or code_to == '':
        break
    money = int(input("Enter amount of money to convert: "))
    print("Checking the cache...")
    # checks the cache and downloads it if it no there from http://www.floatrates.com/
    if code_to not in rates:
        print("Sorry, but it is not in the cache!")
        rates[code_to] = json.loads(requests.get(f"http://www.floatrates.com/daily/{code_to}.json").text)
    else:
        print("Oh! It is in the cache!")
    print(f"You received {round(money / rates[code_to][code_from]['rate'], 2)} {code_to}.")
