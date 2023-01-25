def solution(citations):
    answer = 0
    for n in range(len(citations)+1):#n이 리스트의 갯수까지 될 수 있기에 길이에 +1 추가
        h = 0
        for cit_i in citations: # 이중 for문을 돌려 citations 값이 n이상일 시 h증가 
            if n <= cit_i:
                h += 1
        if n <= h and n-len(citations) <= h:
            # n편 중, 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하일 시 answer값으로 변경
            answer = n
    return answer
