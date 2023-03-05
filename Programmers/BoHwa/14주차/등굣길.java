/*
DP 이용
웅덩이가 있는 곳을 -1로 지정해놓는다.
for 문으로 2차원 배열에 접근하면서 웅덩이(-1)인 경우 0으로 바꾸고 다음 좌표로 넘어간다.
웅덩이가 아닌 경우에는 왼쪽과 위쪽의 값을 더한다.
*/

class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        int[][] map=new int[n+1][m+1];

        map[1][1]=1;

        for (int[] loc:puddles)
        {
            int x=loc[1], y=loc[0]; //좌표 순서 주의
            map[x][y]=-1;
        }
        for (int i=1; i<=n; i++)
        {
            for (int j=1; j<=m; j++)
            {
                if (map[i][j]==-1){
                    map[i][j]=0;
                    continue;
                }
                map[i][j]+=(map[i-1][j]+map[i][j-1])%1000000007;
            }
        }
        answer=map[n][m];

        return answer;
    }
}
