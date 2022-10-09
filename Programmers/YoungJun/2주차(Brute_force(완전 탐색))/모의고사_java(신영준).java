//java로 풀었는데 어떤 수를 써도 런타임 에러로 37.5점 밖에 안 나와서 포기하여 같은 코드로 파이썬으로 써봤더니 맞아서 둘 다 올립니다.
//왜 런타임 에러가 나는지 아시는 분은 훈수 부탁 드립니다
//(해결완료)
import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] o={0,0,0};
        int[] circle1={2, 1, 2, 3, 2, 4, 2, 5};
        int[] circle2={3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int stack=0;
        for(int i=0;i<answers.length;i++){
            if(answers[i]-1==i%5){o[0]++;}
            if(circle1[i%circle1.length]==answers[i]){o[1]++;}
            if(circle2[i%circle2.length]==answers[i]){o[2]++;}
        }             
        int max_index=Math.max(o[0],Math.max(o[1],o[2]));                
        for(int i=0;i<3;i++){
            if(max_index==o[i])
            {stack++;}                           }
        int[] answer= new int[stack];
        stack=0;
        for(int i=0;i<3;i++){
            if(max_index<=o[i]) {answer[stack]=i+1;stack++;}
        }
        return answer;
    }
}
