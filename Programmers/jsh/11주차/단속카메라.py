def solution(routes):
    answer = 0
    routes.sort()
    while routes:
        temp=routes.pop(0)
        start=temp[0]
        end=temp[1]
        #카메라 한대로 같이 찍을수있는 차량들 모두 pop
        while routes and start<=routes[0][0]<=end:
            temp=routes.pop(0)
            start=temp[0]
            if end>temp[1]:
                end=temp[1]
        answer+=1
    return answer
