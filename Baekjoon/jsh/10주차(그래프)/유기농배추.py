import sys
input=sys.stdin.readline
x=[0,0,1,-1]
y=[1,-1,0,0]
T=int(input().strip())

def bfs(li,a,b):
    stack=[[a,b]]
    li[b][a]=0
    while stack:
        temp=stack.pop(0)
        for i in range(4):
            if N>temp[1]+y[i]>=0 and M>temp[0]+x[i]>=0:
                if li[temp[1]+y[i]][temp[0]+x[i]]==1:
                    li[temp[1]+y[i]][temp[0]+x[i]]=0
                    stack.append([temp[0]+x[i],temp[1]+y[i]])
                    
for i in range(T):
    M,N,K=map(int,input().split())
    li=[[0 for _ in range(M)]for _ in range(N)]
    for i in range(K):
        a,b=map(int,input().split())
        li[b][a]=1
    count=0
    for i in range(N):
        for j in range(M):
            if li[i][j]==1:
                bfs(li,j,i)
                count+=1
    print(count)
