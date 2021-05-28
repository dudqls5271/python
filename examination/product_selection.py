from product import *
index = 0
product_ch = input("\n상품을 선택 해주세요 (번호로 선택 가능 위에서부터 1~ 입니다.)>")
loop = int(len(data))
while True:
    print(loop)
    print(index)
    if loop < index:
        product_ch = input("\n상품을 선택 해주세요 (번호로 선택 가능 위에서부터 1~ 입니다.)>")
        index = 0

    if data[index]["name"] == product_ch or data[index]["seq"] == product_ch:
        print(data[index]["name"] + " " + "(" + data[index]["price"] + ")")
        break
    index += 1
