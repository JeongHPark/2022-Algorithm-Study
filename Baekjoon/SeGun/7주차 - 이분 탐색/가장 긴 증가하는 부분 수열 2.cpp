//시간초과를 해결하지 못했고, 이분탐색을 어디서 사용해야 하는지 찾지 못해서 블로그를 보고 해결함
//https://seungkwan.tistory.com/8
//길이별로 마지막에 올 수 있는 최솟값을 기억해서 계속 초기화해주는 것이 핵심
//len[3]=5 -> 길이가 3 인 부분수열의 마지막값의 최솟값은 5
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<queue>
#define endl "\n"

using namespace std;

int N;
vector<int> n;

void input() {
	cin >> N;
	for (int i = 0; i < N; i++) { int x; cin >> x; n.push_back(x); }
}

void solution() {
	vector<int> len;	//len[3]=5 -> 길이가 3 인 부분수열의 마지막값의 최솟값은 5
	len.push_back(n[0]);	//첫번째 값은 바로 들어간다
	for (int i = 1; i < N; i++) {
		if (len.back() < n[i]) {	//탐색하는 값이 더 크다면 len에 push
			len.push_back(n[i]);
		}
		else {	//더 작다면 그 값은 길이가 '얼마'인 부분수열의 마지막값으로 들어가는지 확인 이때 이분탐색 사용
			int idx=lower_bound(len.begin(), len.end(), n[i])-len.begin();	//lower_bound, upper_bound 는 둘다 주소를 반환하기때문에 조심해야한다.
			//bound의 대한 설명 https://seungkwan.tistory.com/8
			len[idx] = n[i];
		}
	}
	/*for (auto x : len) {
		cout << x << " ";
	}*/
	//10 20 10 30 20 50 을 입력하면 len 에는
	//10 20 30 50 이 들어가게된다
	//길이가 1인 부분수열의 마지막에 올 수 있는 최솟값은 10
	//길이가 2인 부분수열의 마지막에 올 수 있는 최솟값은 20
	//길이가 3인 부분수열의 마지막에 올 수 있는 최솟값은 30
	//길이가 4인 부분수열의 마지막에 올 수 있는 최솟값은 50

	//마지막에 len 의 길이를 구해주면 됨
	cout << len.size();
}

int main(void) {
	input();
	solution();
}
