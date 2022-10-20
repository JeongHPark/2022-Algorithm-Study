#include <string>
#include <vector>
#include<algorithm>
using namespace std;
// comand에 들어가있는 데이터 갯수 만큼 반복문을 돌려 i번째부터 j번째까지 
// array에서 자른후 오름차순 정렬해 k번째 숫자를 answer에 push하는 방식으로 했습니다.
vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for (int i = 0; i < commands.size(); i++) {
        vector <int> selection; // array에서 자른 숫자들이 들어가는 배열 
        for (int j = commands[i][0] - 1; j <= commands[i][1] - 1; j++)  selection.push_back(array[j]); //숫자 자르기
        sort(selection.begin(), selection.end()); // 오름차순 정렬
        answer.push_back(selection[commands[i][2] - 1]); // k번째 수 answer에 푸쉬
    }
    return answer;
}
