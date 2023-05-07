from heapq import heappush,heappop

def solution(n, s, a, b, fares):
    answer = 20000001
    res=[[]]

    graph=[[] for _ in range(n+1)] #n개의 노드 수만큼 만들기
    
    def dijkstra(start):
        res=[float('inf') for _ in range(n+1)]
        q=[]

        heappush(q,(0,start))
        res[start]=0
        while(q):
            fare,node=heappop(q) #요금과 노드

            for next_f,next_n in graph[node]: #현재 노드와 연결된 노드들의 (요금, 노드)
                if fare+next_f < res[next_n]:#다음 노드로 가는 요금이 저장된 요금보다 싼 경우 갱신 후 heap에 넣기
                    res[next_n]=fare+next_f
                    heappush(q,[res[next_n],next_n]) #지금까지 거쳐온 노드의 요금과 다음 노드의 요금 합
                
            
        return res


    for i,j,k in fares: #각 노드와 (요금,연결된 노드)를 graph에 저장하기
        graph[i].append((k,j))
        graph[j].append((k,i))

    for i in range(1,n+1): #각 노드에서 출발할 때 가장 최소 요금
        res.append(dijkstra(i))
        
        
    for i in range(1,n+1):#s에서 i로 i에서 a, i에서 b로 가는 경우를 더해서 가장 택시요금이 낮은 경우를 반환
        answer=min(answer,res[s][i]+res[i][a]+res[i][b])
    
    return answer
        
