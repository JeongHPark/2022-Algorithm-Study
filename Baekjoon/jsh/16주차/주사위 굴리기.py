'''
구현문제
'''
import sys
input=sys.stdin.readline
N,M,y,x,k=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(N)]
order=list(map(int,input().split()))
e,w,s,n,u,d=0,0,0,0,0,0
for i in order:
    if i==1 and x+1<M:
        temp=e
        e=u
        u=w
        w=d
        d=temp
        x+=1
        if maps[y][x]==0:
            maps[y][x]=d
        else:
            d=maps[y][x]
            maps[y][x]=0
        print(u)
    if i==2 and x-1>=0:
        temp=e
        e=d
        d=w
        w=u
        u=temp
        x-=1
        if maps[y][x]==0:
            maps[y][x]=d
        else:
            d=maps[y][x]
            maps[y][x]=0
        print(u)
    if i==4 and y+1<N:
        temp=n
        n=d
        d=s
        s=u
        u=temp
        y+=1
        if maps[y][x]==0:
            maps[y][x]=d
        else:
            d=maps[y][x]
            maps[y][x]=0
        print(u)
    if i==3 and y-1>=0:
        temp=s
        s=d
        d=n
        n=u
        u=temp
        y-=1
        if maps[y][x]==0:
            maps[y][x]=d
        else:
            d=maps[y][x]
            maps[y][x]=0
        print(u)

