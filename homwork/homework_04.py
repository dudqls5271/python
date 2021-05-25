def smsple():

    name = "CGV"
    ## 영화 종류
    movies = {'극장판 귀멸의 칼날-무한열차편' : ['A1','12:00'],
              '승리호' : ['A2','14:00'],
              '어벤저스' : ['A3','08:00'],
              '배놈' : ['A4','10:00']}

    ## 지역을 표시
    Areas = {'시흥' : ['장현'],
            '서울' : ['사당'],
            '부천' : ['역곡']
            }
    
    ## 세부 지역중 가장 많은 지역의 수
    max_Areas = 2

    ## 상영관과 좌석을 표시
    Theater = {'A1' : [30, 15, 50, 20],
            'A2' : [30, 38, 40, 20],
            'A3' : [30, 40, 30, 18],
            'A4' : [0, 20, 20, 10]
            }

    # 가격을표시
    Seat_Price = {'S' : 20000,
                   'A' : 15000,
                   'B' : 10000,
                   '커플석' : 25000}

    movie_list_type = list(movies.keys())
    Areas_list_type = list(Areas.keys())
    movie_list_type_num = int(len(movie_list_type))
    Areas_list_tpye_nim = int(len(Areas_list_type))

    movie_list_num = [i for i in range(movie_list_type_num)]
    Areas_list_num = [i for i in range(Areas_list_tpye_nim)]

    Receipt = []

    while True :
        print(list(movies.keys()))
        print("영화를 선택해주세요")
        movie = input()
        for i in movie_list_num :
            if movie_list_type[i] in movie :
                Receipt.append(movie)
                print(Areas_list_type)
                print("지역을 선택해주세요")
                Area = input()
                for i in Areas_list_num:
                    if Areas_list_type[i] in Area:
                        list_s = Areas[Area][0:max_Areas]
                        print(list_s)
                        print("다음 지역을 선택해주세요")
                        Area = input()
                        if list_s[0] in Area:
                            print("상영관과 시간을 확인")
                            Receipt.append(movies[movie][1])
                            print(movies[movie])
                            Receipt.append(movies[movie][0])

                            if movies[movie][0] == "A1":
                                print("남은 좌서 (S A B 커플)")
                                print(Theater[movies[movie][0]])
                            if movies[movie][0] == "A2":
                                print("남은 좌서 (S A B 커플)")
                                print(Theater[movies[movie][0]])
                            if movies[movie][0] == "A3":
                                print("남은 좌서 (S A B 커플)")
                                print(Theater[movies[movie][0]])
                            if movies[movie][0] == "A4":
                                print("남은 좌서 (S A B 커플)")
                                print(Theater[movies[movie][0]])

                            print("인원을 작성해주세요")
                            Personnel = input()
                            print("장애인 명수를 작성해주세요")
                            Personnel_2 = input()
                            total_Personnel = int(Personnel) + int(Personnel_2)
                            Receipt.append(total_Personnel)
                            print(total_Personnel)
                            print("좌석을 선택해주세요 S, A, B, 커플석")
                            Receipt.append("CGV")
                            Seat = input()
                            Receipt.append(Seat)
                            if Seat == "S":
                                print(str(Seat_Price[Seat]) + "원 입니다.")
                                price = int(Seat_Price[Seat]) * int(total_Personnel)
                                print("총 금액" + str(price) + "원 입니다.")
                            elif Seat == "A":
                                print(str(Seat_Price[Seat]) + "원 입니다.")
                                price = int(Seat_Price[Seat]) * int(total_Personnel)
                                print("총 금액" + str(price) + "원 입니다.")
                            elif Seat == "B":
                                print(str(Seat_Price[Seat]) + "원 입니다.")
                                price = int(Seat_Price[Seat]) * int(total_Personnel)
                                print("총 금액" + str(price) + "원 입니다.")
                            if Seat == "커플석" and str(total_Personnel) == "2":
                                print(str(Seat_Price[Seat]) + "원 입니다.")
                                price = int(Seat_Price[Seat]) * int(total_Personnel)
                                print("총 금액" + str(price) + "원 입니다.")

                            print("신용카드 or 현금을 골라주세요")
                            Payment_input = input()
                            if Payment_input == "현금":
                                print("현금 얼마을 지불 하실건가요?")
                                Payment = input()
                                print("현금" + str(Payment) + "원 받았습니다")
                                if int(Personnel_2) > 0:
                                    print("장애인 할인이 적용 됩니다." + str(int(price) * 10 / 100) + "원이 적용 됩니다.")
                                    Payment = int(price) - (int(price) * 10 / 100)
                                    print("할인 적용 금액" + str(Payment))
                                    Change_pay = int(price) - int(Payment)
                                print("거스름돈" + str(Change_pay) + "원 입니다.")
                                print("포인트 정립 하실건가요? (네/아니요)")
                                point = input()
                                if point == "네":
                                    pay_point = (price) * 10 / 100000
                                    print(str(pay_point) + "포인트 정립 해드렸습니다.")
                                print("영수증")
                                print(Receipt)
                            else:
                                print("잘못 입력했습니다. 다시 입력해주세요.")
                        else:
                            print("지역을 잘못 선택했습니다.")
            
         if movie_list_type[i] != movie :
             print("선택하신 영화는 없습니다.")
if __name__ == '__main__':
    smsple()