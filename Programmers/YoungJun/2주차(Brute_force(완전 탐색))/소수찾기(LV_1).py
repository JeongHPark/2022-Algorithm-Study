import math

def soutsu(n,ss) : # 소수를 나눴을때 나눠 떨어지지 않으면 소수 판정
    for i in range(0,len(ss)): #소수 리스트 길이만큼 돌리기
        if math.sqrt(n)<ss[i]: # 시간초과가 계속 떠 질문하기 게시판보고 쓴 조건 n의 제곱근보다 작은 소수에서 나눠지지 않으면 소수.
            break
        if n%ss[i]==0 : # 나눠떨어지면 소수 탈락
            return False    
    return True # for문을 빠져나오면 소수 판정
def solution(n):
    ss = []
    answer = 1 # 2이상 값이므로 1로 시작
    for i in range(3,n+1) : # 3부터 돌아가게 구성
        if i%2!=0 :  # 짝수가 아닐때 시작
            if soutsu(i,ss)==True : # 소수를 나눴을때 나눠 떨어지지 않으면 소수 판정
                answer+=1
                ss.append(i) # 소수 리스트에 값 추가
    return answer
