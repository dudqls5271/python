from product import *

product_ch = None

def product_select():
    global product_ch

    product_ch = input("\n상품을 선택 해주세요 (번호로 선택 가능 위에서부터 1~ 입니다.)>")
    loop = int(len(data))
    index = 0
    while True:
        if loop -1 < index or product_ch == 0:
            print("\n잘못 선택했습니다. 다시 선택 해주세요")
            product_ch = input("상품을 선택 해주세요 (번호로 선택 가능 위에서부터 1~ 입니다.)> ")
            index = 0
        if data[index]["name"] == product_ch or data[index]["seq"] == product_ch:
            print(data[index]["name"] + " " + "(" + data[index]["price"] + ")")
            import numbersProduct
            numbersProduct.numbersProduct()
            break
        index += 1

if __name__ == '__main__':
    product_select()
