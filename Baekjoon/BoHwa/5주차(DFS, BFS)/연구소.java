import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Virus{
    int x;
    int y;
    Virus(int x, int y){
        this.x=x;
        this.y=y;
    }
}
public class Main {
    int[][] map; //처음 입력받는 지도
    static int max;
    public static void main(String[] args) {
        Main ma = new Main();

        ma.makeGraph();
        ma.makeWall(0);
        System.out.println(max);
    }

    public void makeGraph(){
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int m=sc.nextInt();

        map=new int[n][m];
        for (int i=0; i<n; i++) {
            for (int j = 0; j < m; j++) {
                map[i][j] = sc.nextInt();
            }
        }

    }
    public void makeWall(int cnt){
        if (cnt==3){
            bfs();
            return;
        }

        for (int i=0; i<map.length; i++){
            for (int j=0; j<map[0].length; j++){
                if (map[i][j]==0){
                    map[i][j]=1;
                    makeWall(cnt+1);
                    map[i][j]=0;
                }
            }
        }
    }

    public void bfs(){
        Queue<Virus> queue = new LinkedList<>();
        int[][] virusMap=new int[map.length][map[0].length];
        int[] plusX = {0,0,-1,1}; //상하좌우
        int[] plusY = {-1,1,0,0};

        for(int i = 0; i < map.length; i++)
            for(int j = 0; j < map[0].length; j++){
                virusMap[i][j] = map[i][j]; //복사
                if (virusMap[i][j]==2) //바이러스인 경우 큐에 넣기
                    queue.add(new Virus(j,i)); //순서 주의
            }

        while(!queue.isEmpty()){
            Virus v= queue.poll();
            for (int i=0; i<4; i++){ //바이러스의 상하좌우에서
                int newX=v.x+plusX[i];
                int newY=v.y+plusY[i];

                if (newX>=0&&newY>=0&&newX<virusMap[0].length&&newY<virusMap.length){
                    if (virusMap[newY][newX]==0){ //순서 주의
                        queue.add(new Virus(newX,newY));
                        virusMap[newY][newX]=2;
                    }
                }
            }
        }
        checkSafeZone(virusMap);
    }

    public void checkSafeZone(int[][] newMap){
        int answer=0;
        for (int i=0; i<map.length; i++){
            for (int j=0; j<map[0].length; j++){
                if (newMap[i][j]==0) answer++;
            }
        }
        max=Math.max(answer,max);
    }
}
