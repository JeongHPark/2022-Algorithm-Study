'''
works 배열을 정렬해주고 제일큰수부터 1씩빼주는걸 n번반복함
works 길이 m이라고할때 시간복잡도 mlogm(works 정렬)+n(13번째줄 for문 n번 반복)+n(22번째줄 원소 제곱 합 구할때)
'''

def solution(n, works):
    works.sort(reverse=True)
    while n!=0:
        if works[0]!=0:
            cmp=works[0]-1
        else:
            return 0
        for i in range(len(works)):
            if cmp>=works[i]:
                break
            elif n!=0:
                works[i]-=1
                n-=1
            else:
                break
    answer = 0
    for i in works:
        answer+=i*i
    return answer
