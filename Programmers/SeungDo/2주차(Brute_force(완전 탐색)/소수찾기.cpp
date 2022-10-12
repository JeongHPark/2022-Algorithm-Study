#include <string>
#include <vector>
#include<cmath>
#include<algorithm>

using namespace std;
/*
    순열을 이용하여 숫자들을 조합해 수를 만들고 중복값 제거 후에 소수판별 알고리즘으로 소수가 맞다면 anwser값을 증가시키는 방식으로 풀이했습니다.
    도저히 감이 안잡혀서 풀이를 찾아보고 진행하였으며 이해가 안되는 코드에 대해 추가적으로 블로그를 찾아보면서 공부했습니다.
*/
 bool primeNumber(int num) {
    if (num <= 1) return false;    // 1은 소수 X.    
    if (num <= 3) return true;    // 2,3은 소수
    if (num % 2 == 0) return false; // 2로 나누어지면 무조건 합성수
     // num이  3 ~ 루트 num사이 수로 나누어지는게 없으면 소수
    for (int i = 3; i <= sqrt(num); i += 2) if (num % i == 0) return false;  
    return true;
}
int solution(string numbers) {
    int answer = 0;
    vector <char>num; // string으로 입력을 받기때문에 이어져있는 숫자들을 따로따로 저장할 변수  
    vector <int> result; // 소수인지 아닌지 판별할 숫자들이 들어가있는 변수   
    for (int i = 0; i < numbers.size(); i++) num.push_back(numbers[i]); // 숫자를 하나씩 벡터에 저장
    sort(num.begin(), num.end()); // 오름차순으로 정렬
        
    do {
        string tmp = ""; // num에서 숫자를 뽑아 하나의 수로 만드는 변수
        for (int i = 0; i < num.size(); i++) { 
            tmp += num[i];  // 숫자 저장 
            result.push_back(stoi(tmp)); // result에 넣어줌
        }
    } while (next_permutation(num.begin(),num.end())); // 순열이 끝날때 까지 반복함
    sort(result.begin(), result.end()); // 오름차순 정렬 
    result.erase(unique(result.begin(), result.end()), result.end()); // 중복값 제거
    for (int i = 0; i < result.size(); i++) if (primeNumber(result[i]) == true)answer++; // result변수에 들어가있는 수가 소수면 answer++
    return answer;
}

// https://mjmjmj98.tistory.com/50 풀이
// https://kbj96.tistory.com/32 소수 판별
// https://mjmjmj98.tistory.com/38 순열 (next_permutation)
// https://dpdpwl.tistory.com/39 unique
