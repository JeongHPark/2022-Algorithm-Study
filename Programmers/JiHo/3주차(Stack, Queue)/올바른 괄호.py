'''
시간복잡도 O(N)
고려해야하는 요소가 '('또는')' 두개뿐이므로 직접 요소를 저장할 필요가 없다고 생각 -> 정수형으로 저장
( = -1, ) = +1으로 저장할 경우 ()와 같이 정확하게 닫혔을때 0
())와 같이 괄호가 닫히지 않았을 때 0보다 커지게 됨
'''
def solution(s):
    stack = 0 #상태저장용 스택
    for i in s :
        if i == "(" : stack -= 1 # (이면 -1
        elif i == ")" : stack += 1 # )이면 +1
        if stack > 0 : return False #매번 요소마다 stack이 0을 넘는지 확인
    if stack != 0 : return False #모든요소 검사시 열려있는 괄호가 있는지 확인
    return True #위에서 안걸렸을경우 정상괄호
