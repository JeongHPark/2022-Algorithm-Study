입력 받은 문자열을 tmp 라는 빈 문자열에 하나의 문자씩 계속 추가해서
폭발 문자열과 같은지 확인하고 같으면 같은 문자열을 없애주고 다시 이어서 추가하는 것을 반복

#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main(void) {
	string inputStr,boom,tmp="";
	cin >> inputStr>>boom;
	for (int i = 0; i < boom.size(); i++)
		tmp += inputStr[i];
	if (tmp == boom)
		tmp = "";
	for (int i = boom.size(); i < inputStr.size(); i++) {
		tmp.push_back(inputStr[i]);
		if (tmp.size() >= boom.size() && tmp.substr(tmp.size() - boom.size()) == boom) {
			for (int j = 0; j < boom.size(); j++)
				tmp.pop_back();
		}
	}
	if (tmp.size() == 0)
		tmp = "FRULA";
	cout << tmp;
}
