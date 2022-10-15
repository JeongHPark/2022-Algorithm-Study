스택의 개념을 사용해서 top에 있는 값과 넣어줄 값이 같은지를 비교해서 같지 않다면 push 해준다

#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer; //return 해줄 vector
    for(int i=0;i<arr.size();i++){  //배열 탐색
        if(arr[i]!=arr[i-1]||i==0){answer.push_back(arr[i]);} //top과 비교
    }
    return answer;
}
