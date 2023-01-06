'''
그래프 문제이므로 배열또는 사전자료형 사용
여기선 원소가 string이므로 dictionary 사용
양방향 그래프가 아닐수도 있기때문에 모든경우를 탐색해야함(DFS)
순서에따라 경유하지 못하는 공항이 생길수있음
-------------------------------------------------------------------
defaultdict을 사용시 dict의 기본값을 설정할수있음
dict,list는 매개변수로보낼때 얕은복사 또는 깊은복사 해야함(하지않을 경우 메모리를 공유하기때문)
list.copy() or copy.deepcopy(list) 깊은복사는 2차원이상 리스트일경우
'''
from collections import defaultdict
import copy
def solution(tickets):
    destination=defaultdict(list)
    for i in tickets:
        destination[i[0]].append(i[1])
        destination[i[0]].sort()
    def dfs(start,answer,dest):
        answer.append(start)
        if len(answer)==1+len(tickets):
            return answer
        for i in range(len(dest[start])):
            temp=dest[start].pop(i)
            ret=dfs(temp,answer.copy(),copy.deepcopy(dest))
            dest[start].insert(i,temp)
            if ret:
                return ret
    return dfs("ICN",[],copy.deepcopy(destination))
