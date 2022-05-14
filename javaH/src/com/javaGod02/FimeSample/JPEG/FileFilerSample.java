package com.javaGod02.FimeSample.JPEG;

import java.io.File;

public class FileFilerSample {
    public static void main(String[] args) {
        FileFilerSample sample = new FileFilerSample();
        String pathName = "~/Documents/GitHub/python/javaH/src/com/javaGod02/FileSample/JPEG";
        sample.checkList(pathName);
    }

    private void checkList(String pathName) {
        File file;

        try {
            file = new File(pathName);
            File []mainFileList = file.listFiles();

            for(File tempFile:mainFileList) {
                System.out.println(tempFile.getName());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
