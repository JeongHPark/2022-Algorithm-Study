//주어진 정보를 2차원으로 저장
//저장한 정보를 첫번째 원소에 대하여 정렬
//두번째 원소의 값을 비교하면서 i-1 의 second 보다 크다면 i 는 i-1 보다 첫번째 두번째 모두 순위가 낮기에 선발되지않는다.
//작다면 선발이 되기때문에 그 다음사람의 조건을 위해 최솟값을 유지시키면서 탐색한다. 

#include<iostream>
#include <string>
#include <vector>
#include<memory>
#include<algorithm>
#include<vector>

using namespace std;

int N;
vector<pair<int, int>> ranking; //2차원으로 저장
void Input() {  //입력문
	cin >> N;
	for (int i = 0; i < N; i++) {
		int a, b;
		cin >> a >> b;
		ranking.push_back({ a,b });
	}
}

void solution() {
	int result = 1; //첫번째 사람은 항상 선발됨
	sort(ranking.begin(), ranking.end()); //정렬
	int mn = ranking[0].second; //첫번째 사람의 second를 기준으로 잡음
	for (int i = 1; i < ranking.size(); i++) {
		if (ranking[i].second < mn) { result++; mn = ranking[i].second; } //작다면 선발인원을 1 추가해주고 최솟값을 바꿔줌
	}
	cout << result<<endl;
}

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		Input();
		solution();
		ranking.clear();
	}
}
