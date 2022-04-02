package com.company;

import java.util.Scanner;

public class javaQ1 {

    public static void inputNum() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("첫 번쨰 값을 입력해주세요 : ");
        int num1 = scanner.nextInt();
        System.out.print("두 번째 값을 입력해주세요 : ");
        int num2 = scanner.nextInt();

        valueOut(num1, num2);
    }

    public static void valueOut(int num1, int num2) {
        System.out.println(num1 + "+" + num2 + "=" + (num1+num2));
        System.out.println(num1 + "-" + num2 + "=" + (num1-num2));
        System.out.println(num1 + "*" + num2 + "=" + num1*num2);
        System.out.println(num1 + "/" + num2 + "=" + num1/num2);
    }

    public static void main(String[] args) {
        inputNum();
    }
}
