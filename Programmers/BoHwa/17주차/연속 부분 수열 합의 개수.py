def solution(elements):
    result=set()
    new_e=elements*2
    for i in range(len(elements)):
        for j in range(len(elements)):
            result.add(sum(new_e[i:i+j+1]))
        
    return len(result)
