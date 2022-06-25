package com.network.javaBasic;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;

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
                System.out.println("Received data : " + data);

                OutputStream outStream = client.getOutputStream(); //보낼 스트림
                BufferedWriter out = new BufferedWriter( new OutputStreamWriter( outStream ) );
                byte[] bytes = data.getBytes(StandardCharsets.US_ASCII);
                StringBuffer sb = new StringBuffer();
                for( byte b : bytes) {
                    sb.append( String.format("%s ", b ));
                }
                out.write(sb.toString());
                out.newLine();
                out.flush();
                System.out.println("Return : "+sb.toString());
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
