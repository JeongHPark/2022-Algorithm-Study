#include <string>
#include <vector>
#include <algorithm>
using namespace std;
// 오름차순으로 정렬한 후 citations.size만큼 반복문을 돌려 answer에 H_Index값을 넣고 
// citations[i]값이 answer값보다 큰지 비교 후 리턴 
// 문제가 이해가 잘 안돼서 풀이를 보고 진행하였습니다. https://yabmoons.tistory.com/694
int solution(vector<int> citations)
{
	sort(citations.begin(), citations.end()); // 오름차순 정렬
	for (int i  = 0; i  < citations.size(); i++)
	{
		int answer  = citations.size() - i; // h_Index값 넣음
		if (citations[i] >= answer) return answer; // h_Index값보다 인용횟수가 크거나 같다면 h_Index값 리턴
	}
    return 0; // 인용횟수가 전부다 0 일때 0 리턴
}
