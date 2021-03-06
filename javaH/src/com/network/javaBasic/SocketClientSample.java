package com.network.javaBasic;

import java.io.*;
import java.net.Socket;
import java.util.Arrays;
import java.util.Date;
import java.util.Scanner;

public class SocketClientSample {
    public static void main(String[] args) {
        SocketClientSample sample = new SocketClientSample();
        sample.sendSocketSample();
    }

    private void sendSocketSample() {
        for(int loop = 0; loop < 3; loop++) {
            sendSocketData("I liked java at " + new Date());
        }
        sendSocketData("EXIT");
    }

    private void sendSocketData(String data) {
        Socket socket = null;
        try {
            Scanner scanner = new Scanner(System.in);
            System.out.print("Client : 영문을 입력 하시오 : ");
            String str = scanner.nextLine();

            socket = new Socket("127.0.0.1", 8080);
            System.out.println("Clicent:connect status = " + socket.isConnected());
            Thread.sleep(1000);
            OutputStream stream = socket.getOutputStream();
            OutputStreamWriter streamWriter = new OutputStreamWriter(stream);
            BufferedWriter bufferedWriter = new BufferedWriter(streamWriter);

            bufferedWriter.write(str);
            bufferedWriter.newLine();
            bufferedWriter.flush();

            InputStream inputStream = socket.getInputStream();       // 앞으로 받을 데이타의 대한 파일 프라임
            BufferedReader in = new BufferedReader(new InputStreamReader(inputStream));
            String recv = in.readLine();
            System.out.println("recive Data : "+recv);
        } catch (Exception e) {
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
