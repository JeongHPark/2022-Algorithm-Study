class Solution {
    public String solution(String number, int k) {
        //String은 새로운 객체를 계속 만들기 때문에 같은 객체를 계속 사용하는 StringBuilder를 사용한다.
        StringBuilder answer = new StringBuilder();
        int n = k;
        int index = 0;

        /*예 : 75913에서 3개를 없애고 큰 수 만드려면 2개를 남겨야 하므로 맨 뒤의 것은 고를 수 없다.
        맨 뒤의 것을 제외한 인덱스 3번째까지 중에서 가장 큰 값을 첫 번째로 고르고 고른 값 뒤의 값부터 인덱스 3+1번째까지 중 가장 큰 값을 고른다.*/
        while (index != n) {//시작 위치와 고를 수 있는 최대 인덱스가 같지 않을 동안 반복
            char max = '0';
            for (int i = index; i <= n; i++) { //인덱스가 n번째 일 때까지 가능하다.
                if (max < number.charAt(i)) { //max보다 number의 값이 더 크면
                    max = number.charAt(i); //max를 바꾸기
                    index = i; //index는 현재 위치, 가장 마지막에 저장되는 인덱스가 max 값의 인덱스이다.
                }
                if (max == 9) break; //테스트 10 통과, max가 9일 경우에는 for 루프를 바로 벗어난다.
            }
            answer.append(max); //answer에 max 값을 더한다.
            index++; //max 인덱스의 다음 인덱스부터 시작
            if (n<number.length()) n++; //하나를 골랐으므로 n이 끝의 인덱스가 아닐 때 고를 수 있는 인덱스의 범위가 하나 늘어난다.
            if (n >= number.length()) n = index; //테스트 12 해결
        }
        if (index == n && (number.length() - k != answer.length()))
            //시작 위치와 끝날 수 있는 최대 인덱스가 같으면 뺄 수 있는 수는 모두 뺐다는 뜻이므로 나머지 숫자를 모두 붙여준다, 테스트 12 해결
            for (int i = index; i < number.length(); i++) {
                answer.append(number.charAt(i));
            }

        return answer.toString();
    }
}
