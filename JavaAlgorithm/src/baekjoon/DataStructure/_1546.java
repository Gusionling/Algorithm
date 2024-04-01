package baekjoon.DataStructure;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _1546 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int A[] = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        long sum=0;
        long max=0;

        //실은 배열에 데이터를 저장할 필요가 없는 문제이다.
        for (int number : A) {
            if(number > max) max = number;
            sum = sum + number;
        }

        System.out.println(sum*100.0/max/N);
    }
}
