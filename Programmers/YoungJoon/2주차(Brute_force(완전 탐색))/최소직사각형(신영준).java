import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
	    int long1 = 0;//가로 세로 포함 제일 큰 값
	    int long2 = 0;//가로 혹 세로 긴 값을 제외하고서 제일 큰 값
		for(int i=0;i<sizes.length;i++) {
				if(long1<Math.max(sizes[i][0],sizes[i][1])){
                    long1 = Math.max(sizes[i][0],sizes[i][1]);}//제일 큰 값 갱신
				if(long2<Math.min(sizes[i][0],sizes[i][1])){
                    long2 = Math.min(sizes[i][0],sizes[i][1]);}//가로 혹 세로 긴 값을 제외하고서 제일 큰 값 갱신
		}
        int answer= long1*long2;//큰값중 최댓값과 작은값중 최댓값을 곱하여 answer
        return answer;
    }
}
