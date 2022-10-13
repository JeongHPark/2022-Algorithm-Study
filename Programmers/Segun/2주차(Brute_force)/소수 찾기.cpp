//흩어진 종이조각을 '조합'으로 맞춰주고 그 만들어진수가 소수인지를 확인한 뒤에 result++ 해준다.

#include <string>
#include <vector>

using namespace std;

bool visited[11];   //방문 여부 변수
char arr[11];   //뽑은 종이 조각을 저장
int result; //결과값
bool chk[11111111]; //이미 확인했던 값인지 확인

bool decimal(int x) {   //소수를 판별해주는 함수
    if (chk[x] == false) { chk[x] = true; } //처음들어오는 값이라면 확인처리
    else { return false; }  //이미 들어왔던 수라면 false 리턴
    for (int i = 2; i <= x / 2; i++) {  //x가 1과 자기자신외에 다른 수로 나누어지는지 확인
        if (x % i == 0) { return false; }   //나누어진다면 소수가 아님
    }
    
    return true;    //통과했다면 소수
}

//흩어진 종이조각을 맞춰주는 함수
void DFS(int cnt, string num) {
    if (cnt > 0 && cnt <= num.size()) { //수가 1개이상 주어진 수의 길이 이하라면 소수 판별해보기
        string str;
        for (int i = 0; i < cnt; i++) { str.push_back(arr[i]); }    
        //string을 바로 접근하면 오류발생해서 char 배열 사용
        if (decimal(stoi(str)) == true) { result++; } } //소수 확인
    for (int i = 0; i < num.size(); i++) {  //주어진 문자열의 길이만큼 탐색
        if (visited[i] == false) {  //이미 탐색했던곳인지 확인
            visited[i] = true;  //아니라면 방문 표시
            arr[cnt] = num[i];  //고른 종이 조각을 arr에 저장
            DFS(cnt + 1,num);   //다음 종이 조각 뽑기
            visited[i] = false; //종이 조각 뽑고 확인까지 끝낫다면 다시 방문표시를 없애줌
        }
    }
}

int solution(string numbers) {
    chk[0] = true; chk[1] = true;   //0,1은 소수가 아님
    DFS(0, numbers);
    return result;
}
