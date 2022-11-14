def solution(genres, plays):
    answer = []
    dicts=dict()
    for i,(j,k) in enumerate(zip(genres,plays)): #zip함수는 ()튜플을 반환함
        if j not in dicts: #key값이없으면 key값만들어줌
            dicts[j]=[0]
        dicts[j][0]+=k #{j:[총재생횟수,]}
        dicts[j].append([i,k]) #{j:[총재생횟수,[i,k]]}
    for i in sorted(dicts.items(),key=lambda x:-x[1][0]): #value의 첫번째값(총재생횟수)로 정렬
        li=sorted(i[1][1:],key=lambda x:-x[1])[:2] #장르별 각각의 재생횟수로 정렬후 2개까지만 li에 넣어줌
        for j in li:
            answer.append(j[0]) #인덱스번호만 추출후 answer에 넣어줌
    return answer
