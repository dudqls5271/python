cardCVC_re = None
def cardCVC():
    global cardCVC_re
    cardCVC_re = input("카드 뒷자리의 CVC 번호를 입력해주세요 > ")
    while True:
        if int(len(cardCVC_re)) == 3:
            import cardPW
            cardPW.cardPW()
            break
        if int(len(cardCVC_re)) != 3:
            print("잘못 입력하셨습니다.")
            cardCVC_re = input("카드 뒷자리의 CVC 번호를 입력해주세요 > ")

if __name__ == '__main__' :
    cardCVC()