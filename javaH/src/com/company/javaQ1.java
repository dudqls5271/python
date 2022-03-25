package com.company;

import java.util.Scanner;



public class javaQ1 {
    public static void printGugudan(int index){
        for(int i = 0; i < index+1; i++) {
            for(int j = 1; j < 10; j++) {
                System.out.println(i+"*"+j + "=" + i*j);
            }

            System.out.println("=======================================");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = 1;
        while (a != 0) {
            a = scanner.nextInt();
            printGugudan(a);
        }
        scanner.close();
    }
}
