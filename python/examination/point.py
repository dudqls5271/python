import json
from Payment import *
from user_info import *
from Payment import *

with open("user.json", "r", encoding="utf-8") as handle:
    jdata = handle.read()
data = json.loads(jdata)

point = None

def porint():
    global point
    print(user_name)
    with open('user.json', 'r', encoding='UTF-8') as f:
        json_data_defore = json.load(f)

        point = int(price_sum) * 0.03
        print(str(round(point)) + "원 정립 되었습니다.")

        index = 0
        while True:
            if data[str(index)]["user_name"] == str(user_name):
                porint_re = int(data[str(index)]["user_point"]) + int(round(point))

                json_data_defore[str(index)]["user_point"] = porint_re

                with open('user.json', 'w', encoding='UTF-8') as mk_f:
                    mk_f.write((json.dumps(json_data_defore, indent='\t')))
                mk_f.close()

                import Receipt
                Receipt.receipt()

                import menu_view
                menu_view.menm()
                break
            index = index + 1
            if int(len(data)) == index:
                break

if __name__ == '__main__':
    porint()