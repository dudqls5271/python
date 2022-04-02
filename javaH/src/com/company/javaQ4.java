package com.company;

import java.util.Scanner;
import java.util.ArrayList;


public class javaQ4 {
    public static void inputScanner() {
        while (true) {
            System.out.print("입력하실 숫자의 개수를 입력 해주세요 : ");
            Scanner scanner = new Scanner(System.in);
            String arrNum = scanner.nextLine();
            if(arrNum.equals("out")) {
                System.out.println("종료 합니다.");
                break;
            } else if (!arrNum.matches("[+-]?\\d*(\\.\\d+)?")) {
                System.out.println("잘못 입력 했습니다.");

            } else {
                inputArrScanner(Integer.parseInt(arrNum));
            }
        }

    }

    public static void inputArrScanner(int arrNum){
        Scanner scanner = new Scanner(System.in);
        int[] array = new int[arrNum];

        for(int i = 0; i < arrNum; i++) {
            System.out.print("숫자를 입력해주세요 : ");
            array[i] = Integer.parseInt(scanner.next());
        }

        valueSyso(arrNum, array);
    }


    public static void valueSyso(int arrNum, int[] array) {
        ArrayList<Integer> odd = new ArrayList<Integer>();
        ArrayList<Integer> even = new ArrayList<Integer>(); // 타입 지정

        for (int i = 0; i < arrNum; i++) {
            if (array[i] % 2 == 0) {
                even.add(array[i]);
            } else {
                odd.add(array[i]);
            }
        }
        System.out.println("짝수 : " + even);
        System.out.println("홀수 : " + odd);
    }

    public static void main(String[] args) {
        inputScanner();
    }
}
