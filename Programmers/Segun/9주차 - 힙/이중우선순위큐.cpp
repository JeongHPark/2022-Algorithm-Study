//최댓값을 알기위한 big 우선순위큐와 최솟값을 알기위한 small 우선순위큐는 설정
//주어진 push 명령어와 delete 명령어의 개수를 파악해서 큐가 비었는지를 확인
//push와 delete의 개수가 같아진다면 우선순위큐 초기화

#include <string>
#include <vector>
#include<queue>
#include<iostream>
#include<algorithm>

using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    int cnt=0;
    priority_queue<int,vector<int>,less<int>> big;
    priority_queue<int,vector<int>,greater<int>> small;

    for(int i=0;i<operations.size();i++){
        if(operations[i][0]=='I'){
            cnt++;
            big.push(stoi(operations[i].substr(2)));
            small.push(stoi(operations[i].substr(2)));
        }
        else{
            cnt=(cnt-1<0)?0:cnt-1;
            if(operations[i][2]=='1'){
                if(big.size()!=0)
                big.pop();
            }
            else{
                if(small.size()!=0)
                small.pop();
            }
            if(cnt==0){
                //큐 초기화
                while(big.size()!=0){big.pop();}
                while(small.size()!=0){small.pop();}
            }
        }
    }
    if(cnt==0){ //delete가 더 많이 주어졌을때
        answer.push_back(0);
        answer.push_back(0);
        return answer;
    }
    answer.push_back(big.top());
    answer.push_back(small.top());
    return answer;
}
