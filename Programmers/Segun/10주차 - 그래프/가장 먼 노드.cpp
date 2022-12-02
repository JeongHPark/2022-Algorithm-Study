#include <string>
#include <vector>
#include<iostream>
#include<queue>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
	int answer = 0;
	int max = 0;  //가장 멀리 떨어진 노드의 거리를 저장
	vector<int> dis(n + 1);    //거리를 나타냄
	vector<bool> visited(n + 1);
	vector<vector<bool>> map(n + 1, vector<bool>(n + 1));   //매핑

	//매핑
	for (int i = 0; i < edge.size(); i++) {
		map[edge[i][0]][edge[i][1]] = true;
		map[edge[i][1]][edge[i][0]] = true;
	}

	//BFS사용
	queue<pair<int, int>> q;    //<현재좌표, 1에서부터 거리>
	q.push({ 1,0 });
	visited[1] = true;
	while (q.size() != 0) {
		int cur = q.front().first;
		int cnt = q.front().second;
		q.pop();
		for (int i = 1; i <= n; i++) {
			if (map[cur][i] == 1 && visited[i] == false) {
				dis[i] = cnt + 1;
				max = cnt + 1;
				visited[i] = true;
				q.push({ i,cnt + 1 });
			}
		}
	}

	//가장 멀리 떨어진 노드 개수 
	for (int i = 1; i <= n; i++) {
		if (dis[i] == max) { answer++; }
	}
	return answer;
}
