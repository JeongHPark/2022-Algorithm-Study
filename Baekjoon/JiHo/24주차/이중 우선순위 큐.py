#https://an-jiohh.github.io/%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4/baekjoon%20online%20judge/python/BOJ7662/
import sys
import heapq

t = int(input())

for _ in range(t) :
    n = int(input())
    max_heap = []
    min_heap = []
    visited = [False for i in range(n)] #방문한지 저장하는 배열
    for i in range(n) :
        cal = sys.stdin.readline().split()
        if cal[0] == "I" :
            heapq.heappush(max_heap, [-int(cal[1]),i]) #몇번쨰 명령인지 같이저장
            heapq.heappush(min_heap, [int(cal[1]),i])
        elif cal[0] == "D" :
            if len(max_heap) == 0 or len(min_heap) == 0: #힙에 아무것도없으면 다음 명령어 실행
                continue
            if cal[1] == "-1" :
                while min_heap : #pop됬는지
                    temp = heapq.heappop(min_heap)
                    if visited[temp[1]] == False : #다른 힙에서 pop됬는지 확인
                        visited[temp[1]] = True #pop됬다고 체크
                        break
                    else :
                        visited[temp[1]] == False #pop이 된적이 있다면 False로 바꾸고 다음 요소
            elif cal[1] == "1" :
                while max_heap :
                    temp = heapq.heappop(max_heap)
                    if visited[temp[1]] == False : #다른 힙에서 pop됬는지 확인
                        visited[temp[1]] = True
                        break
                    else :
                        visited[temp[1]] == False
    answer = []
    for i in min_heap :
        if visited[i[1]] == False :
            answer.append(i[0])
    if len(answer) == 0 :
        print("EMPTY")
    else :
        print(max(answer), min(answer))
