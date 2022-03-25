import json
import menu_view
with open("user.json", "r", encoding="utf-8") as handle:
    jdata = handle.read()
data = json.loads(jdata)

user_name = None
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

            try:
                index = 0
                while True:
                    if data[str(index)]["user_id"] == user_id and data[str(index)]["user_pw"] == user_pw:
                        print(data[str(index)]["user_name"] + "님 환영합니다.")
                        user_name = data[str(index)]["user_name"]
                        print("-------------------------------------------------")
                        menu_view.menm()
                        break
                    if int(len(data)) == str(index):
                        break
                    index = index + 1
            except IndexError:
                print("잘못 입력하셨습니다.")

        elif str(user_ch) == "2" :
            print("회원가입")
            break
        else:
            print("잘못 입력 하였습니다.")
if __name__ == '__main__':
    user()