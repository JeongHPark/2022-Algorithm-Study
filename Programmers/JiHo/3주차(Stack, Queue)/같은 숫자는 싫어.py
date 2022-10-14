#시간복잡도O(n)
def solution(arr):
    count = 0
    answer = [] #스택선언
    answer.append(arr.pop(0)) #스택 첫번째 값입력
    for i in arr : #arr순회
        if answer[count] != i : #이전에 들어간 요소가 동일한요소가 아니면 추가
            answer.append(i)
            count+= 1 #마지막값 접근을 위한 count 변수
        
    return answer