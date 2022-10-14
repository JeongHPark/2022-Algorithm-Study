import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer;
        ArrayList<Integer> arrList = new ArrayList<>();
        int num=-1;

        for (int i=0; i<arr.length; i++){
            if (num!=arr[i]){ //마지막에 저장된 값과 현재 값이 같지 않으면 저장하고 num에 현재 숫자 저장
                arrList.add(arr[i]);
                num=arr[i];
            }
        }

        answer=new int[arrList.size()];
        for (int i=0; i<arrList.size(); i++){
            answer[i]=arrList.get(i);
        }

        return answer;
    }
}
