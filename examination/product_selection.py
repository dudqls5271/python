from product import *
product_ch = None
def product_select():
    loop = int(len(data))
    global product_ch
    product_ch = input("\n상품을 선택 해주세요 (번호로 선택 가능 위에서부터 1~ 입니다.)>")
    index = 0
    while True:
        if loop - 1 < index:
            product_ch = input("\n상품을 선택 해주세요 (번호로 선택 가능 위에서부터 1~ 입니다.)>")
            index = 0
            break

        if data[index]["name"] == product_ch or data[index]["seq"] == product_ch:
            print(data[index]["name"] + " " + "(" + data[index]["price"] + ")")
            import Confirm_Purchase
            Confirm_Purchase.confirm()
            break
        index += 1


if __name__ == '__main__':
    product_select()
