package com.company;

import java.util.ArrayList;
import java.util.Scanner;

public class javaQ3 {
    public static void inputNum() {
        ArrayList<Integer> num = new ArrayList<Integer>();
        Scanner scanner = new Scanner(System.in);

        for (int i = 1; i < 4; i++) {
            System.out.print(i + "번째 값을 입력해주세요 : ");
            num.add(scanner.nextInt());
        }
        numSum(num);
    }

    public static void numSum(ArrayList<Integer> num) {
        int sum = 0;
        int value = 0;
        for(int i = 0; i < num.size(); i++) {
            sum = sum + num.get(1);
        }
        value = sum / num.size();

        System.out.println("평균 : " + value);
    }

    public static void main(String[] args) {
        inputNum();
    }
}
