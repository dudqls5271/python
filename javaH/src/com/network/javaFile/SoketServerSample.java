package com.network.javaFile;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class SoketServerSample {
    public static void main(String[] args) {
        SoketServerSample sample = new SoketServerSample();
        sample.startServer();
    }

    private void startServer() {
        ServerSocket server = null;
        Socket client = null;
        try {
            server = new ServerSocket(8080);
            while (true) {
                System.out.println("Server:Waiting for request.");
                client = server.accept();
                System.out.println("Server:Accpted");
                InputStream stream = client.getInputStream();
                BufferedReader in = new BufferedReader(new InputStreamReader(stream));
                String data = in.readLine();
                //-------------------------------------------------------
                String sortation = "server";

                FileAdd manager = new FileAdd();
                LocalDateTime now = LocalDateTime.now();
                DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd hh:mm:ss.SSS");
                String formatedNow = now.format(formatter);

                String filename = formatedNow + ".txt";
                String filepath = "/Users/iyeongbin/Documents/GitHub/python/javaH/src/com/network/javaFile/serverFile/"+filename;

                manager.writeFileNot(filepath, formatedNow, data, sortation);
                //-------------------------------------------------------

                OutputStream outStream = client.getOutputStream(); //보낼 스트림
                File file = new File(filepath);
                BufferedOutputStream bufferedOutputStream = new BufferedOutputStream(outStream);

                FileInputStream fileInputStream = new FileInputStream(file);
                BufferedInputStream bufferedInputStream = new BufferedInputStream(fileInputStream);
                byte[] buffer = new byte[1024];
                int readed = -1;
                while ((readed = bufferedInputStream.read(buffer)) > 0 ) {
                    bufferedOutputStream.write(buffer, 0, readed);
                }
                bufferedOutputStream.flush();
                System.out.println("--------::: End :::---------");
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if(server != null) {
                try {
                    server.close();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
