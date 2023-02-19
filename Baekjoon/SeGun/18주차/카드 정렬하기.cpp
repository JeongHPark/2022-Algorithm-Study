카드를 값이 낮은 순으로 합쳐서 최적해를 구할 수 있음
카드를 합쳐서 넣어준 값도 정렬이 되어야하기때문에 우선순위 큐 사용

#include<iostream>
#include<queue>

using namespace std;

int n;
int result;
int main(void) {
	priority_queue<int,vector<int>,greater<>> pq;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		pq.push(x);
	}
	while (pq.size() != 1) {
		int x = pq.top();
		pq.pop();
		int y = pq.top();
		pq.pop();
		result += (x + y);
		pq.push(x + y);
	}
	cout << result;
	
}
