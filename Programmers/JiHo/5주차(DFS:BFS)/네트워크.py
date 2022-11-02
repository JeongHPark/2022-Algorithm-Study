from collections import deque

def solution(n, computers):
    visited = [0 for i in range(n)]
    que = deque()
    answer = 0
    for j in range(n) :
        if visited[j] == 1 : continue #이미 탐색한 노드일경우 다음노드
        que.append(j) #탐색하지 않았을경우 큐에 노드 넣음
        visited[j] = 1
        while que: #BFS탐색
            temp = que.popleft()
            for i in range(n) :
                if computers[temp][i] == 1 and visited[i] == 0 :
                    visited[i] = 1
                    que.append(i)
        answer += 1
    return answer