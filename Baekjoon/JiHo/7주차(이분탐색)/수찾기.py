n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

def binary_search(start, end, t) :
    if start > end : return 0
    mid = (start + end) // 2
    if n_list[mid] == t : return 1
    elif n_list[mid] < t :return binary_search(mid + 1, end, t)
    elif n_list[mid] > t : return binary_search(start, mid-1, t)

n_list.sort()
for i in m_list :
    print(binary_search(0, n-1, i))