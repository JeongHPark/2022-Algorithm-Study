def solution(m, n, puddles):
    answer = 0
    dp=[[0 for _ in range(m)]for _ in range(n)]
    dp[0][0]=1
    for i in range(n):
        for j in range(m):
            if [j+1,i+1] not in puddles:
                if j+1<m and [j+2,i+1] not in puddles:
                    dp[i][j+1]+=dp[i][j]
                if i+1<n and [j+1,i+2] not in puddles:
                    dp[i+1][j]+=dp[i][j]
    return dp[n-1][m-1]%1000000007
