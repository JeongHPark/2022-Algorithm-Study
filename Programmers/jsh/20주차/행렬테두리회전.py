#구현문제 문제대로 작성함
def solution(rows, columns, queries):
    answer = []
    a=[]
    for i in range(rows):
        b=[]
        for j in range(columns):
            b.append(i*columns+j+1)
        a.append(b)
    for k in queries:
        queue=[]
        for i in range(k[1]-1,k[3]):
            queue.append(a[k[0]-1][i])
        for i in range(k[0],k[2]):
            queue.append(a[i][k[3]-1])
        for i in range(k[3]-2,k[1]-1,-1):
            queue.append(a[k[2]-1][i])
        for i in range(k[2]-1,k[0]-1,-1):
            queue.append(a[i][k[1]-1])
        queue.insert(0,queue.pop())
        answer.append(min(queue))
        for i in range(k[1]-1,k[3]):
            a[k[0]-1][i]=queue.pop(0)
        for i in range(k[0],k[2]):
            a[i][k[3]-1]=queue.pop(0)
        for i in range(k[3]-2,k[1]-1,-1):
            a[k[2]-1][i]=queue.pop(0)
        for i in range(k[2]-1,k[0]-1,-1):
            a[i][k[1]-1]=queue.pop(0)
        
    return answer
