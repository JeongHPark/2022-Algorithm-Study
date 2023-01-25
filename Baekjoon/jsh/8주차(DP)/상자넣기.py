#증가하는부분수열에서 사용한 LIS 알고리즘 사용
N=int(input())
box=list(map(int,input().split(" ")))
dp=[]
for i in box:
    if not dp:
        dp.append(i)
        continue
    if dp[-1]<i:
        dp.append(i)
    else:
        for j in range(len(dp)):
            if dp[j]>=i:
                dp[j]=i
                break
print(len(dp))
