#include <string>
#include <vector>

using namespace std;

string solution(string number, int k) {
    string answer;
    int ck = number.length() - k, x = 0 , z = 0; 
    // ck : �̾ƾ��� ���� x : ū���� ã�� �ڿ� ���� ū�� ã�� ��ǥ, z : x���� �Ű��ִ� ����

    while (ck != 0) {
        char max = '-100'; // �� �� ���� char������ ����
        for (int i = x; i <= number.length() - ck; i++) { 
            if (max < number[i] ) { // max�� �� �� ���� ū�� ã��
                max = number[i];
                z = i;
                if (max == 9)break; // max�� 9�϶� 9���� ū���� ������ �ٷ� break; 
            }
        }
        answer += max; // ã�� max���� answer�� �־���
        ck--; // ã�ƾ��� ������ ������ �ϳ� �ٿ���
        x = z + 1; // max�� �ִ� ��ǥ�� + 1�� x�� ����
    }
    return answer;
}
