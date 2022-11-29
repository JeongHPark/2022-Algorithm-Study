import heapq
def solution(jobs):
    answer=0
    for i in jobs:
        answer+=i[1]
    heap=[]
    curtime=0
    jobs.sort()
    j=0
    while j!=len(jobs) or heap:
        for i in range(j,len(jobs)):
            if jobs[i][0]<=curtime:
                heapq.heappush(heap,(jobs[i][1],jobs[i][0]))
                j+=1
        if not heap and j!=len(jobs):
            heapq.heappush(heap,(jobs[j][1],jobs[j][0]))
            curtime=jobs[j][0]
            j+=1
        li=heapq.heappop(heap)
        answer+=curtime-li[1]
        curtime+=li[0]
    return answer//len(jobs)
