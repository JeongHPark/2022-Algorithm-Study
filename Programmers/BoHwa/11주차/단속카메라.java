//참고 : https://velog.io/@ahnick/programmers-%EB%8B%A8%EC%86%8D%EC%B9%B4%EB%A9%94%EB%9D%BC

import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int solution(int[][] routes) {
        int answer = 0;
        int loc=-30001;

        Arrays.sort(routes,new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[1]-o2[1];
            }
        }); //나가는 지점에 대하여 sort

        for (int i=0,len=routes.length; i<len; i++)
        {
            if (loc<routes[i][0]) { //마지막에 카메라 세워진 위치가 현재 자동차의 진입 지점보다 이전에 위치하면 현재 자동차의 진출 지점에 새로운 카메라 세우기
                answer++;
                loc=routes[i][1];
            }
        }
        return answer;
    }
}
