#k개의 물병 각각 2^x 개의 물병으로부터 합쳐져 1개의물병이됐으므로
#k=3이라면 최대 2^a+2^b+2^c개의 물병으로부터 합쳐졌다고 볼수있고
#N에서 N보다 작거나같은 2^x값을 찾아서 k번 반복하면 2^a+2^b+2^c 에서 a,b,c값을 구할수있다.
N,K=map(int,input().split())
for i in range(K-1):
    num=0
    while 2**num<=N:
        num+=1
    N-=2**(num-1)
    if N==0:
        print(0)
        break
if N!=0:
    num=0
    while 2**num<N:
        num+=1
    print(2**num-N)
