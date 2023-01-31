'''
bfs 사용 치즈에닿으면 cnt 1증가 cnt 2이상이면 삭제후 visit=-2설정
'''
from collections import deque
n,m=map(int,input().split())
ch=[list(map(int,input().split())) for _ in range(n)]
dp=[[-1 for _ in range(m)] for _ in range(n)]
xy=[[0,1],[1,0],[0,-1],[-1,0]]
answer=0
cnt=0
for i in range(n):
    for j in range(m):
        if ch[i][j]==1:
            dp[i][j]=0
            cnt+=1
queue=deque()
while cnt!=0:
    queue.append([0,0])
    while queue:
        temp=queue.popleft()
        for i in xy:
            x=temp[1]+i[1]
            y=temp[0]+i[0]
            if 0<=y<n and 0<=x<m:
                if dp[y][x]==-1:
                    queue.append([y,x])
                    dp[y][x]=-2
                elif dp[y][x]>=0:
                    dp[y][x]+=1
                    if dp[y][x]>=2:
                        dp[y][x]=-2
                        ch[y][x]=0
                        cnt-=1
    for i in range(n):
        for j in range(m):
            if ch[i][j]==0:
                dp[i][j]=-1
            else:
                dp[i][j]=0
    answer+=1

print(answer)
