//그리디로는 반례 발생해서 DFS사용

#include <string>
#include <vector>

using namespace std;

int result=987654321;   //최솟값을 구하기 위한 초기화

void Go(string name,string str,int idx,int cnt,int count){  //[입력받은 name][A로 초기화시켜놓은 string][현재의 인덱스][조이스틱입력횟수][탐색 총 횟수]
    if(cnt>=result){return;}  //결과값보다 cnt가 커졌다면 의미 없기에 리턴 
    if(name==str){result=min(result,cnt);return;} //원하는 문장을 만들었다면 result 최솟값 유지하고 리턴
    if(count>name.size()){return;}  //탐색 총 횟수가 name 크기보다 크면 안되기때문에 커지면 리턴

    if(idx==name.size()){idx=0;}  //순환구조때문에 설정
    if(idx==-1){idx=name.size()-1;} //순환구조때문에 설정
    
    if(str[idx]!=name[idx]){  //탐색하는 값이 만들어야 하는 값과 다르다면
        int left=name[idx]-'A'; //A의 차이와
        int right='Z'-name[idx]+1;  //Z의 차이를 비교
        str[idx]=name[idx]; //str에 name 값 저장
        cnt+=min(left,right); //작은 값 저장
    }
    string tmp=str; //뒤로가는 함수에 넣어주기 위해 tmp 사용
    Go(name,str,idx+1,cnt+1,count+1); //앞으로 한칸이동
    Go(name,tmp,idx-1,cnt+1,count+1); //뒤로 한칸이동
}

int solution(string name) {
    string str;
    for(int i=0;i<name.size();i++){str.push_back('A');} //str 을 A로 초기화
    Go(name,str,0,0,0);
    return result==0?0:result-1;  //결과값이 1 증가되어서 저장되기때문에 삼항연산자 사용
}
