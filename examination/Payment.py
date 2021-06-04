import json


from numbersProduct import *
from product_selection import *
with open("product.json", "r", encoding="utf-8") as handle:
    jdata = handle.read()
data = json.loads(jdata)

price_sum = None
sum_data = None
def pay():
    global price_sum
    global sum_data
    index = 0
    while True:
        # print(data[index]["name"])
        print(product_ch)
        if data[index]["seq"] == product_ch:
            price2 = data[index]["price"]
            price_sum = int(price2) * int(productNum)

            strN = str(price_sum)  # 문자화
            lenN = len(strN)  # 문자길이
            len_c = (lenN // 3) * 3  # 3의 배수단위로 개수구함
            str_list = []
            i = len_c
            str_list.append(strN[0:-(len_c)])  # 처음은 따로넣음 12000의 경우 '12'부분
            while i > 3:
                str_list.append(strN[-(i):-(i - 3)])  # 3의배수 단위로 넣어줌
                i -= 3
            str_list.append(strN[-3::])  # 끝은 따로 넣음
            a = ','
            sum_data = a.join(str_list).strip(',')

            print("==================================")
            print("제춤 수량 : " + str(productNum))
            print("제품 이름 : " + data[index]["name"])
            print("제품 가격 : " + sum_data + "원")
            print("==================================")
            import cardpay
            cardpay.cardpay()

        index = index + 1
        if int(len(data)) == index:
            break
if __name__ == '__main__':
    pay()
