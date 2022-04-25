package javaQ2;

import java.util.Scanner;

public class GalaxyS22 extends Nav{
    String phoneModel = "Galaxy";
    public void model(){
        System.out.println( "[ 메뉴( 삼성-갤럭시22 )]");
        nav(phoneModel);
    }


    public void Phoneoption(){
        System.out.println(":::::: 삼성 갤럭시 S22 ::::::");
        System.out.println("제조사 : 삼성전자");
        System.out.println("모델명 : 갤럭시 S22");
        System.out.println("가격 : 100만원");
        model();
    }
}
