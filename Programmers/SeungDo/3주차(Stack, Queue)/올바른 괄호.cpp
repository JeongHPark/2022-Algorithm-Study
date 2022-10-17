#include<string>
#include<stack>
using namespace std;
// 문자열s의 길이만큼 for문을 돌려 스택이 비었거나 괄호완성이 안되면 push 괄호완성이 되면 top값 pop하는 방식으로 풀이해봤습니다.
bool solution(string s)
{
    stack <char> prime; //char형 스택 선언
    for (int i = 0; i < s.size(); i++) {
        if (prime.empty() == 1 || prime.top() != '(' || s[i] != ')') prime.push(s[i]); // 스택이 비었거나 탑 값이 '('가 아니거나 s[i]값이 ')'가 아니면 s[i]값 푸쉬
        else prime.pop(); // 스택의 탑값이 '(' 이고 푸쉬할 값이 ')'일때 top값 팝
    }
    if(prime.empty() == 1) return true; // 스택이 비었다면 true리턴
    if(prime.empty() == 0) return false; // 스택에 값이 남아있다면 false리턴
}
