def solution(board, moves):
    baguni = []
    for i in moves :
        count = 0 #열을 기준으로 뽑기하기때문에 행을 순환하기 위한 변수
        while len(board) > count :
            if board[count][i - 1] != 0: #0일 경우 빈칸이므로 다음칸 탐색
                baguni.append(board[count][i - 1])
                board[count][i - 1] = 0
                break
            count += 1
    stack = []
    answer = 0
    for j in baguni : #바구니에서 하나씩 꺼내면서 검사
        if stack : #스택에 아무것도 없으면 언더플로우발생함
            temp = stack.pop()
            if temp != j : #이전 인형이 같은 인형이 아닐경우
                stack.append(temp)
                stack.append(j)
            else : #이전 인형이 같은인형일경우
                answer += 2
        else :
            stack.append(j)
    return answer
