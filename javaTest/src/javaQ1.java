import java.util.Scanner;
public class javaQ1 {
    public static void userInput() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("단어를 입력 하시오 : ");
        String userStr = scanner.nextLine();
        userWorldCode(userStr);
    }

    public static void userWorldCode(String userStr) {
        int[] world = new int[26];
        for (int i = 0; i < userStr.length(); i++){
            if (65 <= userStr.charAt(i) && userStr.charAt(i) <= 90) {
                world[userStr.charAt(i) - 65]++;
            }
            else {
                world[userStr.charAt(i) - 97]++;
            }
        }
        userWorldMax(world);
    }

    public static void userWorldMax(int[] world) {
        int max = -1;
        char ch = '?';

        for (int i = 0; i < 26; i++) {
            if (world[i] > max) {
                max = world[i];
                ch = (char) (i + 65);
            }
            else if (world[i] == max) {
                ch = (char) world[i];
            }
        }
        System.out.print(ch);
    }


    public static void main(String[] args) {
        userInput();
    }
}
