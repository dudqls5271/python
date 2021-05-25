def is_odd(number) :
    if number % 2 == 1:
        return True
    else:
        return False

def avg_numbers(*args) :
    result = 0
    for i in args :
        result += i
    return result / len(args)

def pro3() :
    input1 = input("첫 뻔째 숫자를 입력하시오")
    input2 = input("두 뻔째 숫자를 입력하시오")

    total = int(input1) + int(input2)
    print("두 수의 합은 %s 입니다." %total)

def pro4() :
    print("you" "need" "python")
    print("you" + "need" + "python")
    print("you", "need", "python")
    print("".join(["you", "need", "python"]))

def pro5() :
    f1 = open("test.txt", "w")
    f1.write("Life is too short")

    # 이거 안해서 저장 안됨
    f1.close()

    f2 = open("test.txt", "r")
    print(f2.read())

def pro6() :
    user_input = input("지정할 내용을 입력히세요 : ")
    f = open("test.txt", "a")
    f.write(user_input)
    f.write("\n")
    f.close()

def pro7() :
    f = open("test.txt", "r")
    body = f.read();
    f.close()
    body = body.replace("java", "python")

    f = open("test.txt", "w")
    f.write(body)
    f.close()
if __name__ == '__main__':
    pro7()