from product import *
class product_view:
    def __init__(self):
        print("==========================")
        Digital()
        life()
        Fashion()
        print("==========================")

        index = 0
        while True:
            product_ch = input("\n상품을 선택 해주세요 (번호로 선택 가능 위에서부터 1~ 입니다.)>")
            if data[index]["name"] == product_ch or data[index]["seq"] == product_ch:
                print(data[index]["name"] + " " + "(" + data[index]["price"] + ")")
                product_ok = input("\n해당 상품을 구메 하시겠습니까? (Y/N)>")
                # if product_ok == "Y" :
                #     print("결제를 진행 합니다.")
            index += 1

if __name__ == '__main__':
    product_view()
