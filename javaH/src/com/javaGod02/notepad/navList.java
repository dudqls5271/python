package com.javaGod02.notepad;

import java.io.File;
import java.io.FileFilter;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;


public class navList {
    public static void nav() {
        Scanner num = new Scanner(System.in);
        System.out.println("===========================");
        System.out.println("1. 메모 쓰기");
        System.out.println("2. 메모 읽기");
        System.out.println("3. 메모 삭제");
        System.out.println("4. 메모 종료");
        System.out.println("===========================");
        System.out.print("메뉴 : ");

        int userch = num.nextInt();

        if(userch == 1) {
            nav1();
        } else if (userch == 2) {
            nav2(userch);
        } else if (userch == 3) {
            nav2(userch);
        } else if(userch == 4) {
            System.exit(0);
        }
    }

    public static void nav1() {
        addFile manager = new addFile();
        Scanner fileStr = new Scanner(System.in);
        System.out.print("메모 이름을 정해주세요 : ");
        String userfileName = fileStr.nextLine();

        System.out.print("메모의 중요도을 입력해주세요 (A,B,C) : ");
        String severity = fileStr.nextLine();

        LocalDate now = LocalDate.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy/MM/dd");
        String formatedNow = now.format(formatter);

        String filename = userfileName + ".txt";
        String filepath = "/Users/iyeongbin/Documents/GitHub/python/javaH/src/com/javaGod02/notepad/note/"+filename;

        manager.writeFile(filepath, severity, formatedNow);
    }

    public static void nav2(int userch) {
        File dir = new File("/Users/iyeongbin/Documents/GitHub/python/javaH/src/com/javaGod02/notepad/note");
        Scanner listNum = new Scanner(System.in);
        FileFilter filter = new FileFilter() {
            public boolean accept(File f) {
                return f.getName().endsWith("txt");
            }
        };
        String[] filenames = dir.list();
        for (int i = 0; i < filenames.length; i++) {
            System.out.println(i + 1 + " : " + filenames[i]);
        }
        System.out.println("번호를 고르시오 : ");
        int num = listNum.nextInt();
        read(dir, num, filter, userch);
    }


    public static void read(File dir, int num, FileFilter filter, int userch)  {
        File files[] = dir.listFiles(filter);
        for (int i = 0; i < files.length; i++) {
            if(num-1 == i) {
                if(userch == 2) {
                    try {
                        Scanner scan = new Scanner(files[i]);
                        System.out.println("file: " + files[i]);
                        while(scan.hasNextLine()){
                            System.out.println(scan.nextLine());
                        }
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                } else if(userch == 3) {
                    if( files[i].exists() ){
                        if(files[i].delete()){
                            System.out.println("파일삭제 성공");
                        }else{
                            System.out.println("파일삭제 실패");
                        }
                    }else{
                        System.out.println("파일이 존재하지 않습니다.");
                    }
                }
            }
        }
    }
}
