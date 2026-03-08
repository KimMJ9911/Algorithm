import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int idx_1 = 0;
        int idx_2 = 0;

        for (int i = 0; i < n; i++) {
            String channel_name = br.readLine();
            if (channel_name.equals("KBS1")) idx_1 = i;
            if (channel_name.equals("KBS2")) idx_2 = i;
        }

        //idx_1 은 0으로 가야하고 idx_2 는 1로 가야함
        //최악의 경우라도 왔다 갔다 400번 내외로 가능함

        if (idx_1 > idx_2) idx_2++;
        sb.append("1".repeat(idx_1)).append("4".repeat(idx_1));
        sb.append("1".repeat(idx_2)).append("4".repeat(idx_2 - 1));

        bw.write(String.valueOf(sb));
        bw.flush();
        br.close();
        bw.close();
    }
}