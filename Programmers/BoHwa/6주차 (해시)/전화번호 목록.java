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
