def solution(N, number):
    if N==number:
        return 1
    dp=[set() for _ in range(9)] #중복제거를위한 집합선언
    dp[1].add(N)
    for i in range(2,9):        
        #사칙연산 말고도 5,55 처럼 붙여쓰는것도가능하기때문에
        dp[i].add(int(str(N)*i))
    # N의개수가 1일때부터 8일때까지 모든경우의수를구해서 number와 비교
    for i in range(2,9):
        for j in range(1,i):
            for k in dp[i-j]:
                for l in dp[j]:
                    if l!=0:
                        dp[i].add(k//l)
                    dp[i].add(k*l)
                    dp[i].add(k-l)
                    dp[i].add(k+l)
        if number in dp[i]:
            return i
    return -1 #N의개수가 9개이상 필요할때 -1리턴
