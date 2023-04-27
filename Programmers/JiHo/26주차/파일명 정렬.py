##https://an-jiohh.github.io/%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4/programmers/python/%ED%8C%8C%EC%9D%BC%EB%AA%85-%EC%A0%95%EB%A0%AC/
def solution(files):
    answer = []
    for i in files :
        head = ""
        number = ""
        for j in i :
            if j.isdigit() : number += j
            elif len(number) == 0 : head += j #number에 아무것도 없으면 헤드로 처리
            elif len(number) != 0 : break #Tail로 처리를 하다가, 다시 숫자가 나왔을때도 그대로 Tail로 처리되는가?
        answer.append((head.lower(), int(number), i)) #소문자로 바꾸고 사전순으로 정렬하였는가?
    answer.sort(key=lambda x:(x[0],x[1]))
    answer = list(map(lambda x:x[2], answer))

    return answer
