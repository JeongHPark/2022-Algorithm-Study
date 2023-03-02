'''
DP사용 현재최대가치값과 자신의가치+가방에 남는자리의 가치최댓값을 비교하여 갱신
'''
n, k = map(int, input().split())
item = []
for i in range(n):
    item.append(list(map(int, input().split())))
item.sort()
w = [0]*(k+1)
for i in item:
    wt = w.copy()
    for j in range(i[0], k+1):
        if wt[j] < i[1]+wt[j-i[0]]:
            w[j] = i[1]+wt[j-i[0]]
print(w[k])
