class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        int[] count = new int[3];
        int[] ans1 = {1, 2, 3, 4, 5};
        int[] ans2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] ans3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        String an="";
        int max=0;

        for (int i = 0; i < answers.length; i++) { //각 수포자의 답안과 비교하여 count 증가
            if (answers[i] == ans1[i % ans1.length]) count[0]++;
            if (answers[i] == ans2[i % ans2.length]) count[1]++;
            if (answers[i] == ans3[i % ans3.length]) count[2]++;
        }

        max=Math.max(count[0],Math.max(count[1],count[2])); //count 중 가장 큰 값 찾기

        for (int i=0; i<3; i++){ //max 값과 똑같은 수만큼 맞춘 수포자를 차례대로 an에 넣는다.
            if (max==count[i]) an+=i+1; //i는 0부터 시작하므로 1을 더한다
            // String 형에 먼저 넣는 이유는 가장 많이 맞춘 수포자가 몇 명인지 정확하지 않기 때문에 크기를 알 수 없어 answer의 객체를 생성할 수 없기 때문이다.
        }

        answer=new int[an.length()]; //answer의 크기는 an에 추가된 수포자의 크기만큼

        for (int i=0; i<an.length(); i++)//string을 int 배열로 변환, 이 부분은 블로그를 참고했다.
            answer[i] = an.charAt(i) - '0'; //String인 an의 글자를 하나씩 가져와 answer에 넣는다.
                                            //'0'을 빼는 이유는 글자를 하나씩 가져올 때 문자형의 '1', '2', '3'을 가져오기 때문에 (아스키 코드로 '0'은 60이고 '1'은 61이다.)
                                            //여기서 문자 '0'을 빼주면 int 1, 2, 3을 얻을 수 있다.
        return answer;
    }
}