function solution(number, k) {
    var answer = '';
    // return 받을 자리수 
    let numberOfDigits =  number.length - k ;
    let startIndex = 0;
    
    for(let i=0;i<numberOfDigits; ++i){
        let maxValue = -1;
        let maxIndex = 0;
        // 범위 설정 이유 :
         ex) "4177952841" ,k = 4 인 경우 원하는 자릿수 6으로
             4 1 7 7 9 | 5 2 8 4 1
                     ↑  
             앞쪽에서 k+1 범위 내에서 가장 큰 수 : 9 , index : k+1 나머지 5자리를 붙여서 만들어야 하기때문에
        for(let j=startIndex; j<=k+i;++j){
            if(maxValue<parseInt(number[j])){
                maxValue = number[j];
                maxIndex = j;
            }
        }
        startIndex = maxIndex+1; 
        answer+=maxValue
    }
    return answer;
}
// 테케 10 : 시간 초과

function solution(number, k) {
    var answer = [];
    for (let i=0;i<number.length;++i){
        while(k>0&&answer[answer.length-1]<number[i]){
            answer.pop();
            k--;
        }
        // answer : 1  number[1] = 9
        // answer : (1) 9  number[2] = 2
        // answer : (1) 9 2 number[3] = 4
        // answer : (1) 9 (2) 4
        answer.push(number[i]);
    }
    console.log(answer);
    // ex) 똑같은 수 나올 경우 "333" while 문에 들어가지 않고 "333"을 전부 return 하게 되기 때문에 원하는 문자열 만큼을 리턴하게 만들어줌 
    return answer.join("").slice(0,number.length-k);
}

[풀이](https://velog.io/@shrup5/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Level2-%ED%81%B0%EC%88%98-%EB%A7%8C%EB%93%A4%EA%B8%B0-Javascript)
