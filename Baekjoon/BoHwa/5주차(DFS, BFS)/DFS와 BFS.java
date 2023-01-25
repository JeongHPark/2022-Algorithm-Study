import java.util.*;

public class Main {
    public static void main(String[] args) {
        Solution so = new Solution();
        so.runProgram();
    }
}

class Solution{
    int[][] arr;
    boolean[] visited;
    public void runProgram(){
        int v=makeGraph();
        dfs(v);
        System.out.println();
        bfs(v);
    }
    public int makeGraph(){
        int n,m,v;
        Scanner sc = new Scanner(System.in);

        n=sc.nextInt();
        m=sc.nextInt();
        v=sc.nextInt();

        arr=new int[n+1][n+1]; //5 * 5

        for (int i=0; i<m; i++){ //간선 개수만큼 입력
            int a=sc.nextInt();
            int b=sc.nextInt();
            arr[a][b]=1;
            arr[b][a]=1;
        }
        visited=new boolean[arr.length];

        return v;
    }
    public void dfs(int v){
        visited[v]=true;
        System.out.print(v+" ");
        for (int i=1; i<arr.length; i++){ //arr.length를 포함하면 안 됨!!
            if (arr[v][i]==1&&visited[i]==false) dfs(i);
        }
    }

    public void bfs(int v){
        Queue<Integer> queue = new LinkedList<>();
        int s;
        visited=new boolean[arr.length];

        queue.add(v);
        visited[v]=true; //첫 번째에 대한 visited를 true로

        while(!queue.isEmpty()){
            s=queue.poll();
            System.out.print(s+" ");
            for (int i=1; i<arr.length; i++){
                if (arr[s][i]==1&&visited[i]==false){
                    queue.add(i);
                    visited[i]=true; //방문 노드 체크
                }
            }
        }
    }
}
