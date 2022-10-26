#include<iostream>
#include<queue>

using namespace std;

int arr[101][101] = { 0, };
int n, m;
bool visited[101] ;

void solution() {
	int answer = 0;
	queue <int> q;
	q.push(1); // 1 푸쉬
	visited[1] = true; // 비지티드 어레이에 1 True
	while (!q.empty()) { // 큐가 빌 때까지 반복
		int x = q.front();  // 프론트 값 변수 x에 넣음
		q.pop(); // 팝
		for (int i = 1; i <= n; i++)
		{
			if (visited[i] == false && arr[x][i] == 1) { // 연결된 정점중에 visited가 false인 정점 푸쉬하고 answer ++
				answer++;
				q.push(i);
				visited[i] = true;
			}
		}
	}
	cout << answer << "\n";
}
int main() {
	int num1,num2;
	cin >> n >> m;

	for (int i = 0; i < m; i++) {
		cin >> num1 >> num2;
		arr[num1][num2] = arr[num2][num1] = 1;
	}
	solution();
}
