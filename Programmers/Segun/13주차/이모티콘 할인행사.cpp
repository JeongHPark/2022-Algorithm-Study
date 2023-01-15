10,20,30,40 각각 할인율을 배열에 따로 넣어주고 조합으로 나올수있는 경우의 수를 모두 탐색
그중에서 문제의 우선순위에따라 이모티콘 플러스 서비스 가입자가 가장 많은 값을 유지하면서
이모티콘 판매액을 최대로 유지
users 의 범위와 emoticons의 범위가 좁기때문에 DFS 가능
문제에 할인율은 10,20,30,40 이라는 것을 제대로 확인하지 못해서 시간낭비 문제를 확실하게 이해하자

#include <string>
#include <vector>
#include<algorithm>
#include<iostream>

using namespace std;

int mx = 0;
int mn = 100;
int n;
int arr[11];
int resultA;
int resultB;

void solve(vector<vector<int>>& users, vector<int>& emoticons) {
	int A = 0, B = 0;
	for (int i = 0; i < users.size(); i++) {
		int sum = 0;
		for (int j = 0; j < emoticons.size(); j++) {
			if (users[i][0] <= arr[j])
				sum += emoticons[j] / 100 * (100 - arr[j]);
		}
		if (sum >= users[i][1])
			A++;
		else
			B += sum;
	}
	if (resultA < A) {
		resultA = A;
		resultB = B;
	}
	else if (resultA == A) 
		resultB=max(resultB,B);
}

void DFS(int cnt, vector<vector<int>>& users, vector<int>& sales, vector<int>& emoticons) {
	if (cnt == n) {
		solve(users, emoticons);
		return;
	}
	for (int i = 0; i < sales.size(); i++) {
		arr[cnt] = sales[i];
		DFS(cnt + 1, users, sales, emoticons);
	}
}

vector<int> solution(vector<vector<int>> users, vector<int> emoticons) {
	vector<int> answer;
	vector<int> sales{10,20,30,40};
	n = emoticons.size();
	DFS(0, users, sales, emoticons);
    answer.push_back(resultA);
    answer.push_back(resultB);
	return answer;
}
