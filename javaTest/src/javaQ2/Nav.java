package javaQ2;

import javax.swing.*;
import java.util.Scanner;

public class Nav extends Main{
    public void nav(String phoneModel){
        GalaxyS22 s22 = new GalaxyS22();
        Iphone12Pro i12Pro = new Iphone12Pro();
        XiaomiRedmi10 xphone = new XiaomiRedmi10();

        System.out.println("1) 기기정보");
        System.out.println("2) 전원ON");
        System.out.println("3) 전원OFF");

        if(phoneModel.equals("Galaxy")) {
            System.out.println("4) 빅스비");
        }
        if(phoneModel.equals("Iphone")) {
            System.out.println("4) 시리");
        }
        if(phoneModel.equals("Xiaomi")) {
            System.out.println("4) 하이구글");
        }

        System.out.println("5) 전화걸기");

        System.out.print("선택> ");
        Scanner scanner = new Scanner(System.in);
        int userCh = scanner.nextInt();

        if(userCh == 2) {
            phoneState = true;
        }

        if(!phoneState) {
            System.out.println("[ 휴대폰 전원이 꺼저 있는 상태에서는 아무것도 할 수 없습니다. ]");
            userChPhone();
        }

        if(userCh == 1) {
            System.out.println("1) 기기정보");
            System.out.println("2) 기기변경");
            System.out.print("선택> ");
            int userChNav = scanner.nextInt();
            if(userChNav == 2) {
                System.out.println("1-애플");
                System.out.println("2-삼성");
                System.out.println("3-샤오미");
                System.out.print("선택> ");
                int userChPhone = scanner.nextInt();
                if(userChPhone == 1) {
                    System.out.println("[애플 아이폰이 선택되었습니다.]");
                    i12Pro.model();
                } else if(userChPhone == 2) {
                    System.out.println("[삼성 갤럭시가 선택되었습니다.]");
                    s22.model();
                } else if(userChPhone == 3) {
                    System.out.println("[샤오미 노트가 선택되었습니다.]");
                    xphone.model();
                }
            }
            if(userChNav == 1) {
                if(phoneModel.equals("Galaxy")) {
                    s22.Phoneoption();
                }
                if(phoneModel.equals("Iphone")) {
                    i12Pro.Phoneoption();
                }
                if(phoneModel.equals("Xiaomi")) {
                    xphone.Phoneoption();
                }

            }

        } else if(userCh == 2) {
            if (phoneState) {
                System.out.println("[ 휴대폰이 켜저 있는 상태 입니다. ]");
                userChPhone();
            } else {
                phoneState = true;
                System.out.println("[ 휴대폰의 전원을 켰습니다. ]");
                userChPhone();
            }

        } else if(userCh == 3) {

            phoneState = false;
            System.out.println("[ 휴대폰 전원이 꺼졌습니다. ]");
            userChPhone();

        } else  if(userCh == 4) {
            System.out.println("1) 검색 ");
            System.out.print("선택> ");
            int userCh4 = scanner.nextInt();
            if(userCh4 == 1) {
                while (true) {
                    System.out.print("검색단어> ");
                    String userSch = scanner.nextLine();
                    System.out.println(userSch+"은" + userSch.length()+"글자 입니다.");

                    System.out.print("검색을 더 하시겠습니까? (yes OR no) ");
                    String userchSch = scanner.nextLine();

                    if(userchSch.equals("no")) {
                        break;
                    } else {

                    }
                }
                userChPhone();
            }
        } else if (userCh == 5) {
            System.out.print("이름 입력 하시오 : ");
            Scanner scanner1 = new Scanner(System.in);
            String userName = scanner1.nextLine();

            System.out.print("전회번호를 입력 하시오 : ");
            Scanner scanner2 = new Scanner(System.in);
            String phoneNum = scanner2.nextLine();

            System.out.println(userName+"의" + phoneNum+"로 전화 걸겠습니다.");
            userChPhone();
        }
        else {
            System.out.println("잘못 입력하셨습니다.");
            nav(phoneModel);
        }
    }
}
