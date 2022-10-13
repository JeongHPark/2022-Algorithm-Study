function solution(arr)
{
    var answer = [];// 정답이 들어가는 배열
    answer.push(arr[0]); // arr의 첫번째 원소를 정답에 넣어주기
    let start = 0; // answer의 맨뒤의 원소와 비교해주기 위해서 따로 변수를 두기
    for(let i=0;i<arr.length;++i){
      // 만약 answer의 마지막 원소와 arr[i]의 원소가 다를때만 answer에 푸시해주기
        if(answer[start]!==arr[i]){ 
            answer.push(arr[i]);
            start++;    
        }
    }
    return answer;
}
