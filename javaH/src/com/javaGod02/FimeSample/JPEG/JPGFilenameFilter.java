package com.javaGod02.FimeSample.JPEG;

import java.io.File;
import java.io.FilenameFilter;

public class JPGFilenameFilter implements FilenameFilter {
    @Override
    public boolean accept(File file, String fileName) {
        if(fileName.endsWith(".jpg")) return true;
        return false;
    }
}
