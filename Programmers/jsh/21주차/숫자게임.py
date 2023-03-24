def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    start=0
    for i in B:
        while start!=len(A) and i<=A[start]:
            start+=1
        if start!=len(A):
            answer+=1
            start+=1
        else:
            break
    return answer
