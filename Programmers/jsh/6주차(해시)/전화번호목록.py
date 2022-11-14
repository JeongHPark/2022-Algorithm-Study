def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x:len(x)) #길이순으로 정렬
    li=set() #중복제거를 위한 집합선언
    dicts=dict() #자료형안의 원소를 빨리찾기위한 딕셔너리 선언
    '''
    각 원소마다 길이를 li에 저장시키고
    dicts에 전화번호저장
    li에 저장된 길이만큼씩 [:j]로 자르고 dicts에 있는지확인(접두사인지 체크)
    '''
    for i in phone_book:
        li.add(len(i))
        dicts[i]=i
        for j in li:
            if i[:j] in dicts and i[:j]!=i:
                return False
    return answer
