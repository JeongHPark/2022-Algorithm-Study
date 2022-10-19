class Solution {
    boolean solution(String s) {
        int count=0;

        if (s.charAt(0)!='(') return false; //처음 괄호가 열린 괄호가 아니면 바로 false 리턴
        if (s.charAt(s.length()-1)!=')') return false; //마지막 괄호가 닫힌 괄호가 아니면 바로 false 리턴

        for (int i=0; i<s.length(); i++){
            if (count<0) return false; //count가 음수가 되면 열린 괄호 없는 상태에서 닫힌 괄호가 들어왔다는 것이므로 바로 false 리턴
            if (s.charAt(i) == '(') { //열린 괄호이면
                count++;
            }
            else count--;
        }
        if (count>0||count<0) return false;
        return true;
    }
}