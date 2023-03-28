'''
운영체제 스케줄링을 방식을 생각하여 강의실이 부족할 때마다 새로운 강의실(스레드를 만들어준다 생각)을 만들어주며 스케줄링해주는 방법을 생각하여 처음에는 다음과 같이 생각하였다.
아래 두번째 for문을 통하여 순회하며 각 강의실에서 수업이 가능한지 여부를 판단하였다.
for i in arr :
    if len(m) == 0 :
        m.append(i[1])
        continue
    check = 0
    for j in range(len(m)) :
        if m[j] <= i[0] :
            m[j] = i[1]
            check = 1
            break
    if check == 0 : m.append(i[1])
그러나 n = 200,000으로 시간초과가 발생하였고 해당 문제를 순회에서 줄여야한다고 생각하여 순회가 아닌 강의실 목록 중 가장 작은 값을 찾는 방법을 생각해내야했다.
더 낮은 비용으로 가장작은 값을 찾기위해 힙 자료구조를 사용하여 탐색을 n에서 2logn으로 줄여 시간초과를 해결하였다.
'''
import sys
import heapq

n = int(input())

arr = []

for i in range(n) :
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort()
m = []
for i in arr :
    if len(m) == 0 :
        heapq.heappush(m, i[1])
        continue
    min = heapq.heappop(m)
    if min <= i[0] :
        heapq.heappush(m, i[1])
    else :
        heapq.heappush(m, min)
        heapq.heappush(m, i[1])

print(len(m))
