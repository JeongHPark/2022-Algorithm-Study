#싸이클을 이루는 집합들을 모두구한다(시작 숫자와 끝 숫자가 같을경우)
#싸이클을 이루면 다시 접근할필요가없으므로 check 변수에 대입함
n = int(input())
number = [int(input()) for _ in range(n)]
number.insert(0, 0)
answer = []
check = []
for i in range(1, n+1):
    top = i
    temp = []
    while top not in check:
        check.append(top)
        temp.append(top)
        top = number[top]
    if not temp:
        continue
    if top == temp[0]:
        answer.append(temp)
    else:
        for _ in range(len(temp)):
            check.pop()
answer = sum(answer, [])
answer.sort()
print(len(answer))
for i in answer:
    print(i)
