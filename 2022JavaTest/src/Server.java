import java.io.*;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.http.HttpRequest;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.HashMap;
import java.util.Map;

public class Server {
    public static void main(String[] args) {
        Server server = new Server();
        server.startServer();
    }


    private void startServer() {
        ServerSocket serverSocket = null;
        Socket client = null;

        try {
            serverSocket = new ServerSocket(8080);
            while (true) {
                System.out.println("Server:Waiting for request.");
                client = serverSocket.accept();

                System.out.println("Server: Accpt");

                InputStream stream =client.getInputStream();
                BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(stream));
                String data = bufferedReader.readLine();
                System.out.println("Received data : " + data + " \nArr Size : " + data.split("").length);
                System.out.println(client.getRemoteSocketAddress());
                String userIP = String.valueOf(client.getRemoteSocketAddress());
                char[] dataArr = new char[data.split("").length];

                // 데이터 배열 넣기
                for(int i = 0; i < data.split("").length; i++) {
                    dataArr[i] = data.charAt(i);
                }

                OutputStream outStream = client.getOutputStream();
                BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(outStream));

                String state = null;

                // 추가 점수 나중에 일단 기본 구현 완료
                int temp = 0;
                for(int i = 0; i < dataArr.length; i++) {
                    if(dataArr[i] == '+') {
                        temp = Integer.parseInt(String.valueOf(dataArr[i - 1])) + Integer.parseInt(String.valueOf(dataArr[i + 1]));
                        state = "1";
                    } else if (dataArr[i] == '-') {
                        temp = Integer.parseInt(String.valueOf(dataArr[i - 1])) - Integer.parseInt(String.valueOf(dataArr[i + 1]));
                        state = "1";
                    } else if (dataArr[i] == '*') {
                        temp = Integer.parseInt(String.valueOf(dataArr[i - 1])) * Integer.parseInt(String.valueOf(dataArr[i + 1]));
                        state = "1";
                    } else if (dataArr[i] == '%') {
                        temp = Integer.parseInt(String.valueOf(dataArr[i - 1])) % Integer.parseInt(String.valueOf(dataArr[i + 1]));
                        state = "1";
                    }
                }
                bufferedWriter.write(state == null ? "Not Defined Command!!" : String.valueOf(temp));
                bufferedWriter.newLine();
                bufferedWriter.flush();
                System.out.println("Return : " + temp);
                System.out.println("--------::: End :::---------");

                //=========== LOG MAKE =============
                FIleAdd manager = new FIleAdd();

                LocalDateTime now = LocalDateTime.now();
                DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd hh:mm:ss.SSS");
                String formatedNow = now.format(formatter);

                String fileName = formatedNow+".txt";
                String filePath = "/Users/iyeongbin/Documents/GitHub/python/2022JavaTest/src/serverFIle/"+fileName;
                String answer = String.valueOf(temp);
                manager.writeFileNot(filePath, formatedNow, String.valueOf(client.getRemoteSocketAddress()), data, answer);
                // ================================



            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if(serverSocket != null) {
                try {
                    serverSocket.close();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
