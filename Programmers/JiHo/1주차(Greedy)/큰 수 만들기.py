#시간복잡도 O(n^2)
def solution(number, k):
    k = len(number) - k # K수만큼제거 -> K만큼 수를 선택
    answer = ''
    max_index, search_index = 0, 0
    while k > 0 : #K만큼 수를 선택
        max = 0
        for i in range(search_index, len(number) - k + 1) : #시작점(가장큰수 다음)~끝점(선택할수있는범위)까지 탐색
            if max < int(number[i]) : #큰값을 찾으면
                max, max_index = int(number[i]), i #큰값의 인덱스, 값 저장
                if max == 9 : break #테스트케이스 8,10 해결
        search_index = max_index + 1 #다음 시작점 설정
        answer += str(max)
        k -= 1 
    return answer