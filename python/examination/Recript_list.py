import os, glob
import os.path
import datetime

from user_info import *


def recipt_list():

    try:
        targerdir = r"Reciept/" + user_name + "/"
        files = os.listdir(targerdir)

        index = 1
        for i in files:
            File_list = i.replace(".txt", "")
            File_list_data = File_list[0:10]
            File_list_time_h = File_list[11:13]
            File_list_time_m = File_list[13:15]
            File_list_time_s = File_list[15:18]
            File_list_time = File_list_time_h + ":" + File_list_time_m + ":" + File_list_time_s
            print(str(index) + ". " + File_list_data + " | " + File_list_time)
            index += 1

        import Recipt_List_Read_name
        Recipt_List_Read_name.recipt_list_read_name()
    except FileNotFoundError:
        print("영수증 리스트가 없거나 잘못 입력 했습니다.")
        import menu_view
        menu_view.menm()


if __name__ == '__main__':
    recipt_list()
