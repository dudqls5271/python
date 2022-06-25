package com.network.javaFile;

import java.io.*;
import java.net.Socket;
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
            System.out.print("Client : \n문장을 입력하시오 [쓰기 중단 : COMPLETE] \n");

            Scanner str = new Scanner(System.in);
            String userStr = "";
            boolean bo = true;

            StringBuffer buffer = new StringBuffer();
            while (bo) {
                String temp = str.nextLine();
                if (temp.equals("COMPLETE")) {
                    userStr = buffer.toString();
                    break;
                } else {
                    buffer.append(temp+"\n");
                }
            }

            socket = new Socket("127.0.0.1", 8080);
            Thread.sleep(1000);
            OutputStream stream = socket.getOutputStream();
            OutputStreamWriter streamWriter = new OutputStreamWriter(stream);
            BufferedWriter bufferedWriter = new BufferedWriter(streamWriter);

            bufferedWriter.write(String.valueOf(buffer));
            bufferedWriter.newLine();
            bufferedWriter.flush();

            InputStream inputStream = socket.getInputStream();       // 앞으로 받을 데이타의 대한 파일 프라임
            BufferedInputStream bufferedInputStream = new BufferedInputStream(inputStream);
            BufferedOutputStream bot = new BufferedOutputStream(
                    new FileOutputStream(new File("/Users/iyeongbin/Documents/GitHub/python/javaH/src/com/network/javaFile/clientFile/test.txt")));

            byte[] bufferFile = new byte[1024];
            int readed = -1;

            while ((readed = bufferedInputStream.read(bufferFile)) > 0) {
                bot.write(bufferFile, 0, readed);
            }
            bot.flush();
            bot.close();
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
