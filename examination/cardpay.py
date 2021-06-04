cardpay_re = None
def cardpay():
    global cardpay_re
    cardpay_re = input("카드 번호을 입력해주세요 > \n Ex) 1111-1111-1111-1111 \n")
    while True:
        # characters = "-"
        # cardpay_re = cardpay_re.replace(characters, "")

        if int(len(cardpay_re)) == 19:
            import cardCVC
            cardCVC.cardCVC()
            break
        elif cardpay_re.isdigit() != True:
            print("잘못 입력하셨습니다.")
            cardpay_re = input("카드 번호을 입력해주세요 > \n Ex) 1111-1111-1111-1111 \n")
if __name__ == '__main__':
    cardpay()