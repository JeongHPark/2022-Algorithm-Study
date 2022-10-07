#include <string>
#include <vector>

// 가로 길이가 가장 큰 명함을 찾은뒤 세로길이가 가장 큰 명함을 찾고 answer에 곱해줌

using namespace std;
void tempFunc(vector<vector<int>> &sizes , int i) { // 가로길이에 가장 큰값으로 몰아줌
    int temp = 0;
    if (sizes[i][1] > sizes[i][0]) {
        temp = sizes[i][1];
        sizes[i][1] = sizes[i][0];
        sizes[i][0] = temp;
    }
}
int solution(vector<vector<int>> sizes) {
    int answer = 0, max1 = 0, max2 = 0; // max: 큰값  
    for (int i = 0; i < sizes.size(); i++) {     // 가장 큰 가로 길이 찾음
        tempFunc(sizes, i);       // 만약 가로길이나 세로길이가 반대쪽 길이보다 크면 큰수로 바꿔줌 
        if (max1 < sizes[i][0]) max1 = sizes[i][0];    // 가장 가로 큰값 찾음  
        if (max2 < sizes[i][1]) max2 = sizes[i][1];    // 가장 세로 큰값 찾음
    }
    answer = max1 * max2;     // 나온 max값을 answer에 더해줌

    return answer;
}
