#include <string>
#include <vector>
using namespace std;
// DFS로 모든 경우의 수를 다 구함 (A ~ UUUUU)
// 블로그를 참조했습니다.
string words = "AEIOU";
int answer, cnt;

void dfs(string now, string target)
{
    if (now == target) answer = cnt; // 찾고자하는 타겟과 같을때 카운트값 answer에 넣어줌
    if (now.length() > 5) return; 
    cnt++;
    for (int i = 0; i < words.length(); i++)
        dfs(now + words[i], target);
}

int solution(string word) {
    dfs("", word);
    return answer;
}
