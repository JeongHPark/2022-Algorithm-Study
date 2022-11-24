n = int(input())
box = list(map(int, input().split()))
dp = [1 for i in range(n)] # 자기자신 하나 최솟값으로 모두 설정
for i in range(1,n):
    tmp = 0
    index = i
    for j in range(i):# i 앞에 값들만 돌림
        if box[i] > box[j] and dp[j] > tmp:
            tmp = dp[j]
            index = j
    if index != i: #위의 for문으로 값이 바뀌었으면 dp값에 추가
        dp[i] += tmp          
print(max(dp))
