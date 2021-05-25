import json

with open("product.json", "r", encoding="utf-8") as handle:
    jdata = handle.read()
data = json.loads(jdata)
def Digital():
    index = 0
    while True :
        # print(data[index]["name"])
        if data[index]["category"] == "Digital" :
            print(data[index]["name"] + " " + "(" + data[index]["price"] + ")")
        index = index + 1
        if int(len(data)) == index:
            break

def life():
    index = 0
    while True :
        # print(data[index]["name"])
        if data[index]["category"] == "life" :
            print(data[index]["name"] + " " + "(" + data[index]["price"] + ")")
        index = index + 1
        if int(len(data)) == index:
            break

def Fashion():
    index = 0
    while True :
        # print(data[index]["name"])
        if data[index]["category"] == "Fashion" :
            print(data[index]["name"] + " " + "(" + data[index]["price"] + ")")
        index = index + 1
        if int(len(data)) == index:
            break

