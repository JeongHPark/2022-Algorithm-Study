//A서부터 UUUUU 까지 모든 나올수있는 경우의 수를 확인하고 주어진 word와 같은 문장이 나왔을때까지 진행

#include <string>
#include <vector>
#include<iostream>

using namespace std;

char alpha[5]={'A','E','I','O','U'};
string str="XXXXX";
int answer = 0;
bool chk;
void DFS(int cnt,string word){
    if(cnt>5||chk==true){return;}
    if(str.substr(0,cnt)==word){chk=true;return;}
    answer++;
    for(int i=0;i<5;i++){
        str[cnt]=alpha[i];
        DFS(cnt+1,word);
    }
}

int solution(string word) {
    DFS(0,word);
    return answer;
}
