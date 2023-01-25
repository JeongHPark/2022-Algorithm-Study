#include <string>
#include <vector>
#include<algorithm>
#include<iostream>
using namespace std;
// 이분탐색 STL함수로 처음에 풀이했지만 이분탐색의 매커니즘을 알기위해 직접 구현해봤습니다.
// 구현한 이분탐색 함수로 벡터값만 매개변수로 넘겼더니 시간초과가 나서 주소값으로 매개변수를 받아 문제해결함. 
bool BinarySearch(vector<int> &nNumbers, int len, int key) {  
	int start = 0, end = len - 1;
	while (start <= end) {
		int mid = (start + end) / 2;    // 중앙 값
		if (nNumbers[mid] == key)   // 키값과 중앙 값이 같을 때 리턴
			return true;
		else if (nNumbers[mid] < key)  // 키값이 mid의 값보다 클때
			start = mid + 1;
		else  // 키값이 mid의 값보다 작을때
			end = mid - 1;
	}
	return false; // 키값을 찾지 못함
}

int main() {
	vector<int> nNumbers,mNumbers;
	int n, m,a;

	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a;
		nNumbers.push_back(a);
	}
	cin >> m;
	for (int i = 0; i < m; i++) {
		cin >> a;
		mNumbers.push_back(a);
	}
	sort(nNumbers.begin(), nNumbers.end()); // 이분탐색을 위한 정렬
	
	for (int i = 0; i < m; i++) {
	//	cout<< binary_search(nNumbers.begin(), nNumbers.end(), mNumbers[i])<<"\n"; 이분탐색 STL함수 
		if (BinarySearch(nNumbers, nNumbers.size(), mNumbers[i]) == true) cout << 1 << "\n";
		else cout << 0 << "\n";
	}
}
