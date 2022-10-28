'''
BFS를 사용하여 풀이하였습니다.
시간복잡도 O(n^2)
큐를 사용하기 위해 deque를 사용
'''
from collections import deque

n = int(input())
v = int(input())

l = [[0]* n for i in range(n)]
vistied = [0 for i in range(n)]

for i in range(v) : #간선정보를 인접행렬로 바꿈
    a,b = map(int, input().split())
    l[a-1][b-1] = l[b-1][a-1] = 1

que = deque([1]) #시작점을 미리 큐에 넣어놓음
vistied[0] = 1 

while len(que) != 0 : #큐가 다 비워지면 종료
    temp = que.popleft() #다음 탐색 노드를 temp에 저장
    for i in range(n): #해당 노드와 연결된 노드들은 확인
        if l[temp - 1][i] == 1 and vistied[i] == 0 : #연결된 노드들이 방문했는지 체크
            que.append(i + 1) #방문안했다면 다음 방문을 위해 큐에 저장
            vistied[i] = 1 #방문체크

print(sum(vistied) - 1) #visited에 체크된 노드의 수 = 감염된 노드의 수