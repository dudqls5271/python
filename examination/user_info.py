import json
import menu_view
with open("user.json", "r", encoding="utf-8") as handle:
    jdata = handle.read()
data = json.loads(jdata)

user_name = "이영빈"
def user():
    global user_name
    index = 0
    while True:
        print("번호를 선택해주세요")
        print("로그인 (1), 회원가입(2)")
        user_ch = input()

        if str(user_ch) == "1" :
            print("아이디를 입력하세요. >", end=' ')
            user_id = input()
            x = user_id
            print("패스워드를 입력하세요. > ", end=' ')
            user_pw = input()

            if data[index]["user_id"] == user_id and data[index]["user_pw"] == user_pw:
                print(data[index]["user_name"] + "님 환영합니다.")
                user_name = data[index]["user_name"]
                print("-------------------------------------------------")
                menu_view.menm()
                break
                index = index + 1
            else:
                print("아이디 또는 비밀번호가 일치 하지 않습니다.")
            if int(len(data)) == index:
                break

        elif str(user_ch) == "2" :
            print("회원가입")
            break
        else:
            print("잘못 입력 하였습니다.")
if __name__ == '__main__':
    user()