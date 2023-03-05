import heapq

def solution(n, works):
    if sum(works)<=n: return 0
    answer = 0
    works=[-i for i in works]
    heapq.heapify(works)
    for _ in range(n):
        a=heapq.heappop(works)
        a+=1
        heapq.heappush(works,a)

    works=[i**2 for i in works]
    answer=sum(works)
    return answer
