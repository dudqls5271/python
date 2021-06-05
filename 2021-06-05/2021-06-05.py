import random


def ex():
    list = []  # 리스트생성
    rnum = random.randint(0, 10)

    for i in range(1):
        while rnum in list:
            rnum = random.randint(0, 100)
        list.append(rnum)

    list.sort()

    Word_list = ["apple", "actor", "airplane", "always", "animal", "angry", "arrive", "autumm", "baby", "maplestory"]
    word_len = len(Word_list[list[0]])
    random_word = Word_list[list[0]]

    try_num = 10
    print("현제 남은 횟수는 " + str(try_num) + "번 입니다.")

    word_list = []
    word_qust = []

    for i in range(word_len):
        word_qust.append("_")
    print(word_qust)
        # print("_", end=" ")

    for i in random_word:
        word_list.append(i)
    print(word_list)

    index = 0
    while True:
        user_ch = input("알파벳을 입력해주세요 > ")
        for i in random_word:
            if user_ch == word_list[index]:
                print("있다")
                break
        index = index + 1
    #
    # for i in range(word_len):
    #     print("_", end=" ")
    #
    # user_ch = input("알파벳을 입력해주세요 > ")
    # while True:
    #     for i in random_word:
    #         if user_ch == i :
    #             print("있습니다.")
    #             print(random_word.find(user_ch))
    #             for j in range(word_len-1):
    #
    #                 print("_", end=" ")
    #     break


if __name__ == "__main__":
    ex()