cardCVC = None
def cardCVC():
    global cardCVC
    cardCVC = input("카드 뒷자리의 CVC 번호를 입력해주세요 > ")
    while True:
        if int(len(cardCVC)) == 3:
            import cardPW
            cardPW.cardPW()
            break
        if int(len(cardCVC)) != 3:
            print("잘못 입력하셨습니다.")
            cardCVC = input("카드 뒷자리의 CVC 번호를 입력해주세요 > ")

if __name__ == '__main__' :
    cardCVC()