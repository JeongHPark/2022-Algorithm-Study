def solution(number, k):
    answer = ''
    sl=list(number)# 각각 나눠줌
    stack=len(sl)-k
    index=-1
    value=sl[0]
    while stack != 0 and index<len(sl):
        index+=1
        max_index=index
        max_value=sl[max_index]
        stack-=1 
        if len(sl)-index!=stack :
            for i in range(index,len(sl)-stack):          #잘랐을 때 사용 할 수 있는 수들 중 제일 큰 값과 그 인덱스 저장
                        if max_value<sl[i]:
                            max_value=sl[i]
                            max_index=i 
                            if max_value == 9 : 
                                break
            index=max_index
            answer+=max_value
        else : # 남은 stack 수와 남은 index값이 같으면 남은값들 다 더하고 while문 나가기
            answer+=sl[index:]
            break
    return answer
