#구현문제 dict로 추천인 연결
def solution(enroll, referral, seller, amount):
    refer={}
    cost={}
    #초기화
    for i in enroll:
        cost[i]=0
    for i,j in zip(enroll,referral):
        refer[i]=j
    for i,j in zip(seller,amount):
        cost[i]+=j*100
    '''
    추천인이 '-' 가나올때까지 추천인을 타고올라가면서 수익을 증가시킴
    '''
    for i,j in zip(seller,amount):
        temp=i
        end=(j*100)//10
        if refer[temp]=='-':
            cost[temp]-=end
        else:
            while refer[temp]!='-':
                cost[refer[temp]]+=end
                cost[temp]-=end
                temp=refer[temp]
                end=end//10
                if end==0:
                    break
            cost[temp]-=end
    answer = []
    for i in cost.items():
        answer.append(i[1])
    return answer
