def solution(n, computers):
    answer = 0
    visit=[]
    stack=[]
    while len(visit)!=n:
        for i in range(n):
            if i not in visit: 
                stack.append(i)
                visit.append(i)
                break
        while stack:
            for i,value in enumerate(computers[stack.pop()]):
                if i not in visit and value==1:
                    visit.append(i)
                    stack.append(i)
        answer+=1
    return answer
