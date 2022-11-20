//현재 탐색하고 있는 상자의 인덱스를 i라고 할때 그 상자의 크기와 0 ~ i-1 번째 상자의 크기를 비교해서( 비교한 값을 j) i번째 상자가 더 크다면 넣을 수 있기에 
//비교했던 상자(j)의 최대 넣을 수 있는 상자 개수 dp[j]+1 해서 dp[i]에 저장시켜주고 저장할때 최댓값 유지를 시켜준다. 

#include <iostream>
#include<algorithm>

using namespace std;

int main() {
  int N;
  int box[1111];
  int dp[1111];  //dp[x]=y x번째 상자를 선택했을때 넣을 수 있는 상자 최대 개수 y 개
  int result=0;
  
  cin>>N;
  for(int i=0;i<N;i++){
    cin>>box[i];
  }
  dp[0]=1;  //첫번째 상자는 최대 1 가능
  for(int i=1;i<N;i++){
    dp[i]=1;  //dp는 0으로 초기화 되어있기때문에 아무것도 넣지 못하는 상자는 0으로 설정되어있기때문에 반례 발생해서 dp[i]=1 저장
    for(int j=0;j<i;j++){
      if(box[j]<box[i]){
        dp[i]=max(dp[i],dp[j]+1); //최댓값 유지 하면서 dp[j]+1  저장
      }
    }
  }
  for(int i=0;i<N;i++){
    result=max(result,dp[i]); //모든 dp 값중 가장 큰값 출력
  }
  cout<<result;
}
