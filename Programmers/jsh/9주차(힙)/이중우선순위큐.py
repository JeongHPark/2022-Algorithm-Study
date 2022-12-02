import heapq
def solution(operations):
    minheap=[]
    maxheap=[]
    num=0
    for i in operations:
        if i[0]=="I":
            heapq.heappush(minheap,int(i[2:]))
            heapq.heappush(maxheap,-int(i[2:]))
            num+=1
        elif num>0:
            if i=="D 1":
                heapq.heappop(maxheap)
                num-=1
            elif i=="D -1":
                heapq.heappop(minheap)
                num-=1
        if num==0:
            while minheap:
                heapq.heappop(minheap)
            while maxheap:
                heapq.heappop(maxheap)
    if num==0:
        return [0,0]
    elif num==1:
        a=heapq.heappop(minheap)
        return [a,-a]
    elif num>=2:
        return [-heapq.heappop(maxheap),heapq.heappop(minheap)]
