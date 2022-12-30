from itertools import product

def solution(word) :
    result=0
    words = ['A', 'E', 'I', 'O', 'U']
    arr = []
    for i in range(1, 6) :#모든 조합 구하는 과정
        tmp=list(map("".joiㅁn, product(words, repeat=i))) #이 메소드(product)의 특징은 두 개 이상의 리스트의 모든 조합을 구할 때 사용된다.
        arr+=tmp
        if tmp==word:
            break;
    arr.sort()
    for i in arr:
        result+=1
        if i==word:
            return result
