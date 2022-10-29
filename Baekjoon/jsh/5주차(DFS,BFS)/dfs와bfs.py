import sys
N,M,V=map(int,sys.stdin.readline().strip().split())
h=[[] for i in range(N+1)]
for i in range(M):
    a,b=map(int,sys.stdin.readline().strip().split())
    h[a].append(b)
    h[b].append(a)
for i in h:
    i.sort(reverse=True)
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
        for i in reversed(h[que.pop(0)]):
            if i not in visit:
                que.append(i)
                visit.append(i)
    return visit
print(' '.join(map(str,dfs())))
print(' '.join(map(str,bfs())))
