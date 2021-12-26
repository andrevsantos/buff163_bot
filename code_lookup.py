import csv
import requests

url = "https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id="
conversion = 0.154327

f = open("key_values.csv", "r", encoding="utf-8")

# Finds the ID of a given item name
def find_id(weapon_name):
   with open("key_values.csv",encoding="utf-8") as f:
     reader = csv.reader(f, delimiter=';')
     for row in reader:
        if weapon_name.lower() in row[1].lower():
            return row[0]

# Retrieves item price based on the id
def get_price(weapon_name):
   weaponID = find_id(weapon_name)
   r = requests.get(url + str(weaponID))
   items = r.json()
   data = items["data"]['items'][0]
   price = float(data['price'])
   print(price * conversion)


# TODO: Add this as CLI
get_price("XM1014 | Entombed (Minimal Wear)")


