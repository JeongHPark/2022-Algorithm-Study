모든 결과를 매핑하고 서로 이기고 지는 모든 경우를 DFS를 사용해서(a가 b 를 이기고 b 가 c를 이기면 a는 c를 이기는것) 추가로 매핑해주고 자신을 제외한 값이 모두 0이 아니라면
몇등인지 확인할 수 있다. 
-플로이드 알고리즘(3중for문)을 사용하면 간단하게 해결가능

#include <string>
#include <vector>
#include<queue>
#include<iostream>

using namespace std;

void DFS(vector<vector<int>>& map,int start,int cur,bool visited[]){
    for(int i=1;i<=map.size();i++){
        if(visited[i]==false){
            if(map[cur][i]==1){
                visited[i]=true;
                map[start][i]=1;
                map[i][start]=2;
                DFS(map,start,i,visited);
            }
        }
    }
}

int solution(int n, vector<vector<int>> results) {
    int answer = 0;
    vector<vector<int>> map(n + 1, vector<int>(n + 1));

    for(int i=0;i<results.size();i++){
        map[results[i][0]][results[i][1]]=1;
        map[results[i][1]][results[i][0]]=2;
    }

    for(int i=1;i<=n;i++){
        bool visited[111]={0,};
        visited[i]=true;
        DFS(map,i,i,visited);
    }

    for(int i=1;i<=n;i++){
        int cnt=0;
        for(int j=1;j<=n;j++){
            if(map[i][j]!=0){
                cnt++;
            }
        }
        if(cnt==n-1){
            answer++;
        }
    }
    return answer;
}
