from Payment import *
from user_info import *

with open("user.json", "r", encoding="utf-8") as handle:
    jdata = handle.read()
data = json.loads(jdata)

def porint():
    print("회원 포인트 적립(3%) 대상 입니다.")
    price_re = price
    characters = ",원"

    for x in range(len(characters)):
        price_re = price_re.replace(characters[x], "")

    point = int(price_re) * 0.03
    print(str(round(point)) + "원 정립 되었습니다.")

    index = 0
    while True :
        if data[index]["user_name"] == user_name :
            print(data[index]["user_point"])
            print(round(point))
            porint_re = int(data[index]["user_point"]) + int(round(point))

            print(data[index]["user_point"])
        index = index + 1
        if int(len(data)) == index:
            break


if __name__ == '__main__':
    porint()