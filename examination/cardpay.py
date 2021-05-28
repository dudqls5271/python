cardpay = None
def cardpay():
    global cardpay
    cardpay = input("카드 번호을 입력해주세요 > \n Ex) 1111-1111-1111-1111 \n")
    while True:
        # characters = "-"
        # cardnum = cardnum.replace(characters, "")

        if int(len(cardpay)) == 19:
            import cardCVC
            cardCVC.cardCVC()
            break
        elif int(len(cardpay)) != 16:
            print("잘못 입력하셨습니다.")
            cardpay = input("카드 번호을 입력해주세요 > \n Ex) 1111-1111-1111-1111 \n")
        elif cardpay.isdigit() != True:
            print("잘못 입력하셨습니다.")
            cardpay = input("카드 번호을 입력해주세요 > \n Ex) 1111-1111-1111-1111 \n")


if __name__ == '__main__' :
    cardpay()