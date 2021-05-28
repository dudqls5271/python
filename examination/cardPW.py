cardPW = None
def cardPW():
    global cardPW
    cardPW = input("카드 비빌번호 앞자리 2자를 입력해주세요 > ")
    while True:
        if int(len(cardPW)) == 2:
            cardPW = str(cardPW) + "**"
            print("** 결제 성공 **")
            # import cardInfo
            # cardInfo.cardInfo()
            break
        if int(len(cardPW)) != 2:
            print("잘못 입력하셨습니다.")
            cardPW = input("카드 비빌번호 앞자리 2자를 입력해주세요 > ")

if __name__ == '__main__' :
    cardPW()