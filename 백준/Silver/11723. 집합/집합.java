import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static StringBuilder sb = new StringBuilder();
    static int[] ans;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        ans = new int[21];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine() , " ");
            String command = st.nextToken();
            int num = 0;
            if (!(command.equals("all") || command.equals("empty")))
                num = Integer.parseInt(st.nextToken());

            input(command , num);
        }
        bw.write(String.valueOf(sb));
        bw.flush();
        br.close();
        bw.close();
    }

    private static void input(String command , int num) {
        switch (command) {
            case "add":
                if (ans[num] == 0)
                    ans[num] = 1;
                break;
            case "remove":
                if (ans[num] == 1)
                    ans[num] = 0;
                break;
            case "check":
                if (ans[num] == 1)
                    sb.append(1).append("\n");
                else
                    sb.append(0).append("\n");
                break;
            case "toggle":
                if (ans[num] == 1)
                    ans[num] = 0;
                else ans[num] = 1;
                break;
            case "all":
                for (int i = 1; i <= 20; i++) {
                    ans[i] = 1;
                }
                break;
            case "empty":
                ans = new int[21];
                break;
            default:
                break;
        }
    }
}