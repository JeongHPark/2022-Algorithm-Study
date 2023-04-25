for문을 사용해서 주어진 돌을 모두 탐색하면서 확인하기는 stones 배열의 200000000이하의 자연수로 시간초과발생
stone의 수가 지나갈 수 있는 사람의 수를 나타내기 때문에 알맞은 stone의 값을 찾아야하기때문에 시간을 줄일 수 있는 
이분 탐색 사용

#include <string>
#include <vector>
#include<algorithm>
#include<iostream>

using namespace std;

bool success(vector<int>& stones,int k,int mid){
    int cnt=0;
    for(int i=0;i<stones.size();i++){
        if(stones[i]<mid)
            cnt++;
        else
            cnt=0;
        if(cnt>=k)
            return false;
    }
    return true;
}

int solution(vector<int> stones, int k) {
    int answer = 0;
    int end=0;
    int start=987654321;
    for(int i=0;i<stones.size();i++){
        start=min(start,stones[i]);
        end=max(end,stones[i]);
    }
    while(start<=end){
        int mid=(start+end)/2;
        if(success(stones,k,mid)){
            start=mid+1;
            answer=max(mid,answer);
        }
        else
            end=mid-1;
    }
    return answer;
}
