def solution(progresses, speeds):
    answer = []
    progresses_day=[] #걸리는 시간 기록 리스트
    for i in range(len(progresses)):#걸리는 시간 계산 후 리스트에 넣는 과정
        if (100-progresses[i])%speeds[i]==0:
            progresses_day.append((100-progresses[i])/speeds[i])#나누어 떨어지기 때문에 / 하나 사용
        else :
            progresses_day.append((100-progresses[i])//speeds[i]+1)#나누어 떨어지지 않기 때문에 / 두개 사용
    check=[num * 0 for num in progresses_day]#리스트길이만큼 0으로 초기화
    for i in range(len(progresses_day)):
        stack=0#앞에서 뒤에 같은 작업날에 낼 수 있는 지 쌓아주는 stack값
        if check[i]==0:#작업물 안 냈으면 진행 
            #원래는 i값을 j+1값으로 변경하는  과정으로 진행할려했으나 for문안에서 i값을 변경하는 식을 넣어도 반영이 안 되어 이 방법을 사용.안 됐던 코드 밑에 첨부
            #https://github.com/shindudwns/Programmers/blob/main/Stack%20and%20Que/%EA%B8%B0%EB%8A%A5%EA%B0%9C%EB%B0%9C(i%EA%B0%92%20%EB%B3%80%EA%B2%BD%20%EC%95%88%EB%90%A8).py
            for j in range(i+1,len(progresses_day)):
                if progresses_day[i]>=progresses_day[j]:
                    stack+=1
                    check[j]=1#작업물 냈다는 뜻
                else:
                    break
            answer.append(stack+1)#progresses_day[i]값 자신도 내기 때문에 stack+1
    return answer
