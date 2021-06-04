from product_selection import *
productNum = None
def numbersProduct():
    print(product_ch)
    global productNum
    productNum = input("상품의 수량을 선택해주세요. > ")
    while True:
        if productNum.isalpha():
            print("잘못입력했습니다.")
            productNum = input("상품의 수량을 선택해주세요. > ")
        else:
            import Confirm_Purchase
            Confirm_Purchase.confirm()
            break

if __name__ == '__main__':
    numbersProduct()