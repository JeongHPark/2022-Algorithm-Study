import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer;
        ArrayList<Integer> arrList = new ArrayList<>(); //배열에 계속 추가하기 위해 ArrayList를 사용
        int num=-1;

        for (int i=0; i<arr.length; i++){
            if (num!=arr[i]){ //마지막에 저장된 값과 현재 arr의 값이 같지 않으면 저장하고 num에 현재 숫자 저장
                arrList.add(arr[i]);
                num=arr[i];
            }
        }

        answer=new int[arrList.size()]; //int형 배열에 ArrayList 값을 넣기
        for (int i=0; i<arrList.size(); i++){
            answer[i]=arrList.get(i);
        }

        return answer;
    }
}
