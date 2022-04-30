package com.javaGod02;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;

public class javaQ01 {
    public static void main(String[] args) {
        ArrayList<Integer> gradeArr = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        System.out.println("학생 수을 입력해주세요 : ");
        int sutNum = scanner.nextInt();

        for(int i =0; i < sutNum; i++) {
            System.out.println("성적을 입력해주세요 : ");
             int grade = scanner.nextInt();
            gradeArr.add(grade);
        }
        System.out.println(gradeArr);

        for(int i =0; i < sutNum; i++) {
            if (i == 0) {
                gradeArr.set(i, 0);
            }
            if (i == 2) {
                gradeArr.set(i, 0);
            }
            if (i == 4) {
                gradeArr.set(i, 0);
            }
        }
        System.out.println(gradeArr);

        LinkedList<Integer> gradeLink = new LinkedList();
        for(int i =0; i < sutNum; i++) {
            System.out.println("성적을 입력해주세요 : ");
            int grade = scanner.nextInt();
            gradeLink.add(grade);
        }
        System.out.println(gradeLink);

        for(int i =0; i < sutNum; i++) {
            if(i == 0) {
                gradeLink.set(i, 0);
            }
            if(i == 2) {
                gradeLink.set(i, 0);
            }
            if(i == 4) {
                gradeLink.set(i, 0);
            }
        }

        System.out.println(gradeLink);
    }
}
