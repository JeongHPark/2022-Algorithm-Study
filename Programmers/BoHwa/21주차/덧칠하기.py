def solution(n, m, section):
    answer = 0
    arr=[True]*(n+1)
    for s in section:
        arr[s]=False
    for s in section:
        if arr[s]==False:
            answer+=1
            for i in range(s,s+m):
                if i>n: return answer
                arr[i]=True

    return answer
