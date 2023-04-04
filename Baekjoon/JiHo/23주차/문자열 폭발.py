arr = input()
bomb = list(input())
bomb.reverse()
bomb2 = bomb[1:]
stack = []
for i in arr :
    if i == bomb[0] :
        count = 1
        temp = []
        for j in bomb2 :
            k = ""
            if stack : 
                k = stack.pop() 
                temp.append(k)
            else : 
                for l in temp[::-1] :
                    stack.append(l)
                stack.append(bomb[0])
                break
            if k == bomb[count] :
                count += 1
                if count == len(bomb) :
                    break
            else :
                for l in temp[::-1] :
                    stack.append(l)
                stack.append(bomb[0])
                break
    else :
        stack.append(i)
if stack :
    for i in stack :
        print(i,end="")
else : print("FRULA")
