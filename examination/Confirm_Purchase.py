product_ok = None


def confirm():
    global product_ok
    product_ok = input("구메 하시겠습니까? (Y/N)")
    while True:
        if product_ok == "Y" or product_ok == "y":
            print("결제 시작합니다.")
            import Payment
            Payment.pay()
            break
        elif product_ok == "N" or product_ok == "n":
            print("취소 합니다.")
            import menu_view
            menu_view.menm()
            break
        else:
            print("잘못 입력하셨습니다.")
            product_ok = input("구메 하시겠습니까? (Y/N)")


if __name__ == '__main__':
    confirm()
