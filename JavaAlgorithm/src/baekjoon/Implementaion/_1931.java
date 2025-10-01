import java.io.*;
import java.util.*;


public class _1931 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[][] lectures = new int[N][2];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            lectures[i][0] = Integer.parseInt(st.nextToken()); // 시작 시간
            lectures[i][1] = Integer.parseInt(st.nextToken()); // 끝 시간
        }


        Array.sort(lectures, (a, b) -> {
            if (a[1] == b[1]) {
                return a[0] - b[0];
            }
            return a[1] - b[1];
        });

        int count = 0;
        int endTime = 0;

        for (int i = 0; i < N; i++) {
            if (lectures[i][0] >= endTime) {
                count++;
                endTime = lectures[i][1];
            }
        }

        System.out.println(count);
    }

}