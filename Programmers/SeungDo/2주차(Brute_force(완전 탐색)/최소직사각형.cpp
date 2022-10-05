#include <string>
#include <vector>

// 가로 길이가 가장 큰 명함을 찾은뒤 세로길이가 가장 큰 명함을 찾고 answer에 곱해줌

using namespace std;

// 함수에서 벡터 값을 바꾸기 위해 참조의 의한 호출을 했습니다.(call by reference)
void tempFunc(vector<vector<int>> &sizes , int i) { // 가로 세로 길이를 바꿔주는 함수
    int temp = 0;
    if (sizes[i][1] > sizes[i][0]) {
        temp = sizes[i][1];
        sizes[i][1] = sizes[i][0];
        sizes[i][0] = temp;
    }
}
int solution(vector<vector<int>> sizes) {
    int answer = 0, max = 0; // max: 큰값  
    for (int i = 0; i < sizes.size(); i++) {     // 가장 큰 가로 길이 찾음
        tempFunc(sizes, i);       // 만약 가로길이나 세로길이가 반대쪽 길이보다 크면 큰수로 바꿔줌 
        if (max < sizes[i][0]) max = sizes[i][0];    // 가장 큰값 찾음  
    }
    answer += max;     // 나온 max값을 answer에 더해줌
    max = 0;        // 가장 큰 세로길이를 구하기 위해 max를 0으로 초기화
    for (int i = 0; i < sizes.size(); i++) {       // 가장 큰 세로 길이 찾음
        tempFunc(sizes, i);       // 만약 가로길이나 세로길이가 반대쪽 길이보다 크면 큰수로 바꿔줌  
        if (max < sizes[i][1]) max = sizes[i][1];    // 가장 큰값 찾음  
    }
    answer *= max; // 가로값이 들어가있는 max에 구한 세로값을 곱합
    return answer;
}
