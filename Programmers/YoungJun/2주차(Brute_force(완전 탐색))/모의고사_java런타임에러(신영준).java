//java로 풀었는데 어떤 수를 써도 런타임 에러로 37.5점 밖에 안 나와서 포기하여 같은 코드로 파이썬으로 써봤더니 맞아서 둘 다 올립니다.
//왜 런타임 에러가 나는지 아시는 분은 훈수 부탁 드립니다

import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] o={0,0,0};//사람들 각자 맞힌 갯수
        int[] circle1={2, 1, 2, 3, 2, 4, 2, 5};//두번째 사람 패턴리스트
        int[] circle2={3, 3, 1, 1, 2, 2, 4, 4, 5, 5};//세번째 사람 패턴리스트
        int stack=0;//자바는 벡터처럼 정답배열에 추가하는 법을 몰라서 공동일등 수 저장변수를 만들어 밑에 변수선언에 일등수만큼 저장해주는 변수 선언
        for(int i=0;i<answers.length;i++){
            if(answers[i]-1==i%5){o[0]++;}//첫번째 사람은 정답값에서 1만빼주면 나머지값이 됨.
            if(circle1[i%circle1.length]==answers[i]){o[1]++;}//리스트 돌려서 정답값확인
            if(circle2[i%circle2.length]==answers[i]){o[2]++;}
        }             
        int max_index=Math.max(o[0],Math.max(o[1],o[2]));     #가장많이 맞힌갯수 저장 변수           
        for(int i=0;i<3;i++){//일등 수 세는 중
            if(max_index==o[i])
            {stack++;}                           }
        int[] answer= new int[stack]; // 일등 수만큼 변수 정답 배열 선언
        for(int i=0;i<3;i++){ // 정답 배열에 저장
            if(max_index<=o[i]) {answer[i]=i+1;}
        }
        return answer;
    }
}
