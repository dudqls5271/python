package javaQ2;

public class Main {
    static boolean phoneState = true;
    public static void userChPhone() {
        System.out.println(phoneState);
        GalaxyS22 s22 = new GalaxyS22();
        s22.model();

//        Iphone12Pro iphone12pro = new Iphone12Pro();
//        iphone12pro.model();
    }

    public static void main(String[] args) {
        userChPhone();
    }
}
