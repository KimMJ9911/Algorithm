import java.io.*;

public class Main {
    static final String USER_1 = "SK";
    static final String USER_2 = "CY";
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        // 한 턴에 가져가는 돌의 갯수가 4면 무조건 후공이 이길 수 있다.
        int val = n % 4;

        if (val % 2 == 0) sb.append(USER_2);
        else sb.append(USER_1);

        bw.write(String.valueOf(sb));
        bw.flush();
        br.close();
        bw.close();
    }
}