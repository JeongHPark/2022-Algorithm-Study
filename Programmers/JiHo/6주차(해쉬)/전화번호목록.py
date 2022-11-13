'''
해쉬를 사용하여 풀려고 시도하였으나 효율성테스트 14번을 해결하지 못하여 sort방법을 이용하였다.
문자열 [119, 19911, 11911] sort시 [119,11911,19911]와 같이 첫번째 자리부터 정렬되는 것을 이용한 방법이다.
즉, sort시 [..., 접두어, 접두어를 가진 수,...]로 정렬되어 다음 value가 접두어를 가지고 있는지 확인하게된다.
'''
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1) :
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])] :
            return False
    return True