import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int[] arr;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine() , " ");
            int idx = Integer.parseInt(st.nextToken());
            arr = new int[21];
            arr[0] = Integer.MIN_VALUE;

            for (int j = 1; j <= 20; j++) {
                arr[j] = Integer.parseInt(st.nextToken());
            }

            int total = 0;

            for (int j = 2; j <= 20; j++) {
                int curr_cnt = 0;
                for (int k = j; k >= 1; k--) {
                    if (arr[k - 1] > arr[k]) {
                        change(k);
                        curr_cnt++;
                    } else break;
                }
                total += curr_cnt;
            }
            sb.append(idx).append(" ").append(total).append("\n");
        }

        bw.write(String.valueOf(sb));
        bw.flush();
        br.close();
        bw.close();
    }

    static void change(int curr) {
        int val = arr[curr - 1];
        arr[curr - 1] = arr[curr];
        arr[curr] = val;
    }
}