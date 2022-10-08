'''
시간복잡도 : O(n^2)
제너레이터는 yield = return과 같이 작동하며 실행시 yield에서 next()실행시까지 대기하게된다.
'''
def supo_1() :#제너레이터1
    count = 0
    while True : 
        count = (count % 5) + 1
        yield count
def supo_2() :#제너레이터2
    tem = [1,3,4,5]
    count = 0
    while True :
        yield 2
        yield tem[count]
        count = (count + 1) % 4
def supo_3() :#제너레이터3
    temp = [3,1,2,4,5]
    coun = 0
    while True : 
        yield temp[coun]
        yield temp[coun]
        coun = (coun + 1) % 5
def solution(answers):
    s1, s2, s3 = supo_1(), supo_2(), supo_3() #제너레이터 사용
    answer = [0,0,0]
    for i in answers : #정답을 순환하며 개수파악
        if i == next(s1) : answer[0] += 1
        if i == next(s2) : answer[1] += 1
        if i == next(s3) : answer[2] += 1
    temp = max(answer)
    answer_max = []
    for i in [0,1,2] : #max와 맞은 개수인 요소를 추가
        if answer[i] == temp : answer_max.append(i + 1)
    return answer_max