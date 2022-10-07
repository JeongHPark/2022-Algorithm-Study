class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int max1 = 0;
        int max2 = 0; //초기화 꼭 하기!

        for (int i = 0; i < sizes.length; i++) {
            for (int j = 0; j < sizes[i].length; j++) {
                if (max1 < sizes[i][j]) { //가장 큰 값을 max1에 저장
                    max1 = sizes[i][j];
                }
            }
        }

        for (int i = 0; i < sizes.length; i++) {
            if (max2 < sizes[i][0] && max2 < sizes[i][1]) {//max2보다 비교하는 배열의 값이 모두 크다면
                max2 = Math.min(sizes[i][0], sizes[i][1]);//배열의 둘 중 작은 값을 max2에 대입
            }
        }

        answer=max1*max2;

        return answer;
    }
}
