N의 범위가 N(2 ≤ N ≤ 11) 이기때문에 DFS로 해결가능
연산은 연산의 상관없이 앞에서부터 진행하기때문에
연산자가 0이 아닌 즉 사용할 수 있는지 여부를 확인하고
현재의 값에 맞는 연산을 진행하면서 다음 단계로 넘겨준다.

#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<climits>

using namespace std;

int N;
vector<int> number;
int oper[4];	//+,-,*,/
int maxResult=INT_MIN;
int minResult=INT_MAX;

void input() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		int x;
		cin >> x;
		number.push_back(x);
	}
	for (int i = 0; i < 4; i++) {
		cin >> oper[i];
	}
}

void insertOper(int cnt,int cur) {
	if (cnt == N) {
		maxResult = max(maxResult, cur);
		minResult = min(minResult, cur);
	}
	for (int i = 0; i < 4; i++) {
		if (oper[i] != 0) {
			oper[i]--;
			if (i == 0)
				insertOper(cnt + 1, cur + number[cnt]);
			else if (i == 1)
				insertOper(cnt + 1, cur- number[cnt]);
			else if (i == 2)
				insertOper(cnt + 1, cur * number[cnt]);
			else if (i == 3)
				insertOper(cnt + 1, cur / number[cnt]);
				
			oper[i]++;
		}
	}
}

int main(void) {
	input();
	insertOper(1, number[0]);
	cout << maxResult << endl<< minResult;
}
