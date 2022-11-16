#include <string>
#include <vector>
#include<algorithm>
#include<iostream>
using namespace std;
// 이분탐색을 안쓰고 풀이 해봤습니다.
int cmp(int a, int b) {
	return a > b;
}
int main() { 
	int n, h, m, answer = 0;
	vector<int>trees;
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n >> m;
	for (int i = 0; i < n; i++) { 
		cin >> h;
		trees.push_back(h);
	}
	sort(trees.begin(), trees.end(), cmp); //내림차순 정렬
	h = 1; // 나무의 번호 1~n번
	while (1) {
		if (h < n && (trees[h-1] - trees[h])*h <= m) { // 자를 나무 갯수가 n보다 작고 나무 두개의 차 * h가 m 보다 작을 때
			m -= (trees[h - 1] - trees[h]) * h; // m -  나무 두개의 차 * h를 함
			if (m == 0) { // m이 0일 때 
				answer = trees[h]; // 다음 나무의 길이를 answer에 넣고 브레이크
				break;
			}
			h++; // 0이 아니라면 다음 나무로
		}
		else {
			// 필요한 나무 길이 / 길이가 맞춰진 나무들 갯수 = 홀수면 올림, 짝수면 그대로
			if (m % h != 0) m = (m / h) + 1; 
			else m /= h;
			answer = trees[h - 1] - m; //  answer = 현재 나무 길이에 - 잘라야되는 나무 길이
			break;
		}
	}
	cout <<answer << "\n";
}
