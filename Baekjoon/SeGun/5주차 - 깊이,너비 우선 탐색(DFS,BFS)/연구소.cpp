//먼저 3개의 벽을 세운다(DFS) 바이러스를 퍼트린다(BFS)
//퍼트린후 빈공간의 개수를 세어주고 최댓값을 유지한다.


#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

int N, M;
int map[11][11];
int submap[11][11];

void input() {  //입력문
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> map[i][j];
		}
	}
}
//4가지 방향을 나타내는 변수
int dix[4] = { 0,0,1,-1 };
int diy[4] = { 1,-1,0,0 };

void moveVirus() {  //바이러스의 움직임 표시함수
	bool visited[11][11] = { 0, };  //방문표시배열
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
      //for문으로 바이러스가 존재하는곳을 발견하고 이미 방문한 곳인지확인
			if (submap[i][j] == 2 && visited[i][j] == false) {
				visited[i][j] = true;
				queue<pair<int, int>> q;
				q.push({ i,j });
				while (q.size() != 0) { //BFS사용
					int x = q.front().first;
					int y = q.front().second;
					q.pop();
					submap[x][y] = 2;
					for (int i = 0; i < 4; i++) { //4가지 방향 탐색
						int dx = x + dix[i];
						int dy = y + diy[i];
						if (dx >= 0 && dx < N && dy >= 0 && dy < M) {
							if (submap[dx][dy] == 0 && visited[dx][dy] == false) {
								visited[dx][dy] = true;
								q.push({ dx,dy });
							}
						}
					}
				}
			}
		}
	}
}

void copy() { //전파되었던 바이러스를 다시 원래의 map 으로 초기화 하기위함
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			submap[i][j] = map[i][j];
		}
	}
}

int result;
void count0() { //빈공간의 개수를 세어주는 함수
	int sum = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (submap[i][j] == 0) { sum++; }
		}
	}
	result = max(sum, result);
}

void makeWall(int cnt, int x,int y) { //벽을 세워주는 함수(DFS 사용)
	if (cnt == 3) { //벽을 3개 세
		copy();
		moveVirus();	//바이러스 움직여주는 함수
		count0();
		return;
	}
	for (int i = x; i < N; i++) {
		for (int j = y; j < M; j++) {
			if (map[i][j] == 0) {
				map[i][j] =1;
				makeWall(cnt + 1, i, j + 1);
				map[i][j] = 0;
			}
		}
		y = 0;  //x값이 증가되면 y값을 0으로 설정
	}
}

void solution() {
	makeWall(0, 0,0);
	cout << result;
}

int main(void) {
	input();
	solution();
}
