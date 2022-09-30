def solution(name):
    sl=list(name) # 긴 문자열을 한 글자씩 나눠서 저장 시킴
    answer=0
    side = len(sl) - 1#옆으로 이동하는 수의 최댓값 저장
    for i, char in enumerate(sl): # for문을 인덱스값인 i를 쓸수 있게 해주는 enumerate()
        stack=i+1 # a연속갯수 저장 스탯
        for j in range(len(sl)-stack):#이중 for문으로 돌려서 a연속갯수 저장
            if sl[stack]=='A' and stack<len(sl):
                 stack+=1
            else :
                 break

        side = min([side, 2 *i + len(sl) - stack, i + 2 * (len(sl) -stack)])#왼쪽으로 갔다가 오른쪽으로 간 값과 오른쪽으로 갔다가 왼쪽으로 간 값 더하기
    answer+=side   #for문이 끝나면 더해주기

    for i in sl :  # 상하좌우 값 아스키 코드값 만큼 더해주기   대문자 아스키 코드 A~Z 65 - 90
        answer += min(ord(i)-65,91-ord(i))
    return answer
