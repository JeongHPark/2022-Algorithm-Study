#dp[i]=dp[i-3]+dp[i-2]+dp[i-1] 를 이용하여 초기값 0인덱스값은 의미가 없으므로 식이 성립하게 1를 추가
#최댓값을 구한뒤 그 수만큼 다 돌린 후 입력받은 케이스값 한꺼번에 출력

dp=[1,1,2]
t=int(input())
ls=[]
for i in range(t):
  ls.append(int(input()))
n=max(ls)
for i in range(3,n+1):
  dp.append(dp[i-3]+dp[i-2]+dp[i-1])
for i in ls:
  print(dp[i])
  
