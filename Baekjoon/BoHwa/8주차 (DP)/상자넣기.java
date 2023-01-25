/*
arr : 1 6 2 5 7 3 5 6
dp :  1 1 1 1 1 1 1 1

6은 1보다 크므로 6 자리의 dp 값을 1자리의 dp 값에 +1 해준다.
1 6 2 5 7 3 5 6
1 2 1 1 1 1 1 1

2는 1보다 크므로 
1 6 2 5 7 3 5 6
1 2 2 1 1 1 1 1

5는 1보다 크므로
1 6 2 5 7 3 5 6
1 2 2 2 1 1 1 1
5는 2보다도 크므로 현재 dp 값인 2와 2의 dp 값인 2에 +1 한 값을 비교하여 더 큰 값을 dp에 넣는다.
1 6 2 5 7 3 5 6
1 2 2 3 1 1 1 1
...
*/
import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		int n=0, max=0;
		Scanner sc = new Scanner(System.in);
		
		n=sc.nextInt();
		int[] arr = new int[n];
		int[] dp=new int[n];
		
		for (int i=0; i<n; i++)
		{
			arr[i]=sc.nextInt();
		}
		
		Arrays.fill(dp,1); //dp 배열을 1로 채우기
		for (int i=1; i<n; i++)
		{
			for (int j=0; j<i; j++)
			{
				if (arr[i]>arr[j]) {
					dp[i]=Math.max(dp[i], dp[j]+1);
				}
			}
			max=Math.max(max, dp[i]);
		}
		System.out.println(max);
		
	}	
}
