주어진 move 열을 탐색해서 열이 비어있지 않다면 가장 위에있는 인형을 bucket이라는 스택계념의 vector에 넣어준다
bucket의 top과 현재 넣고자 하는 인형이 같다면 제거해준다

#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    vector<int> bucket;
    int n=board.size();
    int m=board[0].size();

    for(int k=0;k<moves.size();k++){
        int j=moves[k]-1;
        for(int i=0;i<n;i++){
            if(board[i][j]!=0){
                if(bucket.size()!=0&&bucket[bucket.size()-1]==board[i][j]){
                    answer+=2;
                    bucket.pop_back();
                    board[i][j]=0;
                }
                else{
                bucket.push_back(board[i][j]);
                board[i][j]=0;
                   }
                break;
            }
        }
    }
    
    return answer;
}
