n = int(input())
m = int(input())

city = []

for i in range(n):
    city.append(list(map(int, input().split())))

travel = list(map(int, input().split()))
travel = list(map(lambda x: x - 1, travel))  # 도시가 1부터 시작하기 때문에 전체를 -1

visited = [False for i in range(n)]
stack = [travel.pop()] #여행경로 중 하나 DFS시작점으로 지정
visited[stack[0]] = True #이것을 추가하지않아 문제발생

while stack: #스택을 이용한 DFS를 사용하여 풀이
    v = stack.pop()
    for i in range(n):
        if city[v][i] == 1 and visited[i] == False:
            visited[i] = True
            stack.append(i)

check = "YES"
for i in travel:
    if visited[i] == 0:
        check = "NO"
        break
print(check)
