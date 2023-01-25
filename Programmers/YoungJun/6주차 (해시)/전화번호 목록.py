// 첫번째 시도  (효율성 테스트 3,4 실패)

def solution(phone_book):   
    for i in range(0,len(phone_book)-1):
        b=list(phone_book[i])       
        for k in range(i+1,len(phone_book)):           
            c=list(phone_book[k]) 
            stack=min(len(c),len(b))          
            for j in range(min(len(c),len(b))):            
                if b[j]!=c[j]:
                    break
                stack-=1
            if stack==0:
                return False
    return True
  
 //두번째 시도   (효율성 테스트 3,4 실패)

def solution(phone_book):   
    for i in range(0,len(phone_book)-1):       
        for j in range(i+1,len(phone_book)): 
            a=phone_book[i]
            b=phone_book[j]
            if len(a)>len(b):
                if a[:len(b)]==b:
                    return False
            else:
                if b[:len(a)]==a:
                    return False                            
    return True

//세번째 시도 정렬을 이용하여 해결

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        a=phone_book[i]
        b=phone_book[i+1]
        if len(a) < len(b):
            if b[:len(phone_book[i])] == a:
                return False
    return True
