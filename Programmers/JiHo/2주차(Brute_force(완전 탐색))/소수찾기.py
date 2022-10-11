'''
[itertools]https://docs.python.org/ko/3.8/library/itertools.html
itertools.permutations을 이용하여 순열뽑음 -> 순열이 소수인지 판별
'''
import itertools

def solution(numbers):
    result = []
    for i in range(1,len(numbers)+1) : #1~numbers의 길이의 순열을 뽑음
        result += (list(map(int, map(''.join, itertools.permutations(numbers,i))))) #number->순열(튜플)->순열 문자열->순열 숫자
    answer = 0
    result = set(result) #중복제거
    for i in result :
        answer += check_num(i) #체크함수에 넣어서 판별
    
    return answer

def check_num(num) : #소수판별함수
    if num == 0 or num == 1 : return 0 
    for i in range(2, int(num**0.5) + 1)  : #소수2 ~ num + 1의 제곱근까지 비교
        if num % i == 0 : return 0 
    return 1