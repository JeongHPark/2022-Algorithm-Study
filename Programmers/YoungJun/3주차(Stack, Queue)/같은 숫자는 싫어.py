def solution(arr):
    answer = [arr[0]]#초기값 arr 처음값
    memory = arr[0]#전 값 초기값을 arr 처음값
    for i in range(1,len(arr)):#초기값부터 길이까지
        if(memory!=arr[i]):#전 값이 다르면 저장
            answer.append(arr[i])
            memory=arr[i]# 전 값
    return answer
