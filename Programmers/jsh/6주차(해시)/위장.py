def solution(clothes):
    answer = 1
    dicts={} #딕셔너리선언
    for i in clothes: #같은종류의 옷 수 계산
        if i[1] not in dicts:
            dicts[i[1]]=1
        else:
            dicts[i[1]]+=1
            
    li=list(dicts.values()) #value값들만 리스트로 변환
    for i in li:
        answer*=i+1 #어떤 옷을 입지않는경우까지 1가지의 경우의수로 포함하여 모든 경우의수를 구함
    return answer-1 #모두 안입는 경우의수 1 제외(1개이상의 옷을입어야함)
