import java.util.*;

public class Main {
    static int[] dp=new int[11];
    public static void main(String[] args) {
        Main main = new Main();
        Scanner sc = new Scanner(System.in);

        int T=sc.nextInt();

        dp[1]=1;
        dp[2]=2;
        dp[3]=4;

        for (int i=4; i<11; i++)
        {
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3];
        }

        for (int i=0; i<T; i++)
        {
            int n=sc.nextInt();
            System.out.println(dp[n]);
        }

    }
}
