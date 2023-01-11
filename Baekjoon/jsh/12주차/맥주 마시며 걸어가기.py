'''
그래프문제이므로 bfs,dfs사용 bfs 사용하였음
최대 100*100*50번 반복하므로 시간충분
시작지점부터 1000m까지 움직일수있으므로 queue에 맨처음 시작부분을 넣고
절대값 abs() 를사용하여 거리가 1000m 이하인지 확인후 맞으면 queue에 넣고
visit변수를 1로 설정(방문)
queue가 빌때까지 반복
ret 변수를 "sad"로 초기화하여 22번줄을 한번도 충족하지 않으면 "sad"가 출력되게함
'''
T=int(input())
for i in range(T):
    n=int(input())
    start=list(map(int,input().split(" ")))
    mid=[]
    for i in range(n):
        mid.append(list(map(int,input().split(" "))))
    end=list(map(int,input().split()))
    queue=[start]
    visit=[0]*n
    ret="sad"
    while queue:
        temp=queue.pop(0)
        if abs(end[0]-temp[0])+abs(end[1]-temp[1])<=1000:
            ret="happy"
            break
        for idx,val in enumerate(mid):
            if visit[idx]==0 and abs(val[0]-temp[0])+abs(val[1]-temp[1])<=1000:
                visit[idx]=1
                queue.append([val[0],val[1]])
    print(ret)


