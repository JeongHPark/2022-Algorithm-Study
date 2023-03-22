1~n 까지 탐색을 하면서 색칠해야되는 구역이라면 m길이만큼 색을 칠하고
칠한 부분 다음부터로 이어서 탐색한다
주어진 section을 for 문으로 탐색하면서 탐색하는 section이 이전에 m 만큼 칠했던 부분에 속하는지 속하지 않는지에따라
해결하면 더 효율적으로 작성할 수 있다.

#include <string>
#include <vector>
#include<unordered_map>

using namespace std;

int solution(int n, int m, vector<int> section) {
    int answer = 0;
    int result=0;
    unordered_map<int,bool> um;
    for(auto x:section)
        um[x]=true;
    for(int i=1;i<=n;i++){
        if(um[i]==true){
            result++;
            for(int j=0;j<m;j++){
                if(um[i]==true){
                    answer++;
                    if(answer==section.size())
                        return result;
                }
                i++;
            }
            i--;
        }
    }
    return answer;
}

-------------------------------------------------------------------
  
  
#include <string>
#include <vector>

using namespace std;

int solution(int n, int m, vector<int> section) {
    int answer = 1;
    int tmp=section[0];
    for(auto x:section){
        if(x<tmp+m)
            continue;
        tmp=x;
        answer++;
    }
    return answer;
}
