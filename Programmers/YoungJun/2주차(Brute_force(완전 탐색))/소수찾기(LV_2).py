#순열 부분과 순열된 값을 리스트에 넣는 방법을 해결할 수 없어 인터넷을 참고했다.

import itertools# 순열을 쓰기위한 라이브러리
import math # 제곱근을 쓰기위한 라이브러리

def soutsu(n): # 소수 확인 부함수
    if n < 2:  # 0 , 1 값이면 바로 탈락                    
        return False         
    for i in range(2, int(math.sqrt(n))+1): # 제곱근수보다 1이 큰 경우까지 
        if n % i == 0: # 나눠떨어지면 소수 탈락
            return False   
    return True # 여기까지 오면 통과

def solution(numbers):
    answer = 0 
    arr = [] #순열을 저장할 리스트
    for i in range(1,len(numbers)+1): # 끊을 수 있는 숫자의 갯수가 한 개부터 다 합친 갯수이기에 for문은 해당값 -1값까지만 돌기에 1을 추가하였다.(참고부분)
        arr += itertools.permutations(numbers, i) # 순열 저장 과정(참고부분)
    num = set([int(''.join(i)) for i in arr]) # 순열을 각각 합쳐주는 과정(참고부분)
    for i in num: # 순열 수만큼 돌리기
        if soutsu(i) :# 참이면
            answer+=1 #값 더해주기
    return answer
