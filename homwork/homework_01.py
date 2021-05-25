def problem01() :
    a = "Life is too short, you need python"

    if "wife" in a: print("wife")
    ## 만약에 wife가 a의 문자열에 있다면 wife을 출력 해라
    elif "python" in a and "you" not in a: print("python")
    ## 그게 아니면 pyrhon과 you가 a의 문자열에 있으면 python을 출력 해라
    elif "shirt" not in a: print("shirt")
    ## 그게 아니면 shirt이 a의 문자열에 없으면 shirt을 출력해라
    elif "need" in a: print("need")
    ## 그게 아니면 need가 a의 문자열에 있으면 need을 출력해라
    else: print("none")
    ## 아니면 none을 출력해라


    ## 하지만 가장먼저 참이 되는 값은 shirt 임으로 답은
    ## 출력 되는 값은 shirt다

def problem02():
    result = 0
    i = 1
    while i <= 1000:
    ## 1000까지의 자연수 중 3의 배수의 합을 구해야 함으로 i의 범위를 1000을 잡아주고
        if i % 3 == 0:
        ## if문은 i을 3으로 나눴을때 나머지가 0이 되는 값을 걸러내기 위한 작업
            result += i
            ##만약 나머지가 0이면 result = result + i로 더해주고
        i += 1
        ## i을 1씩 올려주며 반복을 한다

    print(result)

def problem03():
    i = 0
    while True:
        i += 1
        ## while이 돌아가는 중에는 i을 계속 1을 + 해주는 작업이다.
        if i > 5:
        ## 만약에 i 가 5보다 크면 break로 whle을 중단하고
            break
        print("*" * i)
        ## i의 개수 만큼 *을 출력한다.

def problem04() :
    for i in range(1,101):
        print(i)


def problem05() :
    A = [70,60,55,75,95,90,80,80,85,100]
    total = 0
    for score in A:
        total += score
        # total = total + score 입으로 (0 = 0 + 70) 이런식으로 total을 쌓는다
    avg = total / len(A)
    print(avg)

def problem06():
    numbers = [1,2,3,4,5]
    result = [i * 2 for i in numbers if i % 2 == 1]
    ## ?? 서순
    print(result)
if __name__ == '__main__':
    problem06()