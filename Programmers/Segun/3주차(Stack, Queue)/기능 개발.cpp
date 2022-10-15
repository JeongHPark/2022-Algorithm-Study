몇일이 지났는지를 저장하는 변수를 하나 지정해주고 더한값이 100이상인지 확인하면서 answer에 push 

#include <string>
#include <vector>
#include<queue>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue<int> q;   //주어진 배열을 큐에 저장하기위함
    queue<int> s;   //주어진 속도를 큐에 저장하기위함
    for(int i=0;i<progresses.size();i++){q.push(progresses[i]);s.push(speeds[i]);}
    int cnt=1;  //몇일이 지났는지를 알려주는 변수
    while(q.size()!=0){ //큐가 비었다면 종료
        int sum=0;  //하루에 몇개의 작업이 끝낫는지를 나타냄
        while(q.front()+cnt*s.front()>=100){    //작업이 끝나지 않은 값이 나올때까지 반복
            q.pop();s.pop();sum++;  //각각의 큐 pop
            if (q.size() == 0) { break; }   //큐가 비었다면 break
        }
        if(sum>0)answer.push_back(sum); //끝난 작업이 1개 이상일때만 result에 push
        cnt++;
    }
    return answer;
}
