import java.io.*;
import java.net.InetAddress;
import java.net.Socket;
import java.sql.SQLOutput;
import java.util.Date;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        Client client = new Client();
        client.endClient();
    }

    private void endClient() {
        // 테스트 용 나중에 수정 해라
        clientData("EXIT");
    }

    private void clientData(String data) {
        Socket socket = null;
        try {
            Scanner scanner = new Scanner(System.in);
            System.out.println("서버에 보낼 계산식을 입력 하시오 : ");
            String userStr = scanner.nextLine();
            InetAddress ip = InetAddress.getLocalHost();

            if(userStr.equals("EXIT")) {
                clientData("EXIT");
            }

            socket = new Socket(ip.getHostAddress(), 8080);
            System.out.println("Client:connect status = " + socket.isConnected());
            Thread.sleep(1000);

            // 서버로 데이토 보냄
            OutputStream stream = socket.getOutputStream();
            OutputStreamWriter streamWriter = new OutputStreamWriter(stream);
            BufferedWriter bufferedWriter = new BufferedWriter(streamWriter);

            bufferedWriter.write(userStr);
            bufferedWriter.newLine();
            bufferedWriter.flush();

            // 서버에서 데이터를 받음
            InputStream inputStream = socket.getInputStream();
            BufferedReader in = new BufferedReader(new InputStreamReader(inputStream));
            String reve = in.readLine();
            System.out.println("Server Requt : " + reve);

        } catch (Exception e){
            e.printStackTrace();
        } finally {
            if(socket != null) {
                try {
                    socket.close();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
    }
 }
