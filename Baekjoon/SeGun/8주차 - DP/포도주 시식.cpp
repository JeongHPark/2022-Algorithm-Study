#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
int N;
int arr[11111];
int dp[11111];	//dp[x] 는 x번째 포도주를 먹었을때 최대 먹는 양
int result = 0;

int main(void) {
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}

	dp[0] = arr[0];
	dp[1] = arr[0] + arr[1];
	dp[2] =max(dp[1], max(arr[0] + arr[2], arr[1] + arr[2])); 
	for (int i = 3; i < N; i++) {
		dp[i] = max(dp[i - 3]+arr[i-1]+arr[i], dp[i - 2] + arr[i]);
		dp[i] = max(dp[i], dp[i - 1]);
	}
	cout << dp[N-1];
}
