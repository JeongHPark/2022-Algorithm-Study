'''
dfs이용하여 모든 순열 대입
음수를 나눌때 잘못된값이 나와 31번줄 조건문 추가
'''
n=int(input())
num=list(map(int,input().split()))
op=list(map(int,input().split()))
answer=[float("inf"),float("-inf")]
def dfs(sum,op,cnt):
    global answer
    global num
    global n
    if cnt==n-1:
        answer[0]=min(answer[0],sum)
        answer[1]=max(answer[1],sum)
        return sum
    if op[0]!=0:
        op[0]-=1
        dfs(sum+num[cnt+1],op,cnt+1)
        op[0]+=1
    if op[1]!=0:
        op[1]-=1
        dfs(sum-num[cnt+1],op,cnt+1)
        op[1]+=1
    if op[2]!=0:
        op[2]-=1
        dfs(sum*num[cnt+1],op,cnt+1)
        op[2]+=1
    if op[3]!=0:
        op[3]-=1
        #음수일때 나눗셈처리
        if sum<0:
            dfs(-((-sum)//num[cnt+1]),op,cnt+1)
        else:
            dfs(sum//num[cnt+1],op,cnt+1)
        op[3]+=1
dfs(num[0],op,0)
print(answer[1])
print(answer[0])
