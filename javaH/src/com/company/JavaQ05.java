package com.company;

import java.util.ArrayList;
import java.util.Scanner;

public class JavaQ05 {
    public static void choiceNum() {
        while (true) {
            System.out.print("입력하실 문자 개수를 입력 해주세요 : ");
            Scanner scanner = new Scanner(System.in);
            String arrNum = scanner.nextLine();
            if(arrNum.equals("out")) {
                System.out.println("종료 합니다.");
                break;
            } else if (!arrNum.matches("[+-]?\\d*(\\.\\d+)?")) {
                System.out.println("잘못 입력 했습니다.");

            } else {
                userInput(Integer.parseInt(arrNum));
            }
        }
    }

    public static void userInput(int arrNum) {
        ArrayList<String> userInputArr = new ArrayList<String>();

        Scanner scanner = new Scanner(System.in);

        for(int i = 1; i < arrNum+1; i ++) {
            System.out.print(i + "번째 문자을 입력해주세요 : ");
            userInputArr.add(scanner.nextLine());
        }
        valueOut(userInputArr);
    }

    public static void valueOut(ArrayList<String> userInputArr) {
        for(int i = 0; i < userInputArr.size(); i++) {
            System.out.print(userInputArr.get(i) + " ");
        }
        System.out.println();
    }
        public static void main(String[] args) {
            choiceNum();
    }
}
