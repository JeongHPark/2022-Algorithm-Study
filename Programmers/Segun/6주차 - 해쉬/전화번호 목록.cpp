//set을 사용해서 모든 phone_book 값을 set 에 저장해주고 그 phone_book 값을 잘라서 비교
//ex) 12345 이면 1,12,123,1234,12345 가 set에 존재하는지를 확인
//문자열의 길이가 길이순으로 정렬되어있지 않았을때를 생각하지 못해서 반례발생

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
