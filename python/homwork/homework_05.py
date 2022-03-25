def smsple():
    product = {"삼각김밥": 1000,
               "도시락": 4500,
               "콜라": 1200}
    Event = {"콜라" : "1+1 행사상품 입니다."}

    discount = {"할인 상품이 없습니다." : ""}
    print(product)
    while True :
        print("어떤 상품을 선택해주세요")
        product_input = input()
        for key in product.values():
            print(product.get(product_input))
            pay = product.get(product_input)
            break
        for key2 in Event.keys() :
            if product_input == key2 :
                print(Event.get(key2))
            break
        break

    print("신용카드 or 현금을 골라주세요")
    Payment_input = input()
    if Payment_input == "현금" :
        print("현금 얼마을 지불 하실건가요?")
        Payment = input()

        print("현금" + str(Payment) + "원 받았습니다")
        Change_pay = int(Payment) - int(pay)
        print("거스름돈" + str(Change_pay) + "원 입니다.")

    if Payment_input == "신용카드" :
        print("결제 되었습니다.")

    print("포인트 정립 하실건가요? (네/아니요)")
    point = input()
    if point == "네" :
        pay_point = (pay) / 100
        print(str(pay_point) + "포인트 정립 해드렸습니다.")

if __name__ == '__main__':
    smsple()