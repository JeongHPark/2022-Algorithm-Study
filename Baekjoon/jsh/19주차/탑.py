#스택을 이용, 자신과 스택의top과 비교하여 스택의top이 더작으면 pop 아니면 자신을 stack에 넣음
#시간복잡도 2N
n=int(input())
tower=list(map(int,input().split()))
tower=[[val,idx] for idx,val in enumerate(tower)]
answer=[0]*len(tower)
stack=[tower.pop()]
for i in tower[::-1]:
    while stack and stack[-1][0]<i[0]:
        answer[stack.pop()[1]]=i[1]+1
    stack.append(i)
for i in answer:
    print(i,end=" ")
    
