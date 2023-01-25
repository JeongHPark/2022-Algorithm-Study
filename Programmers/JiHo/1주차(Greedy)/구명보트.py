'''
2인용 구명보트 -> 투포인터를 사용하여 구명보트에 태울수있는 짝을 찾는 방법사용
그리디 사용가능한 이유 -> 2인용 구명보트이기 때문에 최대무게가 아닌 최대한 많은 짝을 만드는 것이 목표이며
정렬이후 그리디 알고리즘에 의해 가장 높은 몸무게를 선택하면 나머지 짝이 가능한지 여부를 바로 판별할 수 있어 그리디 사용가능하다.
시간복잡도 O(nlogn) sort로 인한
'''
def solution(people, limit):
    answer = 0 # 구명보트 카운터
    people.sort(reverse=True) #내림차순으로 정렬
    start, end = 0, len(people) - 1 #투포인터 사용(deque.pop를 고민하였지만 시간복잡도문제로 인덱스 접근 사용)
    while start <= end : #포인터만났을때 종료
        if start == end : #마지막에 한명만 남았을때 -> 한명만 구명보트
            answer += 1
            break;
        elif people[start] + people[end] <= limit : #가장 큰 몸무게, 가장 작은몸무게가 짝이가능한지 판별
            start, end = start + 1, end - 1
            answer += 1
        else : #짝이 불가할때 -> 큰 몸무게 한명만 구명보트
            start += 1
            answer += 1
    return answer