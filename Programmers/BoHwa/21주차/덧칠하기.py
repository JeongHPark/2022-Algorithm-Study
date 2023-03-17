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


'''
다른 풀이
참고 : https://comdoc.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8D%A7%EC%B9%A0%ED%95%98%EA%B8%B0
'''
def solution(n, m, section):
    answer = painted = 0
    for s in section:
        if s>=painted:
            answer+=1
            painted=s+m
    
    return answer
