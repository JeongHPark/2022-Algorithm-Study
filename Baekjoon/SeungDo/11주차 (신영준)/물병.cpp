#include<iostream>
using namespace std;
// 최대한 합칠 수 있는 물병을 합친 다음 남는 물병들을 이용하여 사야되는 물병을 구함
int main() {
	int  K, N, x = 1, preX = 0;

	cin >> N >> K;

	for (int i = 0; i < K; i++) { // 들 수 있는 갯수 만큼 최대한 물병을 합침
		x = 1;
		while (1) {
			if (N < x) {
				x /= 2;
				break;
			}
			x *= 2;
		}
		N -= x;
		preX = x; // 합친 물병중 가장 작은 물병의 크기
	}
	if (N == 0) // 모든 물병이 합쳐졌다면 살 물병은 없음
		cout << "0";
	else  // 남아 있는 1리터짜리 물병들이 있다면 가장 작은 물병의 크기 - 남아 있는 1리터 물병 만큼 물병을 삼
		cout << preX - N ;

	return 0;
}
