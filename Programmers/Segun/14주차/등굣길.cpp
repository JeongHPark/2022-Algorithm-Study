문제를 보고 dp를 사용해야된다고 생각
현재의 좌표값은 왼쪽 또는 위쪽에서 도달할 수있기때문에 경우의수 2가지
dp를 사용해서 현재 좌표까지 오는 거리의 경우의 수를 저장하면서 진행
puddle은 -1로 지나가지 못하게 설정하고 dp 값을 수정할때마다 % 1000000007

#include <string>
#include <vector>
#include<iostream>

using namespace std;
int dp[111][111];
int solution(int m, int n, vector<vector<int>> puddles) {
	int answer = 0;
	dp[0][0] = 1;
	for (int i = 0; i < puddles.size(); i++) {
		dp[puddles[i][1] - 1][puddles[i][0] - 1] = -1;
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if ((i != 0 || j != 0) && dp[i][j] != -1) {
				if (i - 1 >= 0 && dp[i - 1][j] != -1) {
					dp[i][j] += dp[i - 1][j] % 1000000007;
				}
				if (j - 1 >= 0 && dp[i][j - 1] != -1) {
					dp[i][j] += dp[i][j - 1] % 1000000007;
				}
			}
		}
	}
	return dp[n - 1][m - 1] % 1000000007;
}
