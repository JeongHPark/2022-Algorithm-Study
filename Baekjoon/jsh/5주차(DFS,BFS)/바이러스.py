N=int(input())
M=int(input())
li=[]
h=[[] for i in range(N+1)]
visit=[0 for i in range(N+1)]
for i in range(M):
    li.append(list(map(int,input().split(" "))))
for i in range(M):
    h[li[i][0]].append(li[i][1])
    h[li[i][1]].append(li[i][0])
stack=[1]
visit[1]=1
result=0
while stack:
    result+=1
    for i in h[stack.pop()]:
        if visit[i]!=1:
            stack.append(i)
            visit[i]=1
print(result-1)
