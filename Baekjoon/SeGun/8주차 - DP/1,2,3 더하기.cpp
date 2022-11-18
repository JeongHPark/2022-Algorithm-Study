//1,2,3 을 1,2,3의 합으로 만들 수 있는 경우의수를 먼저 구해서 저장시켜줌
//4를 만드는 경우의수는 1을 만들 수있는 경우에 3을 더하는것과 2를 만들 수 있는경우에 2를 더하거나 3을 만들수 있는경우에 1을 더하는 것과같기때문에
//dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]); 이 점화식이 성립한다.

#include<iostream>
#include<vector>

using namespace std;

int main(void) {
	int T;
	int dp[11] = { 0,1,2,4,0,0,0,0,0,0,0 };	//dp[x] 는 x를 1,2,3 의 합으로 나타낼 수 있는 경우의 수
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N;
		cin >> N;
		if (dp[N] != 0) { cout << dp[N] << endl; }
		else {
			for (int i = 4; i <= N; i++) {
				dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]);
			}
			cout << dp[N] << endl;
		}
	}
}
