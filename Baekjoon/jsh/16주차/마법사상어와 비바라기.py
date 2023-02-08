'''
구현 문제
파이썬만 그런건지 모르겠는데 -1%3 음수의 나머지를구하면 2가나옴
따로 음수 처리를 안해도됨
속도가 더빠르게나옴
'''
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(n)]
order=[list(map(int,input().split())) for _ in range(m)]
di=[[0,0],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
stack1=[[n-1,0],[n-1,1],[n-2,0],[n-2,1]]
stack2=[]
visit=[[0 for _ in range(n)] for _ in range(n)]
answer=0
for i in order:
    while stack1:
        temp=stack1.pop()
        y=(temp[0]+(di[i[0]][0]*i[1]))%n
        # if y>=n:
        #     y=y%n
        # elif y<0:
        #     y=n-1-(-(y+1)%n)
        x=(temp[1]+(di[i[0]][1]*i[1]))%n
        # if x>=n:
        #     x=x%n
        # elif x<0:
        #     x=n-1-(-(x+1)%n)
        stack2.append([y,x])
        maps[y][x]+=1
    while stack2:
        temp=stack2.pop()
        visit[temp[0]][temp[1]]=1
        if temp[0]-1>=0 and temp[1]-1>=0 and maps[temp[0]-1][temp[1]-1]>0:
            maps[temp[0]][temp[1]]+=1
        if temp[0]+1<n and temp[1]-1>=0 and maps[temp[0]+1][temp[1]-1]>0:
            maps[temp[0]][temp[1]]+=1
        if temp[0]-1>=0 and temp[1]+1<n and maps[temp[0]-1][temp[1]+1]>0:
            maps[temp[0]][temp[1]]+=1
        if temp[0]+1<n and temp[1]+1<n and maps[temp[0]+1][temp[1]+1]>0:
            maps[temp[0]][temp[1]]+=1
    for j in range(n):
        for k in range(n):
            if maps[j][k]>=2:
                if visit[j][k]==0:
                    maps[j][k]-=2
                    stack1.append([j,k])
                else:
                    visit[j][k]=0
print(sum(sum(maps[i]) for i in range(n)))
