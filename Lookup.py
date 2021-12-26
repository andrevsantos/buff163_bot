import requests
import time

cookies = {'session': 'INSERT SESSION COOKIE HERE'}


f = open("demo.txt", "w", encoding="utf-8")

for x in range(835):
    url = "https://buff.163.com/api/market/goods?game=csgo&page_num=" + str(x+1)
    r = requests.get(url,cookies=cookies)

    items = r.json()
    itemsData = items['data']
    for item in itemsData['items']:
        f.write(str(item['id']) + ";" + item['market_hash_name'] + "\n")

    time.sleep(5)

f.close()

