def solution(number, k):
    answer = ''
    sl=list(number)# 각각 나눠줌
    stack=len(sl)-k  # 길이에서 자를 갯수 k를 뺀 완성하기까지 남은 문자의 수 변수 
    index=-1 #초기값 초기화
    value=sl[0]
    while stack != 0 and index<len(sl): # 추가할 문자가 없으면 나갈때와 문자열길이보다 index값이 같거나 클때를 방지(out of range 대비)
        index+=1 #시작할때 인덱스값 증가 밑에 쓰지않은 이유는 초기값을 -1로 지정했기때문
        max_index=index #밑에서 최고값을 찾기 위한 인덱스 초기값
        max_value=sl[max_index] #밑에서 최고값을 찾기 값 초기값
        stack-=1                                        #문자 완성시 하나씩 빼줌
        if len(sl)-index!=stack :#남은수(stack)와 for문 돌아갈 횟수와 같지 않을때 
            for i in range(index,len(sl)-stack):   #잘랐을 때 사용 할 수 있는 수들 중 제일 큰 값과 그 인덱스 저장
                        if max_value<sl[i]: #최고값보다 해당 값이 더 클때 인덱스값과 최고값 저장
                            max_value=sl[i]
                            max_index=i 
                            if max_value == 9 :  # 최고값이 등장했을때 for문 나가기
                                break
            index=max_index #위에서 나온 최고 인덱스 값 저장
            answer+=max_value # 완성할 문자열에 추가
        else : # 남은 stack 수와 남은 index값이 같으면 남은값들 다 더하고 while문 나가기
            answer+=sl[index:] # 남은 값들 다 추가후 while문 벗어나기
            break
    return answer
