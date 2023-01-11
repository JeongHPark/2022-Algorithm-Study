#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool visited[100001];
vector <string> answer;
// 알파벳이 순서가 빠른 기준으로 정렬을 한 후 DFS를 이용해 모든 경로를 구한다.
// 블로그를 참조해 풀이했습니다. https://school.programmers.co.kr/learn/courses/30/lessons/43164

 // 한번 경로를 찾았으면 더 이상 찾지 않기 위해 함수를 bool로 선언
bool dfs(int l, string start, vector<vector<string>> tickets) {
    //모든 경로를 탐색했을 경우
    if (l == tickets.size()) {
        return true;
    }

    for (int i = 0; i < tickets.size(); i++) {
        if (start == tickets[i][0] && !visited[i]) { //start가 갈 수 있는 곳 중 방문하지 않은 경로
            visited[i] = 1;
            answer.push_back(tickets[i][1]); // 경로 추가
            bool check = dfs(l + 1, tickets[i][1], tickets);
            if (check) return true; // 한번 경로를 찾았으면 더 이상 찾지 않음
            visited[i] = 0;
            answer.pop_back(); // 경로가 끊겨 있는 경우에 백트래킹
        }
    }

    return false;
}

vector<string> solution(vector<vector<string>> tickets) {
    sort(tickets.begin(), tickets.end()); // 알파벳 순서가 앞서는 경로로 정렬     

    //인천부터 시작
    answer.push_back("ICN");
    dfs(0, "ICN", tickets);

    return answer;
}
