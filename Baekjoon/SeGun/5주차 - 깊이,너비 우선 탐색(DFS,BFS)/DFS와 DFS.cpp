#include <iostream>
#include<queue>

using namespace std;

int n,m,start;
bool arr[1111][1111];
bool visited[1111];

void input(){   //입력 부분
  cin>>n>>m>>start;
  for(int i=0;i<m;i++){
    int x,y;
    cin>>x>>y;
    arr[x][y]=arr[y][x]=true; //입력받고 바로 arr배열에 연결 정보 저장
  }
}

void DFS(int x){
  cout<<x<<" ";
  for(int i=1;i<=n;i++){
    if(visited[i]==false&&arr[x][i]==true){ //방문하지 않고 x와 연결되어있는 부분 찾기
      visited[i]=true;
      DFS(i);
    }
  }
}

void BFS(int x){
  for(int i=1;i<=n;i++){visited[i]=false;}  //visited 초기화
  visited[x]=true;  //시작점 방문처리
  
  queue<int> q; //큐사용
  q.push(x);  //시작점 큐에 넣어줌
  
  while(q.size()!=0){
    int cur=q.front(); //큐 맨앞 값을 지정해주는 cur 선언
    q.pop();  
    cout<<cur<<" ";
    for(int i=1;i<=n;i++){
      if(visited[i]==false&&arr[cur][i]==true){ //방문하지 않고 cur과 연결되어있는 부분 찾기
        visited[i]=true;  //방문 처리
        q.push(i);  //큐에 넣어주기
      }
    }
  }
}

int main(void) {
  input();
  visited[start]=true;
  DFS(start);
  cout<<endl;
  BFS(start);
}
