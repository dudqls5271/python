import json
from user_info import *

with open("user.json", "r", encoding="utf-8") as handle:
    jdata = handle.read()
data = json.loads(jdata)

def mypoints():
    index = 0
    while True :
        # print(data[index]["name"])
        if data[index]["user_name"] == user_name:
            print("포인트 입니다. " + str(data[index]["user_point"]))
            import menu_view
            menu_view.menm()
        index = index + 1
        if int(len(data)) == index:
            break
if __name__ == '__main__' :
    mypoints()