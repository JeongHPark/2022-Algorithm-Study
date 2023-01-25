#include <string>
#include <vector>

using namespace std;
// 처음에 우선순위가 가장 높은 값을 구한 뒤 벡터의 처음값이 max와 같고 location이 0일때 리턴
int solution(vector<int> priorities, int location) {
    int answer = 0 ,max = 0;
    for(int i = 0; i<priorities.size();i++) if(max < priorities[i]) max= priorities[i];
    while(1){   
        if(priorities[0] == max) {
            if(location == 0) return answer + 1; // 사용자가 원하는 작업일때 리턴
            priorities.erase(priorities.begin()); // 팝
            max =0;
            for(int i = 0; i<priorities.size();i++) if(max < priorities[i]) max= priorities[i];
            answer++; // 작업 수 ++
        }
        else{
            priorities.push_back(priorities[0]); // 첫 번째 값을 맨뒤에 푸쉬
            priorities.erase(priorities.begin()); //첫 번째 값 팝 
        }
        location--; 
        if(location == -1)location = priorities.size() - 1;
    }
}
