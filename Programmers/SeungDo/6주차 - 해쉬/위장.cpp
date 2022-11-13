#include <string>
#include <vector>
#include<algorithm>
using namespace std;
// clothes 종류 별 갯수 + 1(착용하지않음)를 구한 뒤 모든 갯수를 곱한 뒤 -1하고(다 착용하지 않았을 때) 리턴
int solution(vector<vector<string>> clothes) {
    int answer = 1;
    vector<string> clothesType;
    for (int i = 0; i < clothes.size(); i++) clothesType.push_back(clothes[i][1]); // 종류만 넣은 벡터
    sort(clothesType.begin(), clothesType.end()); // 정렬 (중복제거를 하기위해선 정렬이 돼있어야함)
    clothesType.erase(unique(clothesType.begin(), clothesType.end()), clothesType.end()); // 해당 벡터 중복제거
    if (clothesType.size() == 1) return clothes.size(); // 종류가 한가지일때 clothes 갯수만큼 리턴 (입출력 예 2번)
    int* number = new int[clothesType.size()]; // 옷 종류 갯수가 들어갈 동적배열

    for (int i = 0; i < clothesType.size(); i++) number[i] = 1; // 1로 초기화 (해당 옷 착용하지않음)
    for (int i = 0; i < clothes.size(); i++)  // 옷종류 갯수 구하는 반복문
        for (int j = 0; j < clothesType.size(); j++)  
            if (clothes[i][1] == clothesType[j]) number[j] += 1;

    for (int i = 0; i < clothesType.size(); i++)  answer *= number[i]; // 갯수 전부다 곱함
    free(number);
    return answer - 1; // -1(전부다 착용하지 않음)한 후 리턴 
}
