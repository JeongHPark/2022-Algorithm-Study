def solution(routes):
    li = [0 for i in range(len(routes))]
    check = len(routes)
    answer = 0
    routes.sort()
    #routes.sort(key=lambda x:x[1] - x[0]) 맨처음에 이걸로 시도
    while check != 0 :
        answer += 1
        start = -30001
        end = 30001
        for i in range(len(li)) :
            if li[i] == 0 :
                if routes[i][0] >= start and routes[i][0] <= end:
                    start = routes[i][0]
                    li[i] = 1
                if routes[i][1] >= start and routes[i][1] <= end:
                    end = routes[i][1]
                    li[i] = 1
                if routes[i][0] <= start and routes[i][1] >= end:
                    li[i] = 1
                if li[i] == 1 :
                    check -= 1
    return answer

