#시간복잡도 O(nlogn)
def solution(array, commands):
    answer = []
    for i in commands : #명령어를 하나씩 뺴옴
        temp = array[i[0]-1:i[1]] #문자열 슬라이싱으로 잘라줌
        temp.sort() #정렬
        answer.append(temp[i[2]-1]) #정답을 answer에 추가
    return answer