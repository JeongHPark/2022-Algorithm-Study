#include <string>
#include <vector>
#include <algorithm>
using namespace std;
// 오름차순으로 정렬한 후 인접 전화번호만 비교 후 리턴
// 블로그를 참고해 풀이해봤습니다. https://codingwell.tistory.com/34 
bool solution(vector<string> phone_book) {
    sort(phone_book.begin(), phone_book.end());
    for (int i = 0; i < phone_book.size(); i++) 
        if(i != phone_book[i].size() - 1 && phone_book[i] == phone_book[i+1].substr(0, phone_book[i].size())) 
            return false;
    return true;
}
