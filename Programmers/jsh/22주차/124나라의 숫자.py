'''
처음엔 3진법으로 시도해봤으나 0을 표현하는 수가없어서 실패
모든자리엔 무조건 1부터 들어가야하므로 n에 3^0 ~ 3^1,3^2 을 차례대로 빼줌(음수가될때까지)
그다음 3진법으로 계산하여 나머지가 0일땐 '1' 1일땐 '2' 2일땐 '4'를 넣어줌
마지막으로 자릿수를 계산하여 0자리에 '1'을 자릿수에맞게 채워넣어줌
'''
def solution(n):
    answer = ''
    num=['1','2','4']
    su=0
    while n-(3**su)>=0:
        n=n-(3**su)
        su+=1
    while n!=0:
        temp=n%3
        answer+=num[temp]
        n=n//3
    while len(answer)!=su:
        answer+="1"
    return answer[::-1]
