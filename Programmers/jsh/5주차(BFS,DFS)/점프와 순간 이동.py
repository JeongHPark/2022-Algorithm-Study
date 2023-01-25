def solution(n):
    ans = 0 
    '''
    2의제곱수인지 판별(관련 라이브러리가 있는지 찾아보다가 발견)
    비트연산으로 판별 ex)2의제곱수들은 0,10,100,1000 이므로 1작은수와 and연산시 0이됨
    '''
    if not n&(n-1):
        return 1
    while n!=1: #n이 1이될때까지 2로나누거나 1빼기
        if n%2==0:
            n=n//2
        else:
            n=n-1
            ans+=1
    return ans+1
