#현재배열의 max인값을 찾아 그전에사둔 주식들을 모두 매도
#다시 그이후의 max 값을 찾아 반복함
t=int(input())
for i in range(t):
    n=int(input())
    day=list(map(int,input().split()))[::-1]
    answer=0
    maxidx=len(day)
    while maxidx!=0:
        day=day[:maxidx]
        maxidx=day.index(max(day))
        for j in day[maxidx+1:]:
            answer+=day[maxidx]-j
    print(answer)
