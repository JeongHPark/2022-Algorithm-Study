'''
최장 증가 부분수열 알고리즘을 참고하여 코딩했습니다.
https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4
ex) 10,20,5,7,20,30
result=
[10]
[10,20]
[5,20]
[5,7]
[5,7,20]
[5,7,20,30] -> 최대길이 4
'''
N=int(input())
num=list(map(int,input().split(" ")))
result=[num[0]] #맨처음 num의 첫원소를넣어줌
for i in range(1,N):
    if result[-1]<num[i]: #result맨뒤의 원소보다 크면 바로 추가해줌
        result.append(num[i])
    else: #이분탐색을 하여 자신이 들어갈위치를 찾음
        st=0
        en=len(result)-1
        while st<=en:
            if st==en: #자신의 자리를찾음
                result[st]=num[i]
                break
            else:
                if result[(st+en)//2]<num[i]:
                    st=(st+en)//2+1
                elif result[(st+en)//2]>num[i]:
                    en=(st+en)//2
                elif result[(st+en)//2]==num[i]: #이미 있는 경우는 갱신이 필요 없음 반복문 종료
                    break
print(len(result)) #result의 길이가 최장증가 부분수열임
