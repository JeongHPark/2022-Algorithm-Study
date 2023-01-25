'''
처음에는 dfs로 생각하였으나 경우에 따라 여러 선택지 있을경우 불가능하다고 판단하여
bfs탐색을 사용하였다.
즉, 기본적인 bfs를 사용하여 목적지에 도달할 수 있을 경우 happy를 그러지 못한경우 sad를 표현하도록하였다.
시간복잡도 : 구현방식으로 예상불가
'''
import sys
from collections import deque

N = int(sys.stdin.readline())

def bfs():
    while queue :
      v = queue.popleft()
      for k in range(len(arr)) :
        if abs((v[0] - arr[ins + 1][0])) + abs((v[1] - arr[ins + 1][1])) <= 1000 : 
          print("happy")
          return
        if visit[k] == 0 and abs((v[0] - arr[k][0])) + abs((v[1] - arr[k][1])) <= 1000 :
          visit[k] = 1
          queue.append(arr[k])
    print("sad")
              
for i in range(N) :
  ins = int(sys.stdin.readline())
  arr = deque()
  for j in range(ins+2) :
    arr.append(list(map(int, sys.stdin.readline().split())))
  queue = deque([arr[0]])
  visit = [0 for i in range(len(arr))]
  visit[0] = 1
  bfs()
