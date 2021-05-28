import json

from product_selection import *

with open("product.json", "r", encoding="utf-8") as handle:
    jdata = handle.read()
data = json.loads(jdata)

price = "18,9000원"
def pay():
    global price
    index = 0
    while True:
        # print(data[index]["name"])
        if data[index]["seq"] == "1":
            price = data[index]["price"]
            print("==================================")
            print("제품 이름 : " + data[index]["name"])
            print("제품 가격 : " + data[index]["price"])
            print("==================================")

        index = index + 1
        if int(len(data)) == index:
            break


if __name__ == '__main__':
    pay()
