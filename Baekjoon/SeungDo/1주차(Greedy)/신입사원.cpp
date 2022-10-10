#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

// 서류,면접 순위를 2차원 벡터인 numCase에 넣고 서류순위 기준으로 오름차순 정렬을 한뒤 passRaking에 서류순위가 1등인 사람의 면접순위를 넣습니다.
// 그리고 인원수 만큼 반복문을 돌리면서 passRaking의 등수보다 낮으면 합격이 되는 식으로 코딩 해봤습니다. 
 
// 정렬을 하고 합격자를 어떻게 뽑아야할지 고민하다가 답이 안나와서 풀이를 참고했습니다.
// 계속 시간초과가 나서 블로그를 찾아보고 해결했습니다.
void solution() {
	int testCase, num, a, b , passRanking; 

	// 시간초과 해결 코딩 (링크 참조)
	ios::sync_with_stdio(false); 
	cin.tie(NULL);

	cin >> testCase; 

	for (int z = 0; z < testCase; z++) {
		cin >> num;
		vector<vector<int>> numCase; // 서류, 면접 등수를 저장할 2차원 벡터
		for (int i = 0; i < num; i++) {
			vector<int> arr;
			cin >> a >> b; 
			arr.push_back(a);
			arr.push_back(b);
			numCase.push_back(arr); // 2차원 벡터이 a,b저장

		}
		sort(numCase.begin(), numCase.end()); // 서류 등수 기준으로 오름차순 정렬
		passRanking = numCase[0][1]; // 서류순위 1등인 사람의 면접점수를 passRaking 변수에 대입
		int count = 1; // 서류 순위 1등인 사람은 이미 합격 했으니깐 count는 1
		for (int i = 1; i < num; i++) { // 서류순위 2등부터 마지막등수까지 반복
			if (passRanking > numCase[i][1]) { // passRaking에 들어가있는 면접순위보다 다른사람의 면접순위가 낮다면
				count++; // 합격자 + 1
				passRanking = numCase[i][1]; // 합격자의 면접 순위를 passRaking에 대입
			}
		}
		cout << count << "\n"; // 최종 출력
	}
}
int main() {	
	solution();
}

// https://tooo1.tistory.com/245 풀이
// https://blog.in-coder.com/c%EC%96%B8%EC%96%B4-c-%EB%B0%B1%EC%A4%80-cin-cout-%EC%8B%9C%EA%B0%84%EC%B4%88%EA%B3%BC-%ED%95%B4%EA%B2%B0%EB%B2%95/ 시간초과 해결
