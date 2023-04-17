user_id가 banned_id 와 같은지를 판별하는 함수를 만들어준다
DFS를 사용해서 user_id와 banned_id 가 같은 묶음이 몇개가 나오는지 확인한다
만들어진 묶음을 정렬하고 하나의 string 으로 만들어서 set 에 저장
-> 중복되는 경우를 방지하기 위해 ex) a,b,c -> abc, b,c,a -> abc 로 abc 경우는 하나만 set에 저장

#include <string>
#include <vector>
#include<iostream>
#include<algorithm>
#include<unordered_set>

using namespace std;

bool visited[11];
string arr[11];
unordered_set<string> us;

bool chkSame(string str1, string str2) {
	if (str1.size() != str2.size())
		return false;
	for (int i = 0; i < str1.size(); i++) {
		if (str2[i] != '*' && str1[i] != str2[i])
			return false;
	}
	return true;
}

void dfs(int cnt, vector<string>& user_id, vector<string>& banned_id) {
	if (cnt == banned_id.size()) {
		vector<string> vec;
		for (auto x : arr)
			vec.push_back(x);
		sort(vec.begin(), vec.end());
		string str = "";
		for (auto x : vec)
			str += x;
		us.insert(str);
		return;
	}
	for (int i = 0; i < user_id.size(); i++) {
		if (visited[i] == false && chkSame(user_id[i], banned_id[cnt]) == true) {
			visited[i] = true;
			arr[cnt] = user_id[i];
			dfs(cnt + 1, user_id, banned_id);
			visited[i] = false;
		}
	}
}

int solution(vector<string> user_id, vector<string> banned_id) {
	dfs(0, user_id, banned_id);
	return us.size();
}
