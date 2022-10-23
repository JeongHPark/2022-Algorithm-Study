'''
python sort lambda : list로 리턴시 list요소를 기준으로 정렬
lambda x:list(str(x))으로 실행시
-> 34, 30, 3으로 정렬으로 2번예제를 충족하지 못함
-> list(str(x)) * 3으로 비교할수있는 최저 원소를 채워준다(원소최대 1000)
즉, 3 -> 333, 34 -> 343434, 30 -> 303030으로 sort시 list의 앞부분부터 비교되어 정렬되기때문에
두번째, 세번째요소까지 비교하여 정렬가능하게 한다.
시간복잡도 O(nlogn)
'''
def solution(numbers):
    numbers.sort(key = lambda x:list(str(x)) * 3, reverse = True)
    answer = str(int(''.join(list(map(str, numbers))))) 
    #11번 테스트 케이스 [0,0,0,0] -> "0", str(int()) "0000" -> "0"으로 바꾸기 위해사용 
    return answer