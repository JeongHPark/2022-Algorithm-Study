import heapq #우선순위 큐
def solution(scoville, K):
    answer=0
    heapq.heapify(scoville) #리스트를 최소힙 형태로 변환
    while scoville[0]<K: #top에 있는 수가 k이상이면 모든원소가 k이상이므로
        if len(scoville)==1:
            return -1
        #두개를 pop하여 계산후 다시 push해줌
        heapq.heappush(scoville,heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        answer+=1
    return answer
