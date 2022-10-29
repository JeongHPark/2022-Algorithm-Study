import java.util.*;
class Solution {
    public int solution(int n, int[][] computers) {
        int[] visited=new int[n];
        int start,count=1,num=n; //start는 시작을 나타내는 변수, count는 네트워크의 개수를 세는 변수, num은 방문하지 않은 남은 컴퓨터가 있는지 세는 변수
        Queue<Integer> queue = new LinkedList<>();

        queue.add(0); //큐에 먼저 0번째를 삽입
        visited[0]=count; //네트워크 번호로 방문 표시
        num--; //방문했으므로 num 개수 줄임

        while(true){
            while(!queue.isEmpty()){ //큐가 비어있지 않을 동안 반복
                start=queue.poll(); //큐의 맨 앞 제거
                for (int i=0; i<n; i++){
                    if (computers[start][i]==1&&visited[i]==0){ //맨 앞과 연결되어 있고 방문하지 않은 컴퓨터 있을 때
                        visited[i]=count; //네트워크 번호로 방문 표시 후
                        queue.add(i); //큐에 추가
                        num--; //방문하지 않은 컴퓨터 개수 줄임
                    }
                }
            }
            if (num==0) break; //모든 컴퓨터를 방문했을 때 종료
            
            //모든 컴퓨터를 방문하지 않았을 때
            for (int i=0; i<n; i++){
                if (visited[i]==0){ //방문 안 한 컴퓨터 발견하면
                    count++; //네트워크 개수 증가
                    queue.add(i); //방문 안 한 컴퓨터 번호 큐에 삽입
                    visited[i]=count; //네트워크 번호로 방문 표시
                    num--; //방문 안 한 컴퓨터 수 하나 줄임
                    break;
                }
            }
        }

        //네트워크 개수 리턴
        return count;
    }
}
