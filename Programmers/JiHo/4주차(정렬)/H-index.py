'''
citations = [3, 5, 2, 4, 1]
citations.sorted(reverse = True) = [5, 4, 3, 2, 1]
h-index = 2, 5개의 논문중 2번 인용된 논문이 2편이상 -> O
h-index = 3, 5개의 논문중 3번 인용된 논문이 3편이상 -> O
h-index = 4, 5개의 논문중 4번 인용된 논문이 4편이상 -> X
오름차순으로 정렬 후 인덱스h를 0부터 증가시키며(h편이상을 확인), 해당 인덱스의 요소를 확인(h번 인용됬는지 확인)한다.
즉, h-index = 2일때 h = 1, [5, |4| 3, 2, 1] | |이 존재하는 곳의 요소가 h보다 크거나 같다면 오름차순정렬로 인해(이전의 요소들은 해당 인덱스요소보다 크기때문)
h-index가 가능한지 체크하게된다.
'''
def solution(citations):
    citations.sort(reverse = True)
    h = 0
    for i in citations : #citations 요소 수만큼 순환
        if citations[h] <= h : return h #h-index가 가능한지 체크, 안되면 리턴(배열시작번호 차이로 이전의 h-index가 가능한 h로 리턴)
        h += 1 #h-index로 가능하다면 다음인덱스를 확인
    return h