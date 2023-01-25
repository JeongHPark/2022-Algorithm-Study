import sys
N,M,V=map(int,sys.stdin.readline().strip().split())
h=[[] for i in range(N+1)]
for i in range(M): #인접행렬 생성
    a,b=map(int,sys.stdin.readline().strip().split())
    h[a].append(b)
    h[b].append(a)
for i in h:
    i.sort(reverse=True) #역정렬(작은수부터 방문해야하므로)
def dfs():
    stack=[V]
    visit=[]
    while stack and len(visit)!=N:
        store=stack.pop()
        if store not in visit:
            visit.append(store)
            for i in h[store]:
                if i not in visit:
                    stack.append(i)
    return visit
def bfs():
    que=[V]
    visit=[V]
    while que and len(visit)!=N:
        for i in reversed(h[que.pop(0)]): #우선순위 때문에 리스트를 역순으로바꿈(작은수부터방문)
            if i not in visit:
                que.append(i)
                visit.append(i)
    return visit
print(' '.join(map(str,dfs()))) #문자열로 합쳐줌
print(' '.join(map(str,bfs())))
