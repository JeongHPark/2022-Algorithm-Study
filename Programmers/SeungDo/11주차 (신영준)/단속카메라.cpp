#include <string>
#include <vector>
#include <algorithm>

using namespace std;
// 진입지점을 기준으로 오름차순 정렬을 한 후 반복문을 돌리면서 가장 많은 차를 확인 할 수 있는 카메라 위치를 찾음
// 블로그를 참조해 풀이 했습니다.
int solution(vector<vector<int>> routes)
{
    int answer = 1; // 자동차의 대수가 1대 이상이기 때문에 카메라 초기 갯수는 1
    sort(routes.begin(), routes.end()); // 정렬

    int position = routes[0][1]; // 첫 번째 집입 차량의 진출 지점 저장

    for (int i = 1; i < routes.size(); i++)
    {
        // 카메라의 위치보다 해당 차량의 진출 지점이 더 빠르다면 카메라 위치를 해당 차량의 진출 지점으로 조정
        if (routes[i][1] < position) 
            position = routes[i][1]; 
        // 차량의 진입 지점이 카메라 위치보다 늦을 경우 전에 설정해 놓은 카메라 위치에 카메라 설치 및 해당 차량의 진출 시점으로 카메라 위치 설정
        else if (routes[i][0] > position)  
        {
            answer++;
            position = routes[i][1];
        }
    }
    return answer;
}
