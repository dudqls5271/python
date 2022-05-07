package com.javaGod02;

import java.util.HashMap;

public class checkHashMap {
    public static void main(String[] args) {
        HashMap<String, String> map = new HashMap<String, String>();

        map.put("A","a");

        System.out.println(map.containsKey("A"));
        System.out.println(map.containsKey("B"));
    }

}
