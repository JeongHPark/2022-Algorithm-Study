import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        String[] arr = new String[numbers.length];

        for (int i=0; i<numbers.length; i++)
            arr[i]=String.valueOf(numbers[i]); //int 형 numbers를 string 형으로 바꿔준다.


        Arrays.sort(arr,new Comparator<String>(){ //o2+o1과 o1_o2를 비교, comparator의 기준으로 정렬
            @Override
            public int compare(String o1, String o2) {
                return (o2+o1).compareTo(o1+o2); //o2+o1과 o1+o2를 비교하여 o2+o1이 더 작으면 o1 o2 순(o1+o2가 더 크기 때문), o1+o2가 더 작으면 o2 o1 순
            }
        });

        //문자열의 값이 0으로만 구성된 경우(맨 앞의 숫자의 값이 0인 경우) 0만 리턴
        if (arr[0].equals("0")) return "0";

        for (String a:arr){
            answer+=a;
        }

        return answer;
    }
}
