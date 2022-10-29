#include <string>
#include <vector>
#include<queue>
using namespace std;
bool visited[200] = { 0, };

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    queue<int> q;
    for (int i= 0; i < computers.size(); i++) {
        if (visited[i] == false) {
            q.push(i);
            visited[i] = true;
            while (!q.empty()) {
                int popValue = q.front();
                q.pop();
                for (int j = 0; j < computers.size(); j++) {
                    if (visited[j] == false && computers[popValue][j] == 1) {
                        q.push(j);
                        visited[j] = true;
                    }
                }
            }
            answer++;
        }
    }
    return answer;
}
