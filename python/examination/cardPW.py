cardPW_re = None
def cardPW():
    global cardPW_re
    cardPW_re = input("카드 비빌번호 앞자리 2자를 입력해주세요 > ")
    while True:
        if int(len(cardPW_re)) == 2:
            cardPW_re = str(cardPW_re) + "**"
            print("** 결제 성공 **")
            # import cardInfo
            # cardInfo.cardInfo()
            import point
            point.porint()
            break
        if int(len(cardPW_re)) != 2:
            print("잘못 입력하셨습니다.")
            cardPW_re = input("카드 비빌번호 앞자리 2자를 입력해주세요 > ")

if __name__ == '__main__' :
    cardPW()