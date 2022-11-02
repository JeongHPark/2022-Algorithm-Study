//반대로 N에서 0으로 줄여나아가는 방법으로 해결
//짝수라면 2로 나눠주고 홀수이면 한칸 빼고 ans++

#include <iostream>
using namespace std;


int solution(int n)
{
    int ans = 0;
    while(n!=0){    //N이 0이 될때까지 반복
        if(n%2==0){n/=2;}   //짝수면 /=2
        else{n--;ans++;}    //홀수면 한칸 뺴고 정답 1 증가
    }
    return ans;
}
