def solution(name):
    answer = len(name) - 1 #기본적인 움직임(최대값)

    for i in range(len(name)) : #인덱스 번호 활용을 위해 range사용
        count = 0 # A 연속 카운터
        for j in name[i+1:] : #
            if j == "A" : count += 1
            else : break
        dis = min(i, len(name) - (i + 1 + count))
        answer = min(answer, i + len(name) - (i + 1 + count) + dis)

    for i in name :
        answer += min(ord('Z') - ord(i) + 1, ord(i) - ord('A'))

    return answer

name = "A"
print(solution(name))

print(name[100:])