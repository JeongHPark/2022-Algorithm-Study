def solution(n, computers):
    answer = 0
    visit=[]
    stack=[]
    while len(visit)!=n: #모두 방문할때까지 반복
        for i in range(n):
            if i not in visit:  #방문하지않은 n값을 찾아서 스택의 첫번째에넣어줌
                stack.append(i)
                visit.append(i)
                break
        while stack: #스택이빌때까지
            for i,value in enumerate(computers[stack.pop()]): #bfs방식(방문순서는 무시 오로지 네트워크의 개수 판별용)
                if i not in visit and value==1:
                    visit.append(i)
                    stack.append(i)
        answer+=1 #네트워크의 수 증가
    return answer
