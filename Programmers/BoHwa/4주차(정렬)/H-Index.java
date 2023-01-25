import java.util.Arrays;
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        int cnt=0;
        Arrays.sort(citations);
        for (int i=1; i<=citations[citations.length-1]; i++){ //1부터 citations의 최댓값까지 비교
            for (int j=0; j<citations.length; j++){ 
                if (i<=citations[j]&&(citations.length-j)>=i){ //citations의 특정 값이 i 이상이고 인용된 갯수가 i 이상일 때 
                    answer=i; 
                    break;//멈추기
                }
            }
        }
        return answer;
    }
}
