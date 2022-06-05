package com.network.javaBasic;

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
            System.out.print("Client : 영문을 입력 하시오 : ");
            String str = scanner.nextLine();

            socket = new Socket("127.0.0.1", 9999);
            System.out.println("Clicent:connect status = " + socket.isConnected());
            Thread.sleep(1000);
            OutputStream stream = socket.getOutputStream();
            BufferedOutputStream out = new BufferedOutputStream(stream);
            byte[] bytes = str.getBytes();
            out.write(bytes);
            InputStream inputstream = socket.getInputStream();
            BufferedReader in = new BufferedReader(new InputStreamReader(inputstream));
            StringBuffer receivedData = new StringBuffer();
            String serverData = null;
            while ((serverData = in.readLine()) != null) {
                receivedData.append(serverData);
                System.out.println("test");
                
            }
            out.close();
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
