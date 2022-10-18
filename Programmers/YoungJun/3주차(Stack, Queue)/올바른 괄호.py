def solution(s):
    stack = 0 # ( 부호면 증가 ) 부호면 마이너스를 쌓기 위한 변수
    for i in s:
        if s[i] == '(':# ( 부호면 증가
            stack+=1
        else :# ) 부호면 마이너스
            if stack<1:#1보다 작으면 탈락
                return False
            else :
                stack-=1
    if stack!=0 :#0이 아니면 탈락
        return False
    return True
