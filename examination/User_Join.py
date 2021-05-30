import json
with open("user.json", "r", encoding="utf-8") as handle:
    jdata = handle.read()
data = json.loads(jdata)


def user_join():
    user_name = input("닉네임을 입력해주세요 (중복 불가) > ")
    user_id = input("아이디를 입렺해주세요 (중복 불가) > ")
    user_pw = input("비밀 번호를 입력해주세요 > ")
    index = 0
    while True:
        try:
            if data[index]["user_name"] == user_name:
                print("-------------------------------------------")
                print("현제 사용중인 닉네임 입니다. 다시 입력해주세요 ")
                user_name = input("닉네임을 입력해주세요 (중복불가) > ")
                user_id = input("아이디를 입렺해주세요 > ")
                user_pw = input("비밀번호를 입력해주세요 > ")
                if data[index]["user_id"] == user_id:
                    print("-------------------------------------------")
                    print("현제 사용중인 아이디 입니다. 다시 입력해주세요 ")
                    user_name = input("닉네임을 입력해주세요 (중복불가) > ")
                    user_id = input("아이디를 입렺해주세요 > ")
                    user_pw = input("비밀번호를 입력해주세요 > ")
            if int(len(data)) == index:
                break
            index = index + 1
        except IndexError :
            print("회원 가입 축하드립니다.")
            break

if __name__ == '__main__' :
    user_join()