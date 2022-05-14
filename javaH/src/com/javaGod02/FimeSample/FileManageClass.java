package com.javaGod02.FimeSample;

import java.io.File;
import java.io.IOException;

public class FileManageClass {
    public static void main(String[] args) {
        FileManageClass smapl = new FileManageClass();
        String pathName = "/Users/iyeongbin/Documents/GitHub/python/javaH/src/com/javaGod02/FimeSample";
        String fileName = "text.txt";

        smapl.checkFile(pathName, fileName);
    }

    private void checkFile(String pathName, String fileName) {
        File file = new File(pathName, fileName);

        try {
            System.out.println("Create result = " + file.createNewFile());
            getFileInfo(file);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void getFileInfo(File file) throws IOException {
        System.out.println("Absolute path = " + file.getAbsolutePath());
        System.out.println("Absolute file = " + file.getAbsoluteFile());
        System.out.println("Absolute path = " + file.getAbsolutePath());
        System.out.println("Absolute file = " + file.getCanonicalFile());

        System.out.println("Name = " + file.getName());
        System.out.println("Path = " + file.getPath());
    }
}
