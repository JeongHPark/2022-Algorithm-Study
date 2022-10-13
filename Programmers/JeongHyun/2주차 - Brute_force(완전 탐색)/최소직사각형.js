function solution(sizes) {
    let answer = 0;
    let n =0;
    let rotated = sizes.map(([w,h])=>w<h?[h,w]:[w,h]);
    //rotated 는 sizes의 배열 내에서 w와 h 중 더 큰 수를 왼쪽으로 옮기기 위한 변수입니다.
    rotated.sort((a,b)=>{return b[0]-a[0]});
    //sort를 통해 내림차순으로 정렬
    let max = -1;
    // [1,2] sizes의 1의 원소 중 큰값을 찾기 위한 max값 임의 설정
    for(let i=0;i<rotated.length;++i){
        // rotated의 행(↓)만을 탐색하며 큰수 비교 
        if(rotated[i][1]>max)max = rotated[i][1];
        n++;
    }
    //rotated[0][0]이 가장 큰 원소
    answer = rotated[0][0]*max;
    return answer;
}
