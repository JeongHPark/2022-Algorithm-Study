import heapq
import sys
input=sys.stdin.readline
n = int(input())
time = []
for i in range(n):
    time.append(list(map(int, input().split())))
time.sort()
heap = []
maxs = 1
for i in range(n):
    while heap and heap[0][0] <= time[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, [time[i][1], time[i][0]])
    maxs = max(maxs, len(heap))
print(maxs)
