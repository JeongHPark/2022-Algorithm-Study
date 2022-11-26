//heap구조를 사용하는 priority_queue 를 사용해서 문제 해결
//우선순위큐를 오름차순으로 정렬되게 기준을 설정해주고 앞에 두 값을 pop하고 그 두값을 섞은 값을 다시 push해줌

#include <string>
#include <vector>
#include<queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int,vector<int>,greater<int>> pq(scoville.begin(),scoville.end());

    while(pq.top()<K){
        if(pq.size()==1){return -1;}
        int x=pq.top();pq.pop();
        int y=pq.top();pq.pop();
        pq.push(x+y*2);
        answer++;
    }
    return answer;
}
