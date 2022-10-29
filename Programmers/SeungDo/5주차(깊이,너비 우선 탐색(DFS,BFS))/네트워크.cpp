#include <string>
#include <vector>
#include<queue>
using namespace std;
// for문을 컴퓨터 갯수만큼 돌리면서 BFS를 이용하여 연결된 네트워크의 갯수를 구했습니다.
bool visited[200] = { 0, };
int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    queue<int> q;
    for (int i= 0; i < computers.size(); i++) {
        if (visited[i] == false) { // i 번째 컴퓨터를 방문하지 않았다면
            q.push(i); // i를 큐에 넣고
            visited[i] = true; // 방문 완료표시
            while (!q.empty()) { // 큐가 빌 때까지 반복
                int popValue = q.front(); // 프론트값을 변수에 대입
                q.pop(); // 팝
                for (int j = 0; j < computers.size(); j++) { 
                    if (visited[j] == false && computers[popValue][j] == 1) { // 이어진 컴퓨터 탐색
                        q.push(j); 
                        visited[j] = true;
                    }
                }
            }
            answer++; // 네트워크갯수 ++
        }
    }
    return answer;
}
