#혼자 힘으로 해결하지 못하여 인터넷에서 배워서 작성하였습니다.

n= int(input())
a=list(map(int,input().split()))
answer=[0]
for i in a:
  if answer[len(answer)-1]<i:#현재 값이 answer 리스트 마지막 값보다 작으면 추가
    answer.append(i)
  else :
    left = 0
    right = len(answer)
    while left<right: #이분탐색
      mid=(right+left)//2
      if answer[mid]<i:
        left = mid+1
      else :
        right = mid
    answer[right]=i
print(len(answer)-1)
