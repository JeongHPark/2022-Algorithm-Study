'''
누적합 개념을 사용해야함
ex)10 20 30 40 50 일경우 10 30 60 100 150 으로 바꾸면
idx 3~5의 합이필요할경우 150-30=120으로 단순 빼기연산으로 누적합을 바로 구할수있음
DP 와 dfs사용으로 중복 연산을 최소화함(dp값이 있을경우 바로 return 해줌)
재귀 깊이 오류발생 sys.setrecursionlimit(100000) 추가
'''
import sys
sys.setrecursionlimit(100000)
n=int(input())
train=list(map(int,input().split()))
m=int(input())
sum=[0]*(n+1)
dp=[[-1 for _ in range(n)] for _ in range(3)]
for i in range(1,n+1):
    sum[i]+=sum[i-1]+train[i-1]
def dfs(idx,cnt):
    if n-idx+1<m:
        return 0
    elif cnt>=3:
        return 0
    elif dp[cnt][idx]!=-1:
        return dp[cnt][idx]
    else:
        dp[cnt][idx]=max(dfs(idx+1,cnt),sum[idx+m-1]-sum[idx-1]+dfs(idx+m,cnt+1))
        return dp[cnt][idx]
dfs(0,0)
print(max(dp[0]))


