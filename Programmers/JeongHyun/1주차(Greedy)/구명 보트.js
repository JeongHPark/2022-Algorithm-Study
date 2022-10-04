function solution(people, limit) {
    var answer = people.length;
    people.sort((a,b)=>{
        return a-b; // 50, 50, 70, 80 으로 정렬
    })
    console.log(people);
    let start = 0; //시작 index
    let end = people.length-1;  //people index 끝 value
    while(start<end){
        /* 50 50 70 80   50 50 70 80   50 50 70 80  50 50 70 80  50 50 70 80
           ↑        ↑     ↑     ↑       ↑     ↑      ↑  ↑           ↑↑ : answer--
          start     end
        */
        if(people[start]+people[end]<=limit){ 
            answer--;
            start++;
            end--;
        }
        else end--;
    }
    return answer;
}

//안지호님의 조언을 듣고 풀이를 진행하였습니다. 조언 감사합니다.
