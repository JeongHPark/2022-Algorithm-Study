import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Main main = new Main();
		int n,m;
		int[] arr, answer;
		
		n=sc.nextInt();
		arr=new int[n];
		
		for (int i=0; i<n; i++)
		{
			arr[i]=sc.nextInt();
		}
		Arrays.sort(arr);
		
		m=sc.nextInt();
		answer=new int[m];
		
		for (int i=0; i<m; i++)
		{
			int a=sc.nextInt();
			if (main.checkExistence(arr,a)) {
				answer[i]=1;
			}
		}
		for (int i=0; i<m; i++)
		{
			System.out.println(answer[i]);
		}
		
	}

	public boolean checkExistence(int[] arr,int data)
	{
		int low=0,high=arr.length-1;
		
		while(low<=high)
		{
			int mid=(low+high)/2;
			if (arr[mid]<data)
			{
				low=mid+1;
			}
			else if (arr[mid]>data)
			{
				high=mid-1;
			}
			else {
				return true;
			}
		}
		return false;
	}
}
