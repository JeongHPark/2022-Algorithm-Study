//스택의 개념을 사용해서 전에 들어왔던 값이랑 비교해서 다른값이 들어왔을때만 vector에 넣어주게 작성

#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer; //리턴해주는 결과값
    for(int i=0;i<arr.size();i++){  //주어진 배열 탐색
        if(arr[i]!=arr[i-1]||i==0){answer.push_back(arr[i]);}   //다른값이 들어왔으면 넣어주기
    }
    
    return answer;
}
