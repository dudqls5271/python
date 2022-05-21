package com.javaGod02.notepad;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class addFile {
    void writeFile(String fileName, String severity, String formatedNow) {
        FileWriter fileWriter = null;
        BufferedWriter bufferedWriter = null;

        try {
            fileWriter = new FileWriter(fileName);
            bufferedWriter = new BufferedWriter(fileWriter);

            Scanner str = new Scanner(System.in);
            System.out.println("메모를 입력하시오 : ");
            String userStr = "";
            boolean bo = true;

            StringBuffer buffer = new StringBuffer();
            while (bo) {
                String temp = str.nextLine();
                if (temp.equals("exit")) {
                    userStr = buffer.toString();
                    break;
                } else {
                    buffer.append(temp+"\n");
                }
            }
            String dataStr = "중요도 : "+severity +"\n" + "입력날자 : " +formatedNow + "\n";
            bufferedWriter.write(dataStr+String.valueOf(userStr));
            bufferedWriter.newLine();

        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if(bufferedWriter != null) {
                try {
                    bufferedWriter.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if(fileWriter != null) {
                try {
                    fileWriter.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
