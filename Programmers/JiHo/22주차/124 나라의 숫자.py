#3진수로 바꾸고 3진수를 124로 바꾸고자 하였슴
#문제점 0이없고 1일경우는 1이지만 4일경우 10이 아닌 11이 된다는 것이 문제점이다.
#이로인하여 자리수가 올라갈때마다 1씩 올라간다는 것이 문제점이다.
#반복문이 반복될때마다 = 해당 자리수가 계산때 -> n에서 1씩 빼주는 방법을 사용하였다.
def solution(n):
    answer = ''
    arr = [1,2,4]
    while n > 0 :
        n = n - 1
        answer = str(arr[n % 3]) + answer
        n = n // 3
    print(answer)
    return answer
