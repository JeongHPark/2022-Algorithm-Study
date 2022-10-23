//새로운 vec 하나를 만들어주고 주어진 범위에 맞게 insert를 사용해서 범위만큼 저장해주고 정렬한다.
//정렬한 후에 k 번째 수를 answer 에 저장시켜준다.

#include <string>
#include <vector>
#include<algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer; //return 벡터
    for(int i=0;i<commands.size();i++){
        vector<int> vec;    //주어진 범위만큼 옮겨놓은 벡터
       vec.insert(vec.begin(),array.begin()+commands[i][0]-1,array.begin()+commands[i][1]); //insert로 옮기기
        sort(vec.begin(),vec.end());    //정렬 
        answer.push_back(vec[commands[i][2]-1]);    //k번째 값 저장
     }
   return answer;
}
