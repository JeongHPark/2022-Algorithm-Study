using namespace std;
// N부터 0까지 N이 짝수일 때 N/2 홀수일 때 N--,ans++하면서 0까지 순환을 이용하여 풀이해봤습니다.
void cycle(int *n, int* ans) {
    if (*n == 0) return; // 0일때 순환 종료
    if (*n % 2 == 0) *n /= 2; // N이 짝수일 때 순간이동
    else { // N이 홀수일 때 점프후 건전지 사용량 ++
        *n -= 1;
        *ans += 1;
    }
    cycle(n, ans); 
}
int solution(int n)
{
    int ans = 0;
    cycle(&n, &ans); // 순환

    return ans;
}
