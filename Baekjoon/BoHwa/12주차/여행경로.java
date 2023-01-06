/*
주어진 tickets 배열을 정렬시킨다.
ICN 부터 시작하여 갈 수 있는 경로로 끝까지 간다.
만약 모든 공항을 지나지 못하면 이전으로 돌아와 방문했던 공항을 다시 제거하여 다른 경로로 조사한다.
=> dfs 알고리즘 이용
*/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    boolean[] visited; //방문 노드 체크
    List<String> arr=new ArrayList<>();
    boolean check; //모든 공항 방문했는지 확인
    
    public String[] solution(String[][] tickets) {
        visited=new boolean[tickets.length];

        Arrays.sort(tickets, (o1, o2) -> { //tickets 정렬
            if(o1[0].equals(o2[0])) {
                return o1[1].compareTo(o2[1]);
            } else {
                return o1[0].compareTo(o2[0]);
            }
         });
        arr.add("ICN");
        dfs("ICN",tickets,0);

        String[] answer= arr.toArray(new String[arr.size()]); //arraylist를 string array로 바꿈 //블로그 참고
        
        return answer;
    }
    
    public void dfs(String now,String[][] tickets,int count)
    {
        if (count==tickets.length) { //방문한 공항 수와 방문해야 할 공항 수가 같으면
        	check=true;
        	return;
        }
        
        for (int i=0; i<tickets.length; i++)
        {
        	if (tickets[i][0].equals(now)&&!visited[i]) { //현재 방문해야할 공항과 배열의 [0]번째 공항이 같고 방문하지 않았다면
        		arr.add(tickets[i][1]); //그 배열의 [1]번째 공항을 추가
        		visited[i]=true;
        		dfs(tickets[i][1],tickets,count+1); 
        		
        		if (!check) { //배열을 다 돌았는데 check가 false로 되어있다면
        			arr.remove(arr.size()-1); //arraylist의 맨 뒤부터 제거시키기
        			visited[i]=false;
        		}
        	}
        }
    }
}
