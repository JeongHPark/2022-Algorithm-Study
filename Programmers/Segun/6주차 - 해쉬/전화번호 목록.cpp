//set을 사용해서 모든 phone_book 값을 set 에 저장해주고 그 phone_book 값을 잘라서 비교
//ex) 12345 이면 1,12,123,1234,12345 가 set에 존재하는지를 확인
//문자열의 길이가 길이순으로 정렬되어있지 않았을때를 생각하지 못해서 반례발생
//+추가 스터디원들이 해결한 풀이를 보고 정렬을 사용해서도 해결할 수 있다는 것을 알았다.
//처음에 정렬을 사용했을때에는 문자열을 int형으로 변경하고 정렬하는 방법만 생각했지만 풀이를 보고 문자열 그대로 정렬하게되면
//문제를 해결할 수 있도록 문자열정렬이 된다는것을 알았다.

#include <string>
#include <vector>
#include<unordered_set>
#include<iostream>
#include<algorithm>

using namespace std;

bool cmp(string a,string b){ return a.size()<b.size();} //정렬 기준

bool solution(vector<string> phone_book) {
    unordered_set<string> us;   //set 선언
    sort(phone_book.begin(),phone_book.end());  //크기순으로 정렬
    for(int i=0;i<phone_book.size();i++){
        for(int j=1;j<=phone_book[i].size();j++){
            //문자열을 길이가 1 부터 총 문자열까지 자르기 위한 for문
            //substr을 사용해서 문자열 자름, 자른 값이 존재한다면 false 리턴
            if(us.find(phone_book[i].substr(0,j))!=us.end()){  return false;  }
        }
         us.insert(phone_book[i]);  //set에 값 넣어주기
    }
    return true;    //없다면 true 리턴
}

--------------정렬을 사용한 풀이------------------
#include <string>
#include <vector>
#include<iostream>
#include<algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
    sort(phone_book.begin(),phone_book.end());
    for(int i=1;i<phone_book.size();i++){
        if(phone_book[i-1]==phone_book[i].substr(0,phone_book[i-1].size())){return false;}
    }
    return true;
}
