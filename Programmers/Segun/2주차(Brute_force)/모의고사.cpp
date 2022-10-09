#include <string>
#include <vector>
#include<algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int arr1[5]={1,2,3,4,5};    //1번 방식
    int arr2[8]={2,1,2,3,2,4,2,5};  //2번 방식
    int arr3[10]={3,3,1,1,2,2,4,4,5,5}; //3번 방식
    
    vector<pair<int,int>> vec;  //사람당 맞힌 개수를 파악하기위한 vector
    vec.push_back({0,1});   //초기화
    vec.push_back({0,2});   //초기화
    vec.push_back({0,3});   //초기화
    
    for(int i=0;i<answers.size();i++){
        if(answers[i]==arr1[i%5]){vec[0].first++;}  //%를 사용해서 찍는 방식 범위내에 적용
        if(answers[i]==arr2[i%8]){vec[1].first++;}  //%를 사용해서 찍는 방식 범위내에 적용
        if(answers[i]==arr3[i%10]){vec[2].first++;} //%를 사용해서 찍는 방식 범위내에 적용
    }
    
    int mx=max(vec[0].first,max(vec[1].first,vec[2].first));
    if(vec[0].first==mx){answer.push_back(vec[0].second);}     //mx값과 맞은 개수가 같다면  push
    if(vec[1].first==mx){answer.push_back(vec[1].second);}    
    if(vec[2].first==mx){answer.push_back(vec[2].second);}    
    return answer;
}
