#include <string>
#include <vector>

using namespace std;

string solution(string number, int k) {
    string answer;
    int ck = number.length() - k, x = 0 , z = 0; 
    // ck : 뽑아야할 숫자 x : 큰수를 찾은 뒤에 다음 큰수 찾을 좌표, z : x값을 옮겨주는 변수

    while (ck != 0) {
        char max = '-100'; // 비교 할 값을 char형으로 선언
        for (int i = x; i <= number.length() - ck; i++) { 
            if (max < number[i] ) { // max와 비교 후 가장 큰값 찾음
                max = number[i];
                z = i;
                if (max == 9)break; // max가 9일때 9보다 큰값은 없으니 바로 break; 
            }
        }
        answer += max; // 찾은 max값을 answer에 넣어줌
        ck--; // 찾아야할 숫자의 갯수를 하나 줄여줌
        x = z + 1; // max가 있던 좌표값 + 1을 x에 대입
    }
    return answer;
}
