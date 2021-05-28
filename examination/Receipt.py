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

def receipt():
    print("===================================")
    print("              영수증 상세")
    print("===================================")
    print("수량                            " + productNum + "개")
    index = 0
    while True:
        if data[index]["seq"] == product_ch:
            print(data[index]["name"])
            print(str(sum_data) + "원")
        index = index + 1
        if int(len(data)) == index:
            break

    print("===================================")
    now = datetime.datetime.now()
    nowTime = now.strftime('%H:%M:%S')
    print("승인 일시                   " + nowTime)
    print("거래 유형                   " + "승인")
    print("추가 마일리지                " + str(round(point)))
    index = 0
    while True:
        if user[index]["user_name"] == user_name:
            print("보유 마일리지                " + str(user[index]["user_point"]))
        index = index + 1
        if int(len(user)) == index:
            break
    print("거래자 명                   " + user_name)
    print("===================================")
if __name__ == '__main__':
    receipt()