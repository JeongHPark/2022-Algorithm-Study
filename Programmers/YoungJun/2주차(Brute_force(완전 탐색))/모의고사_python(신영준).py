def solution(answers):
    answer = []
    o=[0,0,0]; #사람들 각자 맞힌 갯수
    circle1=[2, 1, 2, 3, 2, 4, 2, 5]; #두번째 사람 패턴리스트
    circle2=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5];#세번째 사람 패턴리스트
    for i in range(len(answers)):
        if answers[i]-1 == i%5: #첫번째 사람은 정답값에서 1만빼주면 나머지값이 됨.
            o[0] += 1
        if answers[i] == circle1[i%len(circle1)]:# 리스트 돌려서 정답값확인
            o[1] += 1
        if answers[i] == circle2[i%len(circle2)]:
            o[2] += 1          
        max_value=max(o) #가장많이 맞힌갯수 저장 변수
    for i in range(len(o)):
        if o[i] == max_value: #가장많이 맞힌사람 찾아서 정답에 저장
            answer.append(i+1)
    return answer       
