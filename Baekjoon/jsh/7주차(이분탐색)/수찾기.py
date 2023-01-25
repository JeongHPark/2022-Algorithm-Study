import sys
input=sys.stdin.readline
N=int(input())
lis=list(map(int,input().strip().split(" ")))
lis.sort() #이분탐색을 위한 정렬
M=int(input())
comp=list(map(int,input().strip().split(" ")))
for i in comp:
    num=0
    st=0 #맨왼쪽값
    en=N-1 #맨오른쪽값
    while st<=en: #이분탐색
        mid=(st+en)//2
        if lis[mid]<i:
            st=mid+1
        elif lis[mid]>i:
            en=mid-1
        else:
            num=1
            break
    print(num)
