'''
구현문제
방향이 0,1,2,3으로 주어졌으므로 리스트를활용함
16번줄 exit를 활용하여 다 막혀있는지 확인
r,c가 리스트의 범위를 넘지않도록 조건추가
'''
n,m=map(int,input().split())
r,c,d=map(int,input().split())
map=[list(map(int,input().split())) for i in range(n)]
di=[[0,-1],[-1,0],[0,1],[1,0]]
answer=0
while 1:
    #청소하기
    if map[r][c]==0:
        map[r][c]=2
        answer+=1
    exit=0
    #왼쪽 탐색하며 회전하기
    for i in range(4):
        temp=di[d%4]
        if 0<=r+temp[0]<=n-1 and 0<=c+temp[1]<=m-1 and map[r+temp[0]][c+temp[1]]==0:
            d+=3
            r=r+temp[0]
            c=c+temp[1]
            exit=1
            break
        d+=3
    #다 막혀있을경우 후진가능한지 확인 
    if exit==0:
        temp=di[(d+3)%4]
        if not 0<=r+temp[0]<=n-1 or not 0<=c+temp[1]<=m-1 or map[r+temp[0]][c+temp[1]]==1:
            break
        r=r+temp[0]
        c=c+temp[1]

print(answer)
