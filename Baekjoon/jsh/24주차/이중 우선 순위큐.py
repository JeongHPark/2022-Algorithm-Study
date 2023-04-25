from heapq import heappop,heappush
from collections import defaultdict
import sys
input=sys.stdin.readline
t=int(input())
for i in range(t):
    d=defaultdict(int)
    cnt=0
    n=int(input())
    heapmax=[]
    heapmin=[]
    for j in range(n):
        cmd,num=input().rstrip().split()
        num=int(num)
        if cmd=="I":
            heappush(heapmin,num)
            heappush(heapmax,-num)
            d[num]+=1
            cnt+=1
        elif num==1 and cnt!=0:
            while 1:
                temp=-heappop(heapmax)
                if d[temp]!=0:
                    d[temp]-=1
                    break
            cnt-=1
        elif cnt!=0:
            while 1:
                temp=heappop(heapmin)
                if d[temp]!=0:
                    d[temp]-=1
                    break
            cnt-=1
    if cnt==0:
        print("EMPTY")
    else:
        while 1:
                temp=-heappop(heapmax)
                if d[temp]!=0:
                    print(temp,end=" ")
                    break
        while 1:
                temp=heappop(heapmin)
                if d[temp]!=0:
                    print(temp)
                    break

