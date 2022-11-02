from collections import deque

n, m, v = map(int, input().split())

#그래프 간선 정보 -> 인접행렬로 변경
nod = [[0] * (n+1) for i in range(n+1)] #노드수 + 1로 배열을 만듬으로 1 -> 0으로 변환해야하는 소요 제거
for i in range(m) :
    a, b = map(int, input().split())
    nod[a][b] = nod[b][a] = 1

#DFS
def DFS(t) :
    visited[t] = 1 
    print(t, end=" ") #탐색
    for i in range(n+1) : #해당 노드와 연결된 노드를 확인
        if nod[t][i] == 1 and visited[i] == 0 : #연결되어 있다면 해당 노드로 바로 탐색
            DFS(i)

visited = [0 for i in range(n+1)] #DFS를 위한 방문배열 선언
DFS(v) #DFS탐색

print("")

#BFS
que = deque([v]) #큐선언 및 큐에 시작노드 추가
visited = [0 for i in range(n+1)] #BFS를 위해 방문배열 초기화
visited[v] = 1 #큐에 들어간 시작노드 방문표시
while len(que) != 0 : #큐가 비워지면 종료
    temp = que.popleft() #다음 탐색 노드를 temp에 저장
    print(temp, end=' ') #방문노드 출력
    for i in range(n+1) : #해당 노드와 연결된 노드들은 확인
        if nod[temp][i] == 1 and visited[i] == 0: #연결된 노드들이 방문했는지 체크
            visited[i] = 1 #방문체크
            que.append(i) #방문안했다면 다음 방문을 위해 큐에 저장