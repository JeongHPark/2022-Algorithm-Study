BFS로 외부공기가 접근할 수 있는 곳까지 체크해줌
-> 외부공기와 내부공기가 나눠짐
외부공기와 두면 이상이 마주닿은 곳은 제거해주고 
다시 그 제거된 부분까지 합쳐서 외부공기가 접근할 수 있는곳을 체크 해주면서 반복


#include<iostream>
#include<vector>
#include<string>
#include<queue>

using namespace std;
//외부공기 2, 치즈 1, 내부공간 0

int N, M;
int map[111][111];
int sx, sy;	//외부공기가 내부로 들어왔는지 확인하기위한 좌표
int dix[4] = { 0,0,1,-1 };
int diy[4] = { 1,-1,0,0 };
int result;

void input() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> map[i][j];
		}
	}
}

void outAir() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (map[i][j] == 2) {
				map[i][j] = 0;
			}
		}
	}
	queue<pair<int, int>> q;
	q.push({ 0,0 });
	map[0][0] = 2;
	while (q.size() != 0) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		for (int k = 0; k < 4; k++) {
			int dx = x + dix[k];
			int dy = y + diy[k];
			if (dx >= 0 && dx < N && dy >= 0 && dy < M) {
				if (map[dx][dy] == 0) {
					map[dx][dy] = 2;
					q.push({ dx,dy });
				}
			}
		}
	}
}

int main(void) {
	input();
	while (1) {
		outAir();
		bool chk = false;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (map[i][j] == 1) {
					chk = true;
					int cnt = 0;
					for (int k = 0; k < 4; k++) {
						int dx = i + dix[k];
						int dy = j + diy[k];
						if (dx >= 0 && dx < N && dy >= 0 && dy < M) {
							if (map[dx][dy] == 2)
								cnt++;
						}
					}
					if (cnt >= 2)
						map[i][j] = 0;
				}
			}
		}
		if (chk == false) {
			cout << result; return 0;
		}
		result++;
	}
}

