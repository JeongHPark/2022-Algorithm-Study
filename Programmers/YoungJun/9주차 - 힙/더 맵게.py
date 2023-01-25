#계속된 시간초과로 해결하지 못하여 인터넷에서 검색하여 heapq를 이용하여 해결하였습니다.

import heapq

def solution(scoville, k):
    answer = 0
    scoville.sort()
    
    while scoville[0]<k :
        if len(scoville) <= 1:
            return -1
        else:
            small = heapq.heappop(scoville)
            small2 = heapq.heappop(scoville)
            heapq.heappush(scoville, (small + (small2 * 2)))
            answer+=1
        
    return answer
