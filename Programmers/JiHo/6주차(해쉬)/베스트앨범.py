from collections import defaultdict

def solution(genres, plays):
    geners_sum = defaultdict(int)
    geners_li = defaultdict(list)
    for i in range(len(genres)) :
        geners_sum[genres[i]] += plays[i] #장르의 합을 구함
        geners_li[genres[i]].append([plays[i],i]) #{장르 = [재생횟수, 인덱스]}로 저장
    
    ordered_li = sorted(geners_sum,reverse=True, key=lambda x:geners_sum[x]) #장르의 합을 기준으로 정렬
    #sorted는 반환값으로 [(key,value)](tuple_pair_list)로 정렬하여 반환하는 특성을 이용하여 dict을 정렬할 수 있다.
    answer = []
    for i in ordered_li : #정렬된 장르 순서로 입력
        answer += (list(map(lambda x:x[1], sorted(geners_li[i], reverse=True, key=lambda x:[x[0],-x[1]])[:2])))
    return answer