package com.network.javaBasic;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class SoketServerSample {
    public static void main(String[] args) {
        SoketServerSample sample = new SoketServerSample();
        sample.startServer();
    }

    private void startServer() {
        ServerSocket server = null;
        Socket client = null;
        try {
            server = new ServerSocket(9999);
            while (true) {
                System.out.println("Server:Waiting for request.");
                client = server.accept();
                System.out.println("Server:Accpted");
                InputStream stream = client.getInputStream();
                BufferedReader in = new BufferedReader(new InputStreamReader(stream));
                String data = null;
                StringBuffer receivedData = new StringBuffer();
                while ((data = in.readLine()) != null) {
                    receivedData.append(data);
                }
                OutputStream outPutstream = client.getOutputStream();
                BufferedOutputStream out = new BufferedOutputStream(outPutstream);
                char[] caster = receivedData.toString().toCharArray();
                byte[] bytAsc = new byte[caster.length];
                for(int i = 0; i < caster.length; i++) {
                    bytAsc[i] = (byte) caster[i];
                    System.out.println("Requst data to Asc : " + bytAsc[i]);
                }
                out.write(bytAsc);
                in.close();
                stream.close();
                client.close();
                if(receivedData != null && "EXIT".equals(receivedData.toString())) {
                    System.out.println("Stop SocketServer");
                    break;
                }
                System.out.println("----------------");
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
