선형 탐색으로 풀었을때 시간초과
정렬을 사용해서 선형 탐색 시간초과
set 을 사용해서 해결했을때 164ms
  
재귀함수를 사용해서 이분탐색 156ms
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<queue>


#define endl "\n"

using namespace std;

int N, M;
vector<int> n;
vector<int> m;

void Input() {
	cin >> N;
	for (int i = 0; i < N; i++) { int x; cin >> x; n.push_back(x); }
	cin >> M;
	for (int i = 0; i < M; i++) { int x; cin >> x; m.push_back(x); }
}

bool divide(int x, int start, int end) {
	int mid = (end + start) / 2;  //반을 의미하는 mid 선언
	if (n[mid] == x) { return true; } //나눈값이 찾는 값이면 참 리턴
	else if (start > end) { return false; } //start가 end보다 커진다면 종료

	if (x < n[mid]) { return divide(x, start, mid-1); } //x가 가운데 있는 값보다 작다면 end를 mid-1로 설정
	else if (x > n[mid]) { return divide(x, mid + 1, end); }  //x가 가운데 있는 값보다 크다면 start를 mid+1로 설정
}

void Solution() {
	sort(n.begin(), n.end());
	for (auto x : m) {
		if (divide(x, 0, n.size() - 1) == true) { cout << 1 << endl; }  
		else { cout << 0 << endl; }
	}
}

int main(void) {
	Input();
	Solution();
}

재귀함수가 아닌 while 문을 사용해서 확인해보기
while문 사용했을때 156ms
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<queue>


#define endl "\n"

using namespace std;

int N, M;
vector<int> n;
vector<int> m;

void Input() {
	cin >> N;
	for (int i = 0; i < N; i++) { int x; cin >> x; n.push_back(x); }
	cin >> M;
	for (int i = 0; i < M; i++) { int x; cin >> x; m.push_back(x); }
}

void Solution() {
	sort(n.begin(), n.end());
	for (auto x : m) {
		int left = 0, right = n.size() - 1;
		while (left <= right) {
			int mid = (left + right) / 2;
			if (n[mid] == x) { cout << 1 << endl; break; }
			
			if (x < n[mid]) { right = mid - 1; }
			else if (x > n[mid]) { left = mid + 1; }
		}
		if (left > right) { cout << 0 << endl; }
	}
}

int main(void) {
	Input();
	Solution();
}
