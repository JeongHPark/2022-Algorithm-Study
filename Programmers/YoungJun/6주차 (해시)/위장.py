def solution(clothes):
    dic = {}
    answer = 1
    for i in clothes:
        key = i[1] # 키값 value 값 구분
        value = i[0]
        if key in dic:#값 추가
            dic[key].append(value) 
        else:
            dic[key] = [value]
    for key in dic.keys():
        answer = answer * (len(dic[key]) + 1) # 안입는 경우의 수를 위해 +1
    return answer - 1
