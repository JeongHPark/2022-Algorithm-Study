import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
		int[] max = new int[sizes.length]; //가로 세로 중 큰 값 저장 배열
		int[] min= new int[sizes.length];  //가로 세로 중 작은 값 저장 배열
		for(int i=0;i<sizes.length;i++) {
				max[i]=Math.max(sizes[i][0],sizes[i][1]);//둘 중 큰 값 저장
				min[i]=Math.min(sizes[i][0],sizes[i][1]);//둘 중 작은 값 저장
		}
		Arrays.sort(max);//정렬
		Arrays.sort(min);
        int answer=max[sizes.length-1]*min[sizes.length-1];//큰값중 최댓값과 작은값중 최댓값을 곱하여 answer
        return answer;
    }
}
