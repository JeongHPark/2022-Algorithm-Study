def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)] 
    for i in range(n): # visited값에 0이 있을 시 anwer +=1 해주고 bfs 돌리기
        if visited[i]==0:
            queue=[i]
            visited[i]=1
            while queue:
                v=queue.pop(0)
                for j in range(n):
                    if visited[j]==0 and computers[v][j]==1:
                        queue.append(j)
                        visited[j]=1
            answer+=1 
                    
    return answer    
