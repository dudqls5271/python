package com.network;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.sql.SQLOutput;

public class DatagramServerSample {
    public static void main(String[] args) {
        DatagramServerSample sample = new DatagramServerSample();
        sample.starServer();
    }

    private void starServer() {
        DatagramSocket server = null;
        try {
            server = new DatagramSocket(9999);
            int bufferLength = 256;
            byte[] buffer = new byte[bufferLength];
            DatagramPacket packet = new DatagramPacket(buffer, bufferLength);

            while (true) {
                System.out.println("Server:Waiting for requst");
                server.receive(packet);
                int dataLength = packet.getLength();
                System.out.println("Server:received. Data lenth = " + dataLength);
                String data = new String(packet.getData(), 0, dataLength);
                System.out.println("Receivde data : " + data);

                if(data.equals("EXIT")) {
                    System.out.println("Stop DatargramServer");
                    break;
                }
                System.out.println("---------------");
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
