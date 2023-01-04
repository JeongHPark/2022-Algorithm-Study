import sys

t = int(input())

sys.setrecursionlimit(10**6) #재귀 제한을 풀어주는 함수

x_count = [0, -1, 0, 1]
y_count = [-1, 0, 1, 0]

def dfs(y, x) : #깊이 우선탐색을 이용하여 주변 위치 탐색
    for i in range(4) :
        if all([y + y_count[i] >= 0, y + y_count[i] < n, x + x_count[i] >=0, x + x_count[i] < m]) :
            if li[y + y_count[i]][x + x_count[i]] == 1 :
                li[y + y_count[i]][x + x_count[i]] = 2 #탐색한 위치를 2로 표시
                dfs(y + y_count[i],x + x_count[i])


for i in range(t) :
    count = 0
    m,n,k = map(int, input().split())
    li = [[0] * m for i in range(n)]
    for i in range(k) :
        x, y = map(int, input().split())
        li[y][x] = 1

    for i in range(n) :
        for j in range(m) :
            if li[i][j] == 1 : #탐색안한 위치이면 탐색
                li[i][j] = 2
                count += 1 #탐색시작하므로, 즉 하나의 덩어리의 시작이므로 count+= 1
                dfs(i, j)
    print(count)
