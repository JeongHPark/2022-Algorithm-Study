#https://deok2kim.tistory.com/317 참고하여 작성
N, K = map(int, input().split())
count = 0
while bin(N).count('1') > K:
  N += 1
  count += 1
  
print(count)
