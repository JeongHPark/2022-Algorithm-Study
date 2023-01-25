import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static int[][] graph;
	static boolean[][] visited;
	static int M;
	static int N;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int count=0;
		Main ma=new Main();
		int T=sc.nextInt();
		for (int i=0; i<T; i++)//테스트 케이스
		{
			count=0;
			M=sc.nextInt();
			N=sc.nextInt();
			
			graph=new int[M][N];
			visited=new boolean[M][N];
			int K=sc.nextInt();
			for (int j=0; j<K; j++)
			{
				int X=sc.nextInt();
				int Y=sc.nextInt();
				graph[X][Y]=1;
			}
			
			for (int j=0; j<M; j++) {
				for (int k=0; k<N; k++) {
					if (graph[j][k]==1&&!visited[j][k]) {
						ma.bfs(j,k);
						count++;
					}
				}
			}
			System.out.println(count);
		}
	}

	public void bfs(int x, int y)
	{
		Queue<int[]> q = new LinkedList<>();
		int[] row= {-1,1,0,0};
		int[] column= {0,0,-1,1};
		
		q.add(new int[] {x,y});
		visited[x][y]=true;
		while(!q.isEmpty())
		{
			int[] arr=q.poll();
			for (int i=0; i<4; i++) {
				int newX=arr[0]+row[i];
				int newY=arr[1]+column[i];
				if (newX>=0&&newY>=0&&newX<M&&newY<N) {
					if (!visited[newX][newY]&&graph[newX][newY]==1) {
						q.add(new int[] {newX,newY});
						visited[newX][newY]=true;	
					}
				}
			}
		}
	}
}
