import java.util.*;

public class Solution {
    public int solution(int n) {
        int ans = 0;

        while(n!=0){
            if (n%2==0){
                n=n/2;//2로 나누었을 때의 몫!
            }
            else {
                n--;
                ans++;
            }
        }

        return ans;
    }
}
