'''
첫번째전구의 상태가 켜진경우와 꺼진경우 두가지로 나눠서 (브루트포스)
첫번째 전구의 상태가 정해졌으므로 끝까지 탐색하면서 차례대로 켤지 말지 정하고
마지막전구의 상태가 정답의 상태와 같을경우 answer에 상태를 변화시킨 수를 저장(마지막 전구를 제외한 나머지 전구는 탐색하면서 같게 만들었으므로)
'''
n=int(input())
bf1=list(map(int,input()))
bf2=bf1[:]
af=list(map(int,input()))
answer=-1
bf1[0]=1-bf1[0]
bf1[1]=1-bf1[1]
cnt=1
for i in range(1,n-1):
    if bf1[i-1]!=af[i-1]:
        bf1[i-1]=1-bf1[i-1]
        bf1[i]=1-bf1[i]
        bf1[i+1]=1-bf1[i+1]
        cnt+=1
if bf1[n-2]!=af[n-2]:
        bf1[n-2]=1-bf1[n-2]
        bf1[n-1]=1-bf1[n-1]
        cnt+=1
if bf1[n-1]==af[n-1]:
    answer=cnt
cnt=0
for i in range(1,n-1):
    if bf2[i-1]!=af[i-1]:
        bf2[i-1]=1-bf2[i-1]
        bf2[i]=1-bf2[i]
        bf2[i+1]=1-bf2[i+1]
        cnt+=1
if bf2[n-2]!=af[n-2]:
        bf2[n-2]=1-bf2[n-2]
        bf2[n-1]=1-bf2[n-1]
        cnt+=1
if bf2[n-1]==af[n-1]:
    if answer==-1:
        answer=cnt
    elif answer>cnt:
        answer=cnt
print(answer)
