def solution(n, edge):
    answer = 0
    li=[[] for i in range(n+1)]
    ds=[0]*(n+1)
    for i in edge:
        li[i[0]].append(i[1])
        li[i[1]].append(i[0])
    stack=[1]
    while stack:
        num=stack.pop(0)
        for i in li[num]:
            if ds[i]==0 and i!=1:
                ds[i]=ds[num]+1
                stack.append(i)
    return ds.count(max(ds))
