def solution(n, stations, w):
    answer = 0
    start=1
    i=0
    while start<=n:
        if len(stations)>i and start+w>=stations[i]:
            start=stations[i]+w+1
            i+=1
        else:
            answer+=1
            start+=2*w+1
    return answer
