import datetime

def Simple():
    now = datetime.datetime.now()
    start_h = now.strftime('%H:%M:%S')

    print(start_h)

    print("사용자 이름과 지불 하실 금액을 적어주세요 Ex) 이영빈 2000")
    user_info = list((input().split()))
    print(user_info)

    user_h = round(int(user_info[1]) / 1000)
    print(user_h)
    end_h = now + datetime.timedelta(hours=user_h)
    print(end_h)
    print(str(user_h) + "시간 충전 했습니다.")

    user_h_out = list((now), (end_h))
    print("시작 시간 : " + user_h_out[0] + "끝나는 시간 : " + user_h_out[1])
if __name__ == '__main__':
    Simple()