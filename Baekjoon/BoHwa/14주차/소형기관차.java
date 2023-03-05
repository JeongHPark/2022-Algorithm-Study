/*
참고 : https://comyoung.tistory.com/184
누적합과 dp 이용
배열에 이전 객차들에 탑승한 승객과 현재 객차에 탑승객을 합한 값을 저장(누적합)
소형기관차 개수에 따라 객차 개수가 최대일 때 가장 큰 값(승객 수)을 가지는 경우를 계산
*/

public class Main{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int n,max;
        int[] client;
        int[][] dp;

        n=sc.nextInt(); //객차 수
        client=new int[n+1];//각 객차의 탑승객을 그 전까지의 객차 탑승객에 누적하여 저장하는 배열

        for (int i=1; i<=n; i++)
        {
            int tmp=0;
            tmp=sc.nextInt();
            client[i]=client[i-1]+tmp;
        }

        max=sc.nextInt();//소형기관차가 최대로 끌 수 있는 객차 수

        dp=new int[4][n+1];

        for (int i=1; i<=3; i++)
        {
            for (int j=i*max; j<=n; j++){ //소형기관차 개수에 따른 최대 객차 수
                dp[i][j]=Math.max(dp[i][j-1],dp[i-1][j-max]+(client[j]-client[j-max]));//이전 값과 (소형기관차가 1개 줄었을 때 값 + 소형기관차 하나에 대한 승객 수)를 비교 
            }
        }
        System.out.println(dp[3][n]); //배열의 가장 끝 값이 최댓값이다.
    }
}
