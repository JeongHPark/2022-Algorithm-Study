def solution(array, commands):
    answer = []
    for i in range(len(commands)):#총 commands[i][j]의 i갯수만큼 돌림 
        arr = [] # 자른 길이만큼 저장할 리스트
        for j in range(commands[i][0]-1,commands[i][1]) : # 길이에 맞게 잘라줌
            arr.append(array[j])# 리스트에 값 추가
        arr.sort()#정렬
        answer.append(arr[commands[i][2]-1])#답 리스트에 추가 
    return answer
