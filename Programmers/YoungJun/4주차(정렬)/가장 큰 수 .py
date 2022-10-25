  #1차 시도
  #순열을 이용해 풀었으나 시간초과가 남
  #인터넷을 찾아보니 "permutations 함수는 시간복잡도가 O(n!) 혹은 O(nr)으로 코딩테스트에 쓰기에는 적합하지 않습니다." 라고 함.


  
import itertools
def solution(numbers):
    array=[]
    aa=[1 for num in numbers] # numbers 리스트 복사
    aaa = itertools.permutations(aa, len(aa)) # 순열
    ans = [int(''.join(i)) for i in aaa]
    ans.sort(reverse=True) # 정렬
    answer=str(ans[0])# 정렬 후 가장 큰 값
    return answer

  
  

  #2차 시도
  #while 문과 for 문 사용으로 시간복잡도 O(n^2)으로 풀었지만 시간 초과가 남
  # 9 이거나and 전 최댓값과 같을 때 스킵, 10자리 이상 수 모두 소모시 나머지 일의 자리수들 다 더하고 종료하게 설정까지 했지만
  #4번 케이스는 (949.62ms, 10.3MB)로 통과
  #1,2,3,5,6번 케이스는 시간 초과 
  #채점 결과
  #정확성: 66.7
  #합계: 66.7 / 100.0    66.7점
    
    
    
    
def vs(a,b): # 문자형으로 합친후 정수형으로 비교후 큰 값 반환해 주는 함수
    c=str(a)+str(b)
    d=str(b)+str(a)
    if int(c>d):
        return a
    else :
        return b  
def solution(numbers):
    answer = ''
    numbers.sort(reverse=True) #10의 자리수 이상 수를 다 쓰면 일의 자리수들 순서대로 다 더하기 위해 정렬
    check=[0 for num in numbers] # 썼는지 안 썼는지 체크
    tmp=0 # 문자갯수 다 채우면 while 문 탈출
    check_i=0
    mi= -1 #전 최댓값 저장 변수 초기화
    cnt=0
    for i in numbers: # 10의 자리 이상 카운트
        if len(str(i))>1:
            cnt+=1
    while tmp<len(numbers):
        mx=-1
        for j in range (0,len(numbers)):
            if check[j]==0:
                if numbers[j]==9 or numbers[j]==mi:# 전 최댓값과 똑같거나 9일 때 break
                    check_i=j # 인덱스값 저장 (check값 반영을 위해)
                    mx=numbers[j]
                    break
                else:
                    mx= vs(mx,numbers[j]) # 위의 함수를 이용하여 더 큰 수 추출
                    if mx==numbers[j]:
                        check_i=j   
        if len(str(mx))!=1: # 10의 자리 이상 일시 감소
            cnt-=1
            if cnt==0:  # 10자리 이상의 수를 모두 소모 했을 시 나머지 1의 자리수 모두 더하고 break 
                for i in range (check_i,len(numbers)):
                    if check[i]==0:
                        answer+=str(numbers[i])
                break
        check[check_i]=1 # check값 반영
        tmp+=1  # 문자열 갯수 증가
        mi=mx   # 전 최댓값 반영
        answer+=str(mx)
    if int(answer) == 0: # 0000일때 0으로 
        answer='0'
    return answer

  
  
  
  # 3차 시도는 도저히 줄일 수 있는 방법을 생각 해 낼 수 없다고 판단하여 인터넷에서 참조하여 짰음.
  # lambda 라는 함수를 사용하여 해결.
  # 참고 블로그(자세한 설명)
  # https://jokerldg.github.io/algorithm/2021/05/06/most-big-number.html
  
  
  
def solution(numbers):
    numbers = list(map(str, numbers)) # numbers 모두 자료형으로 변환
    numbers.sort(key=lambda x: x * 3, reverse=True) # 문자형이라 *3을 하면 세번 쓰게됨. 세번 쓴 이유는 최댓값 1000이기 때문. 변환 후 앞에 자리수만 가지고 비교하여 정렬 
    return str(int(''.join(numbers)))#숫자형으로 바꾼 뒤 문자형으로 다시 변환 그 이유는 0000을 정수형으로 바꾸면 0이기 때문
    
