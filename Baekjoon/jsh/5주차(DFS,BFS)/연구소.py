from copy import deepcopy
from itertools import combinations
N,M=map(int,input().split(" "))
li=[list(map(int,input().split(" "))) for i in range(N)]
two=[]
zero=[]
max=0
x=[0,1,-1,0] #상하좌우 탐색을위해
y=[1,0,0,-1]
for i in range(N): #0의 위치 리스트
    for j in range(M):
        if li[i][j]==0:
            zero.append([i,j])
for i in range(N): #2의 위치 리스트
    for j in range(M):
        if li[i][j]==2:
            two.append([i,j])
for q in list(combinations(zero, 3)): #0의 위치 중 3곳을 선택하는 모든경우의수를 뽑음
    lis=deepcopy(li) #리스트 복사
    for i,j in q: #조합중 한개의 경우를 뽑아서 벽을세워줌
        lis[i][j]=1
    for i,j in two: #2의 위치 돌아가면서 감염시작
        stack=[[i,j]] #dfs로 구현
        while stack:
            for k,l in [stack.pop()]:
                for m in range(4):
                    if N>k+y[m]>-1 and M>l+x[m]>-1 and lis[k+y[m]][l+x[m]]==0:
                        stack.append([k+y[m],l+x[m]])
                        lis[k+y[m]][l+x[m]]=2
    result=0
    for i in range(N):
        result+=lis[i].count(0)
    if max<result: #0의개수의 최댓값
        max=result

print(max)
