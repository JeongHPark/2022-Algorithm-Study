#가장 긴 증가하는 부분 수열2 문제와 같은 로직으로 접근
n = int(input())

n_li = list(map(int, input().split()))

m_li = []

def search(n) :
    for i in range(len(m_li)) :
        if m_li[i] >= n : return i #동일한 값일때도 처리
    return -1

for i in n_li :
    temp = search(i)
    if temp == -1 : 
        m_li.append(i)
    else :
        m_li[temp] = i

print(len(m_li))