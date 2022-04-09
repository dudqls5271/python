package com.company;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class javaQ7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String userInput = scanner.nextLine();
        String userCh = scanner.nextLine();
        char[] inputArr = userInput.toCharArray();
        if(userCh.equals("1")) {
            for(int i = 0; i < userInput.length(); i++) {
                if (i % 2 != 0) {
                    System.out.print(inputArr[i] + " ");
                }
            }
        } else {
            for(int i = 0; i < userInput.length(); i++) {
                if(i % 2 == 0) {
                    System.out.print(inputArr[i] + " ");
                }
            }
        }
    }
}
