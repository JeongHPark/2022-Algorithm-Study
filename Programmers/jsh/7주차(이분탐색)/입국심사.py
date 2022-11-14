def checktime(n,time,times):
    #시간이 주어 졌을때 그시간안에 n명이상을 볼수있는지 확인
    cnt=0
    for i in times:
        cnt+=time//i #모든 심사관이 각각 시간안에 몇명을 볼수있는지 카운트
    return n<=cnt
def solution(n, times):
    answer = 0
    count=0
    maxvalue=max(times)
    if n%len(times)==0: #대기하는사람수/심사관수 몇번 반복해야하는지
        count=n//len(times)
    else:
        count=(n//len(times))+1
    maxtime=maxvalue*count #최대 걸리는 시간(maxvalue보다 많이걸릴수는없다)
    #이분탐색 시작
    #시간으로 이분탐색을하여 시간안에 n명이상을 받을수있는지 확인
    st=1
    en=maxtime
    while st<en:
        if checktime(n,(st+en)//2,times):
            en=(st+en)//2
        else:
            st=(st+en)//2+1
    return st
