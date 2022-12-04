from collections import deque #양방향에서 추가 및 제거 가능

t=int(input())

dx = [1,0,0,-1]
dy = [0,-1,1,0]

def bfs(mp, q, j):
    queue = deque()
    queue.append((q,j))
    mp[q][j] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=m or ny < 0 or ny >= n:
                continue
            if mp[nx][ny] == 1:
                mp[nx][ny] = 0
                queue.append((nx, ny))
    return

for i in range(t):
  answer=0
  m,n,k=map(int,input().split())
  mp=[[0]*n for i in range(m)] # 리스트 배열수에 맞게 초기화
  
  for j in range(k):
    x,y=map(int,input().split())
    mp[x][y]=1
    
  for q in range(m):
    for j in range(n):
      if mp[q][j]==1: # 배추 발견시 bfs실행 및 answer 수 증가
        answer+=1
        bfs(mp, q, j)
  print(answer)
