package com.solvecode.java;

import java.io.*;
import java.util.StringTokenizer;

public class Baek1000 {
    public static void baek1000(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter((System.out)));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int num1 = Integer.parseInt(st.nextToken());
        int num2 = Integer.parseInt(st.nextToken());

        bw.write(num1 + num2);
        bw.close();
    }
}
