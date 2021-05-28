from cardpay import *
from cardPW import *
from cardCVC import *

def cardInfo():
    print("결제 카드 정보")
    print("=================================")
    print("카드 번호 : " + str(cardpay))
    print("CVC 번호 : " + str(cardCVC))
    print("카드 비빌번호 : " + str(cardPW))

if __name__ == "__main__" :
    cardInfo()