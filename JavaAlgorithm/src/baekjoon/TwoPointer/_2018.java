package baekjoon.TwoPointer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _2018 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        //투 포인터 초기화
        long start = 1;
        long end = 1;
        long sum = 1;
        //정답 변수(자기 자신으로 만족하는 정답케이스 포함)
        long count = 1;

        while (end != n) {
            if (sum == n) {
                count++; end++; sum = sum + end;
            } else if (sum > n) {
                sum = sum - start;
                start++;
            } else {
                end++; sum = sum + end;
            }

        }
        System.out.println(count);

    }
}
