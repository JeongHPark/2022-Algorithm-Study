DFS를 생각했지만 주어진 범위와 시간을 보고 시간초과가 발생할거같아서 DP 적용
dp를 사용해서 한번 구했던 탐색범위의 재탐색을 방지
경우의 수는 현재탐색하는 객차를 사용하거나 사용하지 않고 다음 객차를 사용하는 경우
두가지 경우중 큰 값을 사용
재귀문안에서 객차에 포함된 인원수를 구하는 과정을 넣었더니 시간초과
-> 밖으로 빼서 누적합을 미리 구해줘서 해결



#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int N,M;
vector<int> vec;
int result;
int allSum[55555];

void input() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		int x;
		cin >> x;
		vec.push_back(x);
	}
	cin >> M;

	for (int i = 0; i <= N-M; i++) {
		for (int j = 0; j < M; j++) {
			allSum[i] += vec[i + j];
		}
	}
}
int dp[3][55555];
int DP(int cnt,int cur) {
	if (cnt == 3 || cur >= N) { return 0; }
	if (dp[cnt][cur] != 0) { return dp[cnt][cur]; }
	
	return dp[cnt][cur]= max(DP(cnt, cur + 1), allSum[cur] + DP(cnt + 1, cur + M));

}

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	input();
	cout << DP(0, 0);
}
