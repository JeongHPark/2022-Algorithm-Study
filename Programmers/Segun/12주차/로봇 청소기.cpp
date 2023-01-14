처음 문제를 보자마자 DFS로 해결해봐야겠다고 생각하고 접근
해결하는 중에 굳이 이동하기전의 좌표를 스택에 저장하는 DFS 방식이 필요없다고 생각함
그래서 DFS로 좌표를 기억하면서 탐색하기보다는 로봇의 움직임을 따라가면되기에 while문을 사용
청소했던 지점을 기억하기위해 visited 배열 사용, 뒤로 움직였을때에 방향유지확인하지 못해 시간소비

#include<iostream>
#include<algorithm>

using namespace std;

int N, M;
int rx, ry, rd;
bool map[55][55];
int dix[4] = { -1,0,1,0 };
int diy[4] = { 0,1,0,-1 };
int answer = 1;
bool visited[55][55];

void input() {
	cin >> N >> M;
	cin >> rx >> ry >> rd;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> map[i][j];
			visited[i][j] = map[i][j];
		}
	}
}

void goBack() {
	int rotation = 0;
	while (rotation != 4) {
		rd = (rd + 3) % 4;
		int dx = rx + dix[rd];
		int dy = ry + diy[rd];
		if (map[dx][dy] == 0 && visited[dx][dy] == 0) {
			visited[dx][dy] = 1;
			answer++;
			rx = dx;
			ry = dy;
			rotation = 0;
		}
		else {
			rotation++;
		}
	}
}

int main(void) {
	input();
	visited[rx][ry] = 1;
	goBack();
	while (map[rx + dix[(rd + 2) % 4]][ry + diy[(rd + 2) % 4]] == 0) {
		rx = rx + dix[(rd + 2) % 4];
		ry = ry + diy[(rd + 2) % 4];
		goBack();
	}
	cout << answer;

}
