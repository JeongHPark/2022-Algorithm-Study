import java.util.ArrayList;

class Solution {
    ArrayList<Integer> arr = new ArrayList<Integer>(); //만들어진 숫자를 저장하는 List
    boolean visited[];//방문했는지 확인하는 배열

    public int solution(String numbers) {
        int answer = 0;
        String tmp = "";
        visited = new boolean[numbers.length()];

        for (int i = 1; i <= numbers.length(); i++) { //i 자릿수 만듦
            makeNum(numbers, tmp, i);
        }

        for (int x : arr) {
            if (isPrime(x)) answer++;
        }

        return answer;
    }

    public void makeNum(String num, String tmp, int len) {
        if (tmp.length() == len) {//현재 문자열의 길이가 원하는 자릿수와 같다면
            if (!arr.contains(Integer.parseInt(tmp))) //현재 문자열을 int로 전환하여 ArrayList에 포함되어 있는지 확인
                arr.add(Integer.parseInt(tmp)); //없으면 추가
            return; //돌아감
        }
        for (int i = 0; i < num.length(); i++) { //문자열 길이만큼 반복
            if (visited[i]) continue; //방문했던 숫자라면 넘어감
            tmp += num.charAt(i);
            visited[i] = true;
            makeNum(num, tmp, len);
            visited[i] = false;
            tmp = tmp.substring(0, tmp.length() - 1); //마지막 자리 숫자 제외 후 갱신
        }

    }

    public boolean isPrime(int n) {
        if (n == 0 || n == 1) return false;

        for (int i = 2; i <= Math.sqrt(n); i++) { //테스트 케이스 2, 10, 11 통과, =을 포함시켜야 한다.
            if (n % i == 0) return false;
        }
        return true;
    }

}