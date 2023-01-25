#include <string>
#include <vector>
#include<algorithm>
#include<iostream>
using namespace std;
int main() {
	vector <string> v,answer;
	int n, m;
	string s;
	cin >> n >> m;
	for (int i = 0; i < n + m; i++) { // 입력받은 이름 벡터에 넣음
		cin >> s;
		v.push_back(s);
	}
	sort(v.begin(), v.end()); // 오름차순 정렬
	for (int i = 0; i < v.size(); i++) {
		int check = 0;
		if (i != v.size() - 1 && v[i] == v[i + 1]) { // 인접 배열만 비교
			answer.push_back(v[i]);
		}
	}
	cout << answer.size() << "\n"; 
	for (int i = 0; i < answer.size(); i++) {
		cout << answer[i] << "\n";
	}

}
