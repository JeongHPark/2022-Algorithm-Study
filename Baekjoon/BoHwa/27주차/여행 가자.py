#https://www.jongung.com/292를 참고하여 분리집합 개념을 이용하였습니다.

def union(x,y):
    x=find(x)
    y=find(y)
    if x>y:
        parent[x]=y
    else:
        parent[y]=x
    
def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]

n=int(input())
m=int(input())

graph=[list(map(int,input().split())) for _ in range(n)]
plan=list(map(int,input().split()))
parent=[i for i in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            union(i,j)
            
ans="YES"

for i in range(1,m):
    if parent[plan[i]-1]!=parent[plan[0]-1]:
        ans="NO"
        break
        
print(ans)
