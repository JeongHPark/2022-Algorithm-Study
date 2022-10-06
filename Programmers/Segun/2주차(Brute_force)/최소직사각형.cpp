//주어진 가로,세로 길이중 작은 값들중에 최댓값을 구하고
//주어진 가로, 세로 길이중 큰 값들중에 최댓값을 구해서 곱해준다.

#include <string>
#include <vector>
#include<algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int max1=0,max2=0;
    for(int i=0;i<sizes.size();i++){
        max1=max(max1,min(sizes[i][1],sizes[i][0]));    //가로 세로 중 작은 값들중의 최댓값
        max2=max(max2, max(sizes[i][1],sizes[i][0]));   //가로 세로 중 큰 값들중의 최댓값
    }
    return max1*max2;
}
