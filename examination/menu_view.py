def menm():
    print("다음 항목 중에 선택하실 수 있습니다.")
    print("상품 구메하기 (1), 내 포인트 조회(2), 내 영주증 리스트 조회(3), 내 영수증 조회(4) ")
    ch = input()

    if ch == "1":
        import product_view
        product_view.te()
    elif ch == "2":
        print("내 포인트 조회")
    elif ch == "3":
        print("내 영주증 리스트 조회")
    elif ch == "4":
        print("내 영수증 조회")
    else:
        print("요류")

if __name__ == '__main__':
    menm()