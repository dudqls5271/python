import datetime

def smsple():
    now = datetime.datetime.now()
    nowTime = now.strftime('%H:%M:%S')

    print (nowTime)

    print("일반 학생의 이름을 입력해주세요(Ex) 이영빈 김민우 신환희)")
    stu1 = list((input().split()))

    # print("장애인 학생의 이름을 입력해주세요(Ex) 이영빈 김민우 신환희)")
    stu2 = list((input().split()))
    print(stu1)
    # print(stu2)

    attendance = 0
    notattendance = 0;
    for i in stu1 :
        print(i + "는 강의실에 있나요? Ex) o(알파벳): ")
        stuCh = list((input().split(), nowTime, i))
        print(stuCh)
if __name__ == '__main__':
    smsple()