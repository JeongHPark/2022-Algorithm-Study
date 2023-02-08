
def solution(elements):
    sums=set()
    elements+=elements
    for i in range(1,len(elements)//2+1):
        for j in range(len(elements)//2):
            sums.add(sum(elements[j:j+i]))
    return len(sums)


#누적합사용으로 시간개선
def solution(elements):
    answer=set()
    elements+=elements
    sumsave=[0]
    #누적합
    for i in elements:
        sumsave.append(i+sumsave[-1])
    for i in range(1,len(elements)//2+1):
        for j in range(len(elements)//2):
            answer.add(sumsave[j+i]-sumsave[j])
    return len(answer)


