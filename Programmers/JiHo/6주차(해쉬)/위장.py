from collections import defaultdict

def solution(clothes):
    clo_list = defaultdict(int)
    for i in clothes :
        clo_list[i[1]] += 1
    
    answer = 1
    for i in clo_list.values() :
        answer *= (i + 1)
    answer -= 1
    return answer