class Solution {
    static char[] aeiou = {'A','E','I','O','U'};
    static ArrayList<String> list;
    
    public int solution(String word) {
        int answer = 0;
        list=new ArrayList<>();
        
        stick(0,"");
        Collections.sort(list);
        answer=list.indexOf(word)+1;
        
        return answer;
    }
    public void stick(int n, String st){
        if (n>=5) return;
        for (int i=0; i<aeiou.length; i++){
            list.add(st+aeiou[i]);
            stick(n+1,st+aeiou[i]);
        }
        
    }
}
