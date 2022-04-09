package com.company;

import java.util.Scanner;

public class javaQ6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String inputuser = scanner.nextLine();

        System.out.println(inputuser.length());
        System.out.println(inputuser.substring(0,1) + "\n"+ inputuser.substring(inputuser.length()-1,inputuser.length()));
    }
}
