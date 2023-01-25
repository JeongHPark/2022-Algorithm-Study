T=int(input())
for j in range(T):
    dp=[0,1,2,4] #N이 0,1,2,3 일때의 경우의수
    N=int(input())
    for i in range(4,N+1): #N이 4이상일때의 경우의수
        dp.append(dp[i-2]+dp[i-1]+dp[i-3])
    print(dp[N])
