from collections import defaultdict
def solution(fees, records):
    answer = []
    cartime={}
    cartimesum=defaultdict(int)
    carlist=set()
    for i in records:
        time,num,io=i.split(" ")
        num=int(num)
        carlist.add(num)
        time=int(time[0:2])*60+int(time[3:5])
        if io=="IN":
            cartime[num]=time
        else:
            cartimesum[num]+=time-cartime[num]
            cartime[num]=-1
    for i in carlist:
        fee=0
        if cartime[i]!=-1:
            cartimesum[i]+=23*60+59-cartime[i]
        if fees[0]>=cartimesum[i]:
            fee=fees[1]
        elif (cartimesum[i]-fees[0])%fees[2]==0:
            fee=fees[1]+(cartimesum[i]-fees[0])//fees[2]*fees[3]
        else:
            fee=fees[1]+((cartimesum[i]-fees[0])//fees[2]+1)*fees[3]
        answer.append([i,fee])
    answer.sort()
    return [i[1] for i in answer]
