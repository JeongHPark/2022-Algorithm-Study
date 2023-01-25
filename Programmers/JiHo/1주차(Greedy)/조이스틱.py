#시간복잡도 O(n^2)
def solution(name):
    answer = len(name) - 1 #기본적인 움직임(최대값)

    for i in range(len(name)) : #인덱스 번호 활용을 위해 range사용
        count = 0 # A 연속 카운터
        for j in name[i+1:] : # i다음 칸부터 A연속횟수 저장
            if j == "A" : count += 1
            else : break
        dis = min(i, len(name) - (i + 1 + count)) #연속된 A의 왼쪽,오른쪽 비교
        answer = min(answer, i + len(name) - (i + 1 + count) + dis) #기존의 값과 짧은 곳을 왕복 반복하는 방법 비교 -> 작은값 대입

    for i in name :
        answer += min(ord('Z') - ord(i) + 1, ord(i) - ord('A')) #각 문자간 변경 횟수 추가

    return answer