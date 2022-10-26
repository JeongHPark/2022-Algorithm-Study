#include <string>
#include <vector>
#include<algorithm>
// int형인 값들을 스트링형 벡터에 넣어준 후 정렬하고 0부터 길이만큼 answer에 +한 뒤 리턴 
using namespace std;
bool compare(string a, string b) {
    // a + b하고 b + a하고 큰쪽에 왼쪽으로 오게 정렬
    // ex) 3 30일때 330이 303보다 크기때문에 해당 조건으로 3 30으로 정렬
    // 해당 조건은 블로그를 참조했습니다. https://mungto.tistory.com/22
    return a + b > b + a;
}
string solution(vector<int> numbers) {
    string answer = "";
    vector<string> result;
    for (int i = 0; i < numbers.size(); i++)  result.push_back(to_string(numbers[i])); //스트링형 벡터로 옮김
    sort(result.begin(), result.end(),compare); // 정렬
    if (result[0] == "0") return "0"; // 첫번째가 0일때 0리턴 (문자열 리턴)
    for (int i = 0; i < result.size(); i++)  answer += result[i]; // 순서대로 answer에 ++
    return answer; //리턴 
}
