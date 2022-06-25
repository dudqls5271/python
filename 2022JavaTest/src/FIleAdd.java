import javax.swing.plaf.ViewportUI;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class FIleAdd {
    void writeFileNot(String fileName, String formatedNow, String userIP, String requst, String answer) {
        FileWriter fileWriter = null;
        BufferedWriter bufferedWriter = null;

        try {
            System.out.println("======= Make LOG FILE ======");
            fileWriter = new FileWriter(fileName);
            bufferedWriter = new BufferedWriter(fileWriter);

            String dataStr = formatedNow + "-" + userIP + ":" + requst + "->" + answer;
            bufferedWriter.write(dataStr);
            bufferedWriter.newLine();
            bufferedWriter.close();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (bufferedWriter != null) {
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
