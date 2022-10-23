//기준 점이 되는 h를 start로 두고 1부터 하나씩 증가시키면서 조건이 맞는지 확인
//정렬을 시킨후 small 이라는 start보다 작은값의 개수, big이라는 start보다 큰값의 개수를 조사해서 비교
//start 값이 citations 벡터의 마지막 값보다 크다면 return(종료 조건)

#include <string>
#include <vector>
#include<algorithm>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    sort(citations.begin(),citations.end());    //정렬
    int start=1;    //기준이되는 h값
    while(1){
        int small=0;    //h보다 작은 값 개수
        int big=0;  //h보다 큰값 개수
        for(int i=0;i<citations.size();i++){
            if(citations[i]<start){small++;}    //작은값 조사
            else if(citations[i]>start){big++;} //큰값 조사
            else{small++;big++;}    //같다면 둘다증가
        }
        
        if(small<=start&&big>=start){answer=max(answer,start);} //문제 조건 
        start++;    //start 증가
        if(start>citations[citations.size()-1]){return answer;} //start가 마지막 값보다 크면 종료
    }
}



다른 사람의 풀이를 보고 굳이 작은값, 큰값을 탐색하지않아도 충분히 해결할 수 있었다.
h값은 비교해야될 값을 의미하기도 하지만 개수를 의미하기도 하기 때문에 h값은 주어진 vector의 size() 안에 존재한다.
h 이상 인용되었던 것이 h편 이상이라고 했기때문에 index로 문제를 해결하면 효율적인 방법으로
작성할 수 있었다.
---------------참고코드-----------------
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    sort(citations.begin(), citations.end(), greater<int>());

    for (int i = 0; i < citations.size(); ++i) {
        if (citations[i] <= i ) {
            return i;
        }
    }

    return citations.size();
}
