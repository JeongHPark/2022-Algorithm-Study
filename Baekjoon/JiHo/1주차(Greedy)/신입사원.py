'''
시간 복잡도 O(nlogn) -> sort사용으로 인한
서류 성적으로 정렬할 경우 비교할 대상이 하나 줄어 들기 때문에
면접 성적으로 비교하여 비교적 쉽게 비교가능하다.
'''
import sys #빠른 입출력을 위한 sys.stdin.readline사용

n = int(input())

for i in range(n) :
    m = int(input())
    score = []
    for j in range(m) :
        score.append(list(map(int, sys.stdin.readline().split()))) #2차원 배열로 저장[서류 성적, 면접 성적]
    score.sort(key=lambda x:x[0]) #서류 성적 기준으로 정렬
    num = 1 #서류성적 1등은 무조건 합격이므로 카운트
    score_max = score[0][1] #서류성적 1등의 면접 성적으로 초기화
    for i in score[1:] : #서류1등 이후 인원들 비교
        if score_max > i[1] : #이전 맥스값보다 더 성적이 좋을경우만 합격
            score_max = i[1] #맥스값을 더 좋은 성적으로 초기화
            num+=1 #합격자추가
    print(num)