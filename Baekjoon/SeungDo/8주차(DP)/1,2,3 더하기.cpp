#include<iostream>
using namespace std;
// 블로그를 참고해 풀이했습니다. https://omyodevelop.tistory.com/43
int main() {
	int n,x;
	int arr[11];

	cin >> n;

	arr[0] = 0;
	arr[1] = 1;
	arr[2] = 2;
	arr[3] = 4;

	for (int i = 4; i < 11; i++) {
		// 점화식 이용
		arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3];
	}

	for (int i = 0; i < n; i++) {
		cin >> x;
		cout << arr[x] << endl;	
	}
}
