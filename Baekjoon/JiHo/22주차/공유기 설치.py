'''
접근
이분탐색으로 최소거리를 설정하고 최소거리를 통과 할 수 있는가?
BFS, DFS로 풀이할 수 있지않을까?
이분탐색으로 최소거리를 찾아가는 방법을 사용
즉 최소거리를 임의로 지정하여 가능한지 확인하며 이분탐색으로 최소거리를 계속 추출
이분탐색이 가능한 이유 : 임의지정한 최소거리가 가능하지 않은경우 해당 최소거리보다 작은 경우의 수가 없다.
'''

import sys

n, c = map(int, input().split())

arr = [int(sys.stdin.readline()) for i in range(n)]
arr.sort()
min = 0
ma = arr[len(arr) - 1]
answer = []
while ma >= min :
    cen = (ma + min) // 2 #cen == mid, cen값은 최소거리를 의미한다.
    count = 1 #cen값
    pre = arr[0]
    for i in arr[1:] :
        if i - pre >= cen :
            pre = i
            count += 1
    if count >= c : #설치해야하는 것보다 더많이 설치할 경우 = 가능할 수 있는 최소값일 경우
        answer.append(cen) #가능한 답을 answer에 입력
        min = cen + 1 
    else : #가능하지 않은 최소값일 경우
        ma = cen - 1
        
    
print(max(answer))
