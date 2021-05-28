import json

with open("product.json", "r", encoding="utf-8") as handle:
    jdata = handle.read()
data = json.loads(jdata)

from product_selection import product_ch
product_name = product_ch
index = 0
