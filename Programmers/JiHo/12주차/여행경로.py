#dfs를 이용한 풀이
#dfs로 들어가되 끝까지 안되면 안되었던데로가서 다시 돌아가서 탐색
#즉 dfs로 더욱 갈곳이 없을시(전체를 돌지않았는데 = (count != 0)) 이전 탐색노드로 돌아서와서 다른 공항으로 dfs (모든 도시를 방문할 수 없는 경우가 없으므로 가능)
# 알파벳 순서가 앞으로서는 경로 : sort를 이용하여 정렬 후 선택으로 해결

from collections import deque

def dfs(start, tickets, visit, count, answer):
    answer.append(start)
    if count == 0 : return 0, answer
    for i in range(len(tickets)) :
        if start == tickets[i][0] :
            if visit[i] == 0 :
                visit[i] = 1
                check, answer = dfs(tickets[i][1], tickets, visit, count - 1, answer)
                if check == 0 : return 0, answer #check가 0인 경우 최종까지 도달한 경우로 바로 리턴
                visit[i] = 0 #visit를 초기화하고 다른 노드를 탐색
    answer.pop() #해당 시작지부터 전체노드가 불가능할 경우 answer 제외한후 리턴(이전공항으로 이동전 초기화)
    return 1, answer #이전공항으로 이동

def solution(tickets):
    qu = deque(tickets[0])
    start = "ICN"
    visit = [0 for i in range(len(tickets))]
    tickets.sort()
    
    count = len(tickets)
    count, answer = dfs(start,tickets,visit,count, [])
    
    return answer
