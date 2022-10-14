#include <vector>

using namespace std;
// arr의 첫 번째 값을 스택에 넣고 두 번째 값 부터 arr의 길이 만큼 반복문을 돌려 스택의 top값과 푸쉬 할 arr[i]값이 다르면 arr[i]값을 스택에 푸쉬
vector<int> solution(vector<int> arr){
    vector<int> answer;
    answer.push_back(arr[0]); // 스택 안에 값이 있어야 반복문에서 top값과 arr[i]값을 비교할 수 있기 때문에 arr의 첫 번째 값을 스택에 푸쉬함 
    for (int i = 1; i < arr.size(); i++) if (arr[i] != answer.back())answer.push_back(arr[i]); // arr[i]값과 스택의 top값을 비교 후 다르다면 스택에 푸쉬
    return answer;
}
