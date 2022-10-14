import java.util.*;

public class 같은숫자는싫어 {
    public static void main(String[] args){
        Solution so = new Solution();
        //so.solution();
    }

}


//큐
//같은 숫자 연속 -> 한 번만 출력
//순서대로
//마지막에 들어가 있는 것이 현재 숫자와 같으면 넣지 않고 같지 않으면 넣는다.
class Solution {
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
