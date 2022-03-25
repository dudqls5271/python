package com.company;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // write your code here
        Scanner scanner = new Scanner(System.in);
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();
        System.out.println(num1+"+" +num2+ "=" + (num1+num2));
        System.out.println(num1+"*" +num2+ "=" + (num1*num2));
        System.out.println(num1+"-" +num2+ "=" + (num1/num2));
        System.out.println(num1+"-" +num2+ "=" + ( num1-num2));
    }
}
