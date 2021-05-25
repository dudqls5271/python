def problem01():
    kor = 80
    eng = 75
    math = 55
    print((kor + eng + math)/3)

def problem02():
    num = 13
    if num%2 != 0 :
        print(str(num) + "은 홀수 입니다.")
    else:
        print(str(num) + "은 짝수 입니다.")

def problem03():
    pin = "881102-1068234"
    lastyy = pin[0:2]
    firstyy = "0"
    mm = pin[2:4]
    dd = pin[4:6]
    num = pin[7:]

    if pin[7:8] == "1" or pin[7:8] == "2":
        firstyy = "19"
    elif pin[7:8] == "3" or pin[7:8] == "4":
        firstyy = "20"

    print(firstyy + lastyy + mm + dd)
    print(firstyy + lastyy + "." + mm + "." + dd)
    print(num)

def problem04():
    pin = "881102-1068234"

    if pin[7:8] == "1" or pin[7:8] == "3":
        print("남자")
    elif pin[7:8] == "2" or pin[7:8] == "4":
        print("여자")

    print(pin[7:8])

def problem05() :
    a = "a:b:c:d"
    b = a.replace(":","#")

    print(b)

def problem06() :
    a = [1,3,5,4,2]
    print(a)
    # sort() = > 오름차순 정렬
    a.sort()
    print(a)
    a.reverse()
    print(a)

def problem07() :
     a = ["Life", "is", "too", "short"]
     # join에 공백을 주어서 뛰어 쓰기를 함
     result = " ".join(a)
     print(result)

def problem08() :
    # id() => 메모리 주소 출력
    a = (1,2,3)
    print(id(a))

    # id을 출력 해보니 2개의 튜플의 메모리 값이 맞지 않는다
    # 그 이유는 변경된 튜플은 변경하는 동안 새롭게 만들어진 튜플이기 때문이다.

    a = a + (4,)
    print(id(a))
    print(a)

def problem09() :
    a = dict()

    # 1)
    # a["name"] = "python"

    # 2)
    # a[('a',)] = "python"

    # 3)
    a[[1]] = "python"

    # 딕셔너리는 순서가 없는 집합? 인데 a[[1]]은 리스트? 형식이여서 않되는 듯 하다.

    #  오류 문구
    # Traceback(most recent call last):
    # File, line92, in < module >
    #
    # File, line 85, in problem09
    # a[[1]] = "python"
    # TypeError: unhashable
    # type: 'list'

    # 4)
    # a[250] = 'python'

    print(a)

def problem10() :
    a = {"A" : 90,
         "B" : 80,
         "C" : 70}
    # result = a.get("B")
    result = a.pop("B")

    # 책에서 나오는 힌트는 pop을 쓰라고 했지만 pop는 특정 값을 리턴하고 삭제 하는 반면에
    # get은 키를 리턴하고, 만약 키가 없다면 디폴트 값을 반환 한다고 한다.

    print(a)
    print(result)

def problem11() :
    a = [1,1,1,2,2,3,3,3,4,4,5,5]
    ## 1) set은 중복을 허용하지 않는다.
    ## 2) 순서가 없다
    b = set(a)
    print(b)

    a = list(b)
    print(a)

def problem12() :
    a = b = [1,2,3]
    a[1] = 4

    print("a : " + str(id(a)))
    print("b : " + str(id(b)))

    # a 와 b의 메모리을 찍어보면 같은것을 볼수있다
    # 따라서 a 와 b는 같은 변수? 라는것이다.
    # 그래서 한쪽으로 값을 변경해줘도 다른쪽에서도 값이 변경되는것 같다.

    print("b : " + str(b))
    print("a : " + str(a))

if __name__ == '__main__':
    problem12()

