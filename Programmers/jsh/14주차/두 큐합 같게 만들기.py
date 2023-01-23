'''
두개의 큐를 합친후 투포인터를 활용하여 전체 합의 절반값이 나올때까지 더하고 뺌
ex)[3,2,7,2,4,6,5,1]
start=0
end=3
1. 처음 4개합친값이 14이므로 절반값 15보다 작음 end를 1증가(queue2에서 queue1에 값을 넘겨준 것과 같음)
2. 14+4=18 이므로 값을 줄이기위해 start 1감소(queue1 에서 queue2로 값을 넘겨준것과같음)
3. 18-3=15 15가나왔으므로 종료
'''
def solution(queue1, queue2):
    answer = -1
    cnt=0
    sumdata=sum(queue1)+sum(queue2)
    if sumdata%2!=0: #2로 안나눠지면 종료
        return -1
    sumdata=sumdata//2
    start=0
    end=len(queue1)-1
    temp=sum(queue1)
    queues=queue1+queue2
    while start<=end: # 투포인터 활용
        if temp<sumdata:
            end+=1
            if end<len(queues): #인덱스 초과 오류가 떠서 if문 추가
                temp+=queues[end]
                cnt+=1
            else:
                break
        elif temp>sumdata:
            temp-=queues[start]
            start+=1
            cnt+=1
        else:
            answer=cnt
            break
    return answer
