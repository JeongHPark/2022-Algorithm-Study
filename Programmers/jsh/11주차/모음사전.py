#경우의수가 최대6^5이므로 다중for문을 사용해도 무방하므로
#모든경우를 계산하여 해결함
def solution(word):
    answer = 0
    lists=['A','E','I','O','U']
    for i in lists:
        temp=['x','x','x','x','x']
        temp[0]=i
        answer+=1
        if word=="".join(temp[:1]):
            return answer
        for j in lists:
            temp[1]=j
            answer+=1
            if word=="".join(temp[:2]):
                return answer
            for k in lists:
                temp[2]=k
                answer+=1
                if word=="".join(temp[:3]):
                    return answer
                for l in lists:
                    temp[3]=l
                    answer+=1
                    if word=="".join(temp[:4]):
                        return answer
                    for q in lists:
                        temp[4]=q
                        answer+=1
                        if word=="".join(temp[:5]):
                            return answer
                        
    return answer
