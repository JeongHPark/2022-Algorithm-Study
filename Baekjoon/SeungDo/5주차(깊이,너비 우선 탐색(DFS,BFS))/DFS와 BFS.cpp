#include<iostream>
#include<queue>
#include<vector>
// dfs 재귀함수가 잘 안풀려서 https://scarlettb.tistory.com/76 블로그를 참고 해 풀이했습니다.
using namespace std;

int map[1001][1001] = { 0, }, n, m , v;
bool visited[1001] = { 0, };

void dfs( int v ) { // dfs
	cout << v << " "; // 방문한 정점 출력
	visited[v] = 1; // 방문한 정점 방문 완료 표시
	for (int i = 1; i <= n; i++) {
		if (visited[i] == 0 && map[v][i] == 1) { // 방문하지 않았고 방금 방문한 정점과 이어져 있을 때
			dfs(i); // 재귀함수를 이용해 방문 정점 구함
		}
	}
}

void bfs(int v) {  // bfs
	queue <int> q; 
	for (int i = 1; i <= n; i++) visited[i] = 0; // dfs에서 방문한 정점 초기화
	q.push(v); // 시작 정점 queue에 푸쉬
	cout << v << " "; // 출력
	visited[v] = 1; // 방문 완료
	while (!q.empty()) { 
		int popValue = q.front(); // 팝하는 값 변수에 입력
		q.pop(); // 팝
		for (int i = 1; i <= n; i++) {
			if (visited[i] == 0 && map[popValue][i] == 1) { // 방문하지 않았고 방금 방문한 정점과 이어져 있을 때
				q.push(i); // 푸쉬
				cout << i << " "; // 방문한 정점 출력
				visited[i] = 1; // 방문 완료 표시
			}
		}
	}
	cout << "\n";
}
int main() {
	int  a, b;
	cin >> n >> m >> v;
	for (int i = 1; i <= m; i++) {
		cin >> a >> b;
		map[a][b] = map[b][a] = 1;
	}

	dfs(v);
	cout << "\n";
	bfs(v);
}
