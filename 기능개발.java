import java.util.ArrayList;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = {};
        int index = 0; //아직 배포되지 않은 작업의 가장 앞 작업을 가리키는 index
        int count = 0;
        ArrayList<Integer> arr = new ArrayList<>();

        while (index != progresses.length && progresses[index] < 100) { //index != progresses.length를 안 쓰면 index of bounds exception
            for (int i = 0; i < progresses.length; i++) //각 작업에 speeds 만큼식 더해준다.
                progresses[i] += speeds[i];

            while (index != progresses.length && progresses[index] >= 100) { //더해준 후 index 부분이 100 이상이면
                count++; //count를 올려주고
                index++; //다음 인덱스 가리킨다.
                if (index != progresses.length && progresses[index] < 100) { //가리키는 index의 작업이 100보다 작으면
                    arr.add(count); //count 만큼을 arr에 추가한다.
                    count=0; //count 0으로 다시 초기화
                }
                //Index out of bounds exception를 방지하기 위해 마지막 인덱스 였었던 경우를 따로 나눈다.
                else if (index==progresses.length&&progresses[index-1]>=100) arr.add(count);
            }
        }

        answer=new int[arr.size()];
        for (int i = 0; i < arr.size(); i++)
            answer[i]=arr.get(i);


        return answer;
    }
}