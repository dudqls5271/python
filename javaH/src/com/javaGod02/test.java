package com.javaGod02;

import java.util.ArrayList;

public class test {
    public static void main(String[] args) {
        ArrayList a = new ArrayList();
        ArrayList b = new ArrayList();
         a.add(1);
         b.add(2);

         b.addAll(a);
        System.out.println("B : " + b);
        System.out.println("a : " + a);
    }
}
