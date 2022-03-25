def menm():
    print("\n다음 항목 중에 선택하실 수 있습니다.")
    print("상품 구메하기 (1), 내 포인트 조회(2), 내 영주증 리스트 조회(3)")
    ch = input()

    while True:
        if ch == "1":
            import product_view
            product_view.te()
            break
        elif ch == "2":
            import mypoint
            mypoint.mypoints()
            break
        elif ch == "3":
            print("-------------------------------------------------")
            import Recript_list
            Recript_list.recipt_list()
            break
        else:
            print("잘못 선택 했습니다.")
            print("상품 구메하기 (1), 내 포인트 조회(2), 내 영주증 리스트 조회(3)")
            ch = input()

if __name__ == '__main__':
    menm()