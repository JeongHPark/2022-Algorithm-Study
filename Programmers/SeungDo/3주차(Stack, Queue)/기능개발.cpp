#include <vector>
// 큐에 있는 모든 작업 진도에 작업 속도를 더한 후 반복문을 이용해 맨 앞에 있는 작업이 100이 넘었는지 확인 후 넘었다면 팝 하는 방식으로 풀이 해봤습니다.
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    /* 
       변수 x를 둔 이유는 for문의 조건을 progresses.size()로 뒀을 때 팝이 되면 
       큐의 크기가 for문을 돌릴 때마다 -1이 되기 때문에 for문이 작업을 다 비교하지 못하고 끝나버림
       그래서 큐의 처음 크기를 나타내는 변수 x를 두어 끝난 작업을 배포한 뒤에 
       count만큼 x값을 빼는 방식으로 큐 안에 있는 모든 작업을 다 비교할수 있게 함   
    */   
    int x = progresses.size(); // 작업 진도가 들어있는 큐의 크기 저장 
    while (1) {
        int count = 0; // 몇 개가 배포됐는지 count
        for (int i = 0; i < x; i++) progresses[i] += speeds[i]; //모든 작업 진도에 작업 속도를 더함
        for (int i = 0; i < x; i++) {
            if (progresses.front() >= 100) { // 맨앞에 있는 작업의 진도가 100을 넘었다면 
                count++; // 배포할 작업 수 ++
                progresses.erase(progresses.begin()); // 맨앞 작업 진도 팝
                speeds.erase(speeds.begin()); // 맨앞 작업 속도 팝
            }
            else break;
        }// 맨앞에 있는 작업의 진도가 100을 넘지않았을때는 바로 break  
        if (count > 0) { // 배포할 작업 수가 1개 이상이라면 
            answer.push_back(count); // answer에 count값 푸쉬
            x -= count; // 배포한 수 만큼 전체크기를 줄임
        }
        if (progresses.empty() == 1) return answer; // 큐가 비었다면 answer 리턴
    }
}
