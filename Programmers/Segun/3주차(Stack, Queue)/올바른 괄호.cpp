스택을 사용해서 스택에 쌓여있있는 '(' 가 ')'를 만났다면 pop, 아니라면 push 해줘서 for문이 끝났을때에 vec 사이즈를 보고 리턴함

#include<string>
#include <iostream>
#include<vector>

using namespace std;

bool solution(string s)
{
    vector<char> vec; //스택사용
    for(int i=0;i<s.size();i++){
        if(vec.size()!=0&&vec[vec.size()-1]=='('&&s[i]==')'){vec.pop_back();} //스택의 top이 '('이고 현재 탐색값이 ')' 이라면 pop
        else{vec.push_back(s[i]);}  //vec에 아무것도 없고 위에 조건에 해당되지않는다면 push
    }
    return (vec.size()==0)?true:false;
}
