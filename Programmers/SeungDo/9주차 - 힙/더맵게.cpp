// 효율성테스트 실패
#include <string>
#include <vector>
#include<algorithm>
using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0 , x= 0;
    
    while (1) {
        sort(scoville.begin(), scoville.end());
        if (scoville[0] < K) {
            scoville[1] = scoville[0] + scoville [1] * 2;
            scoville.erase(scoville.begin());
            answer++;
        }
        else return answer;
        if(scoville.size() == 1 && scoville[0] < K) return -1; // K 이상을 만들지 못할 때
    }
}

// 블로그 참고하여 풀이 https://silver-g-0114.tistory.com/70
// 우선 순위 큐 사용
#include <vector>
#include <queue>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    int first, second;
    
    // 오름차순 우선순위 큐
    priority_queue<int, vector<int>, greater<int>> pq;
    for(int i=0; i<scoville.size(); i++){
        pq.push(scoville[i]);
    }
    
    while(pq.top()< K && pq.size()>1){
        answer++;
        first = pq.top(); // 가장낮츤 스코빌지수
        pq.pop();
        second = pq.top(); // 두 번째로 낮은 스코빌 지수
        pq.pop();
        pq.push(first+second*2); // 합치기
    }
    
    if(pq.top()<K) return -1;
    else return answer;
}
