package com.network.javaFile;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class FileAdd {
    void writeFileNot(String fileName, String formatedNow, String data, String sortation) {
        FileWriter fileWriter = null;
        BufferedWriter bufferedWriter = null;

        try {
            System.out.println("--------파일생성 시작-------");
            fileWriter = new FileWriter(fileName);
            bufferedWriter = new BufferedWriter(fileWriter);

            String dataStr =  "입력날자 : " +formatedNow + "\n" + "\n" + data;
            bufferedWriter.write(dataStr);
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
