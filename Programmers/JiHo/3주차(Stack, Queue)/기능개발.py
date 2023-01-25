'''
day를 계속 최대걸린 날짜로 계속 유지하며 나머지 개발일수를 비교하여 한번에 출시하는 날짜를 합친다.
시간복잡도 O(N)
'''
import math

def solution(progresses, speeds):
    answer = []
    day = math.ceil((100 - progresses[0]) / speeds[0]) # 1//100과 같이 0.1같이될 경우 -> 올림(ceil)로 처리
    counter = 1
    for i in range(1, len(progresses)) :
        temp = math.ceil((100 - progresses[i]) / speeds[i]) #다음 개발 소요시간 계산 후 임시 저장
        if temp <= day : #소요시간이 이전 항목의 출시일 수보다 적으면(이미 완료된 개발이면)
            counter += 1 #누적 출시를 하나 추가
        else : #조금더 소요시간이 필요할때
            answer.append(counter) #출시를 정답 리스트에 추가
            counter = 1 #누적 출시를 1로 초기화
            day = temp #day를 오래걸리는 개발일수로 초기화 시켜줌
    answer.append(counter) #마지막 요소를 정답 리스트에 추가해줌
            
    return answer