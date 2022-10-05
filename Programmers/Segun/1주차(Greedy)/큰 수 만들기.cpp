//(0부터 k+1까지)인덱스 0 부터 k+1 까지 중에서 가장 큰수와 그 값의 인덱스를 저장한다
//가장 큰수를 찾은 그 인덱스 전까지 범위를 k에서 빼준다
// k의 값과 탐색지점을 기억해주고 다시 반복한다(max값의 인덱스 부터 k+1까지) 

#include <string>
#include <vector>
#include<algorithm>

using namespace std;

string solution(string number, int k) {
    string answer = "";
    int i=0;  //0부터 시작
    int size=number.size()-k; //찾아야하는 문자열의 크기
  
    while(1){
        char mx='0';   //문자 비교이기때문에 char 선언
        int idx=i;  //idx 초기화
      
        for(int j=i;j<=i+k;j++){  //k의 범위만큼 탐색
            if(mx<number[j]){mx=number[j];idx=j;} //max값과 그 값의 인덱스 저장
        }
        answer+=number[idx];  //answer에 max값 추가
        if(answer.size()==size){return answer;} //answer가 다 채워졌다면 return
        
        k-=(idx-i); //k 재설정
        i=idx+1;  //i 재설정
    }
}
