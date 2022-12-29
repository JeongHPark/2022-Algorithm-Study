def solution(word):
    li = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    e = [781,156,31,6,1]
    answer = 0
    count = 0
    for i in word :
        answer += li[i] * e[count]
        answer += 1
        count += 1

    return answer
