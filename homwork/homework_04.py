name = "CGV"

# 시간은 동일 대신 좌석은 영호관 마다 다르다.

## 영화 종류
movies = {'승리호' : '14:00',
          '어벤저스' :'08:00',
          '배놈' : '10:00'}
## 지역을 표시
areas = {'시흥': ['장현', '배곧']}

def movies_chek():
    print(movies.keys())
    print("영화를 선택해주세요")
    movie_input = input()
    movie = movies.get(movie_input)
    if movie is None:
        print("선택하신 영화는 없습니다.")

def area_chek():
    print(areas.keys())
    print("지역 선택해주세요")
    area_input = input()

    area = areas.get(area_input)
    if area is None:
        print("선택하신 지역은 없습니다.")

if __name__ == '__main__':
    inputText = ""
    while (inputText!="0"):
        movies_chek()
        area_chek()