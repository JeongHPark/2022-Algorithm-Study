import java.util.Scanner;

public class Main {
	static int count,n,m;
	static int[] rd = {-1,0,1,0}; //북,동,남,서
	static int[] cd = {0,1,0,-1};
	static int[][] map;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Main main = new Main();
		int r,c,d;
		
		n=sc.nextInt();
		m=sc.nextInt();
		r=sc.nextInt(); //세로
		c=sc.nextInt(); //가로
		d=sc.nextInt(); //0:북,1:동,2:남,3:서
		
		map=new int[n][m];
		
		for (int i=0; i<n; i++)
		{
			for (int j=0; j<m; j++)
			{
				map[i][j]=sc.nextInt();
			}
		}
		main.clean(r,c,d);
		System.out.println(count);
	}

	public void clean(int r,int c,int d)
	{
		if (map[r][c]==0) //현재 위치 청소
		{
			count++;
			map[r][c]=2;
		}
    
    int next_d, next_r,next_c;
        
		for (int i=0; i<4; i++)
		{
            next_d = (d + 3) % 4;//현재 방향의 왼쪽 방향
            next_r = r + rd[next_d];
            next_c = c + cd[next_d];


            if (next_r >= 0 && next_c >= 0 && next_r < n && next_c < m) { //직사각형 크기 범위 내 면서
                if (map[next_r][next_c] == 0) {   // 청소해야 할 공간 존재 시
                    clean(next_r, next_c, next_d);
                    return;
                }
            }
            d=(d + 3) % 4; //방향 완전히 전환
		}

		int back=(d+2)%4; //후진
		next_r=r+rd[back];
		next_c=c+cd[back];
		
		if(next_r >= 0 && next_c >= 0 && next_r < n && next_c < m && map[next_r][next_c] != 1) {
            clean(next_r, next_c, d); //후진할 때 방향 
        }
	}
}
