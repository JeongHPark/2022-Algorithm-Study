#식에 주어진 연산자들로 만들수있는 모든순열을 구하여 값을비교 (21번줄)
#숫자와 연산자를 나누어 리스트에 저장후 (15번줄)
#연산자의 순서에따라 계산후 계산된 숫자와 연산자는 pop후 결과를 push함 (35번줄)
#ex)1,+,20,*,30   +->*
#ex)1,+,20 3개를 pop후 21을push  ==> 21,*,30
from itertools import permutations
def solution(expression):
    answer=0
    op=[]
    for i in ['-','+','*']:
        if i in expression:
            op.append(i)
    list=[]
    s=0
    for i,v in enumerate(expression):
        if v in op:
            list.append(int(expression[s:i]))
            list.append(v)
            s=i+1
    list.append(int(expression[s:]))
    for i in permutations(op):
        temp=list.copy()
        for j in i:
            while(1):
                try:   
                    opidx=temp.index(j)
                except:
                    break
                if j=='-':
                    result=temp[opidx-1]-temp[opidx+1]
                elif j=='+':
                    result=temp[opidx-1]+temp[opidx+1]
                elif j=='*':
                    result=temp[opidx-1]*temp[opidx+1]
                del temp[opidx-1:opidx+2]
                temp.insert(opidx-1,result)
        answer=max(answer,abs(temp[0]))
    return answer
