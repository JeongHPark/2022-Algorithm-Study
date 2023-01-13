11주차때 해결하지 못했던 문제
받아온 loutes 배열의 모든 값의 진입 지점부터 진출 지점을 나타낼수있는
chk 배열을 만들어줌 ex) [1,5],[4,5] -> 11122
진입 지점을 기준으로 loutes배열을 오름차순 정렬 시키고 loutes배열을 탐색하면서
현재 loutes의 어느 idx에 어느지점에서 가장 많이 카메라를 만나게하는지 max값을 찾아가면서 해결
시간초과 발생, 반례 발생
굳이 chk 배열을 만들어줄 필요없이 x라는 변수에 첫번째 차의 진출 지점을 넣어주고 나머지 값들과 비교하면서 x를 갱신하면서 해결
반례 발생
int solution(vector<vector<int>> routes) {
    int answer = 1;
    int x=routes[0][1];
    sort(routes.begin(),routes.end());
    for(int i=1;i<routes.size();i++){
        if(x<routes[i][0]){ //이조건으로 최적해를 구할 수 없다
            answer++;
            x=routes[i][1];
        }
    }
    return answer;
}
https://mungto.tistory.com/49 (블로그 출처)
두가지 경우의수 확인 
다음에 들어올 차가 지금 차보다 먼저나갈때
다음에 들어올차가 지금차 나가고 나갈때

#include <string>
#include <vector>
#include<iostream>
#include<algorithm>

using namespace std;

int solution(vector<vector<int>> routes) {
    int answer = 1;
    sort(routes.begin(),routes.end());
    int x=routes[0][1];
    for(int i=1;i<routes.size();i++){
      //이번차가 나가고 다음차가 들어올 경우
        if(x<routes[i][0]){
            answer++;
            x=routes[i][1];
        }
      //이번차보다 다음차가 먼저 나가는 경우
        else if(x>=routes[i][1]){
            x=routes[i][1];
        }
    }
    return answer;
}
