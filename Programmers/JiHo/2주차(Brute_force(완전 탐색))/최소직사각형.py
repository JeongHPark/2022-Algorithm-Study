#시간복잡도 O(n) : 최댓값을 위한 순차탐색으로 인한 O(n)시간 소요
def solution(sizes):
    max_l, max_r = -1, -1 #가로, 세로 최댓값 저장
    for i in sizes : #모든 명함 크기를 순회
        if i[0] < i[1] : i[0], i[1] = i[1] , i[0] #가로부분이 긴 길이가 되도록 명함을 회전시킴 (가로>세로 형태)
        if i[0] > max_l : max_l = i[0] #가로 최대값 저장
        if i[1] > max_r : max_r = i[1] #세로 최대값 저장
    answer = max_l * max_r #최대값을 바탕으로 지갑크기 계산
    return answer