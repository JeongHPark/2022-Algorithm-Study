입력받은 배열을 오름차순으로 정렬 후 배열의 시작점과 끝점을 비교하면서 해결하려 했으나 사용하지 않는 공간을 불러오지 못해서 최적해를 찾지못함
사용하지 않는 공간을 알기위해서 우선순위 큐사용
수업이 끝나는 시간 한가지로 최적해를 찾기위해서 오름차순정렬
수업이 끝나는 시간이 낮은 것이 우선순위를 갖는 우선순위큐사용
top의 값보다 현재 탐색하고있는 배열의 시작점이 크거나 같다면 top 제거 후 현재 배열값의 끝점 push
top이 시작점보다 크다면 제거 없이 push
우선순위큐의 size 리턴

#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>

using namespace std;


int main(void) {
	int N;
	cin >> N;
	vector<pair<int, int>> vec;
	int result = 1;
	priority_queue<int, vector<int>, greater<int>> pq;

	for (int i = 0; i < N; i++) {
		int x, y;
		cin >> x >> y;
		vec.push_back({ x,y });
	}
	sort(vec.begin(), vec.end());
	pq.push(vec[0].second);
	for (int i = 1; i < vec.size();i++) {
		if (pq.top() <= vec[i].first) {
			pq.pop();
			pq.push(vec[i].second);
		}
		else
			pq.push(vec[i].second);
	}
	cout << pq.size();
}
