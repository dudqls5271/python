import json

with open("user.json", "r", encoding="utf-8") as handle:
    jdata = handle.read()
data = json.loads(jdata)
def user_join_json():

    index = 0
    while True:
        temp = data[str(index)]


        car_group = dict()
        car_group[index] = temp
        avante = dict()
        avante["price"] = "3000"
        avante["year"] = "2014"
        car_group[123] = avante
        print(car_group)
        index += 1
        # json 파일로 저장
        # with open('user.json', 'w', encoding='utf-8') as make_file:
        #     json.dump(car_group, make_file, indent="\t")
        # index = index + 1
        if int(len(data)) == index:
            break

if __name__ == '__main__':
    user_join_json()