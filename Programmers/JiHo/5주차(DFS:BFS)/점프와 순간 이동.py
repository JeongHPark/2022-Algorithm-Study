'''
(현재까지 온 거리) x 2 조건으로 이진수를 구하는 과정과 매우 흡사하다고 판단하였다.
맨 처음 풀이에서 스택을 이용하여 풀이하였으나 스택을 개선하지 않는 방법으로 개선하였다.
'''
def solution(n):
    stack = []
    while True : #스택에 이진수 넣기
        stack.append(n % 2)
        n = n // 2
        if n == 0 : break
    ans = 0
    for i in stack :
        if i == 1 : ans += 1

    return ans

'''
개선된 풀이
def solution(n):
    ans = 0
    while n!=0 :
        if n % 2 == 1 : ans += 1
        n = n // 2
    return ans
'''