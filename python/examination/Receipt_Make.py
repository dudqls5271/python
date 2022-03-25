import datetime
import json

from user_info import user_name
from product_selection import product_ch
from  numbersProduct import productNum
from point import point
from Payment import sum_data

with open("product.json", "r", encoding="utf-8") as handle:
    jdata = handle.read()
data = json.loads(jdata)
with open("user.json", "r", encoding="utf-8") as handle:
    jdata2 = handle.read()
user = json.loads(jdata2)
now = datetime.datetime.now()
nowTime = now.strftime('%Y-%m-%d_%H:%M:%S')
days = now.strftime('%Y-%m-%d')
re = nowTime.replace(":", "")
index = 0
while True:
    if data[index]["seq"] == product_ch:
        print(data[index]["name"])
        print(str(sum_data) + "원")
        total = str(sum_data)
        name = data[index]["name"]
    index = index + 1
    if int(len(data)) == index:
        break
index = 0
while True:
    if user[str(index)]["user_name"] == user_name:
        user_point = str(user[str(index)]["user_point"])
    index = index + 1
    if int(len(user)) == index:
        break

import os

def receipt_make():

    path = "./Reciept/"+ str(user_name)
    if not os.path.isdir(path):
        os.mkdir(path)

    f = open("Reciept/"+str(user_name) + "/" + str(re) + ".txt", 'w', encoding="utf-8")
    f.write("=================================== \n"
            "            영수증 상세\n"
            "===================================\n"
            "수량                            " + productNum + "개\n"
            + name + "\n"
            + total + "\n"
            "===================================\n"
            "승인 일시        " + nowTime + "\n"
            "거래 유형                   " + "승인\n"
            "추가 마일리지                " + str(round(point)) + "\n"
            "보유 마일리지                " + user_point + "\n"
            "거래자 명                   " + user_name + "\n"
            "===================================")
    f.close()

if __name__ == '__main__' :
    receipt_make()