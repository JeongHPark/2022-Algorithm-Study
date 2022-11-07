//혼자 풀지 못해서 블로그를 참고하였습니다.
import java.util.Map;
import java.util.HashMap;

class Solution {
    public boolean solution(String[] phone_book) {
        Map<String,Integer> map = new HashMap<>();
        for (int i=0; i<phone_book.length; i++)
            map.put(phone_book[i],i); //HashMap에 phone_book의 각 값과 i(인덱스) 넣기
        
        for (int i=0; i<phone_book.length; i++){
            for (int j=0; j<phone_book[i].length(); j++){
                if (map.containsKey(phone_book[i].substring(0,j)))
                    //phone_book의 i번째 값을 0번째부터 j번째까지 잘라가면서 자른 값들이 map에 저장되어 있는 값인지 확인한다.
                    //map에 있는 값이면 false 반환
                    return false;
            }
        }
        
        return true;
    }
}
/* 해시를 이용하지 않은 풀이
import java.util.Arrays;
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Arrays.sort(phone_book); //phone_book을 값에 따라 정렬한다. (ex) 12, 111, 119, 121 -> 111, 119, 12, 121 (문자열이기 때문에 숫자에 따라 정렬 후 길이에 따라 정렬)
        for (int i=0; i<phone_book.length-1; i++){
            if (phone_book[i+1].startsWith(phone_book[i])){ //다음 값의 시작이 현재 값으로 시작하는지 확인
                return false;
            }
        }
        return answer;
    }
}

*/
