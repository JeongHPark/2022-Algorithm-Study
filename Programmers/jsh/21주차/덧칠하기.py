def solution(n, m, section):
    paint=[1]*n
    answer = 0
    for i in section:
        paint[i-1]=0
    for i in range(n):
        if paint[i]==0:
            for j in range(i,i+m):
                if j==n:
                    return answer+1
                paint[j]=1
            answer+=1
    return answer
