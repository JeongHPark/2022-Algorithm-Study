#include <string>
#include <vector>

using namespace std;

// 1~3번 수포자의 찍기 패턴을 배열에 넣어 놓고 answer의 수 만큼 반복을 돌려 수포자들이 답을 맞췄을때 tmp배열에 맞춘 갯수를 넣은뒤
// max값을 찾은 뒤 max값을 가진 수포자 번호를 찾아 result값에 넣고 return

// 처음에 수포자2의 패턴을 1 3 4 5로 하고 i값이 짝수(i & 2 == 0)가 될때 2를 비교하는 식으로 했는데 오답이 나와 2,1,2,3,2,4,2,5으로 바꿧더니 해결
// 위의 방법이 안되는지 아직도 잘 모르겠습니다. 혹시 아시면 피드백 해주시면 감사드리겠습니다. 

vector<int> solution(vector<int> answers) {
    vector<int> result; // 답
    int tmp[3] = {}; // 수포자들이 맞춘 문제 갯수 
    int z = 1,x = 0, y = 0; // 수포자 1 2 3 의 패턴 좌표갯수

    // 수포자1패턴은 1~5까지 순서대로이므로 만들지 않았음
    int person2Patten[8] = { 2,1,2,3,2,4,2,5 };  
    int person3Patten[10] = { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 };

    for (int i = 0; i < answers.size(); i++) {
        //수포자 1~3의 답 확인
        if (answers[i] == z) tmp[0] += 1;
        if (answers[i] == person2Patten[y])  tmp[1] += 1;
        if (answers[i] == person3Patten[x])  tmp[2] += 1;

        x++, y++, z++; // 각자의 좌표 ++

        // 각자의 좌표의 마지막에 되었을때 0으로 초기화
        if (z == 6) z = 1;
        if (x == 10) x = 0;
        if (y == 8) y = 0;
    }
    int max = 0;
    for (int i = 0; i < 3; i++) if (max < tmp[i])max = tmp[i];  // max값 찾기
    for (int i = 0; i < 3; i++) if (max == tmp[i])result.push_back(i + 1); // max값을 가진 수포자를 result값에 넣어줌
    return result;
}
