//N의 범위가 pq에 1을 N번 넣어주고 해결하려면 시간초과발생

#include<iostream>
#include<queue>
#include<string>
#include<vector>

using namespace std;

int main(void) {
	int N, K;
	int result = 0;
	cin >> N >> K;

	priority_queue<int, vector<int>, greater<int>> pq;
	//N의 최대값을 넘지않는 2의 배수
	int solve = 8388608;

	while (N!=0) {
		if (N / solve == 1) {
			N -= solve;
			pq.push(solve);
			solve /= 2;
		}
		else 
			solve /= 2;
	}

	while (pq.size() > K) {
		int x = pq.top();
		pq.pop();
		int y = pq.top();
		pq.pop();
		if (x == y) 
			pq.push(x + y);
		else {
			pq.push(y);
			result += x;
			pq.push(x * 2);
		}
	}
	cout << result;
}
