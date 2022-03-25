from user_info import *

def recipt_list_read_name():

    read_name = input("조회 하실 영수증을 입력해주세요 EX) 2021-05-30_01:46:19 > ")
    re = read_name.replace(":", "")
    f = open("Reciept/"+user_name+"/" + re +".txt", 'r', encoding="utf-8")
    while True:
        line = f.readline()
        if not line: break
        print(line,  end='')

    import menu_view
    menu_view.menm()
if __name__ == '__main__' :
    recipt_list_read_name()