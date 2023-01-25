
function solution(name) {
    // 'A'~'Z' : 65~90
    let answer = 0; 
    const nameLength = name.length;
    let move = nameLength - 1; //오른쪽으로 모두 이동하였을 때의 count
    for(let i=0;i<nameLength;++i){
        // ▲ ▼ 부분
        
        //name.charCodeAt(i) => name의 i번째 인덱스의 아스키 코드값 - 65('A'의 아스키 코드값) 
        let howManyClickButton = name.charCodeAt(i)-65; 
        // 알파벳의 개수 26개, 반으로 나누어 13보다 큰 값이면 'Z'부터 count하는게 더 최소.
        if(howManyClickButton>13) howManyClickButton = (26- howManyClickButton); 
        answer+=howManyClickButton;
        
        // ◀ ▶ 부분
        //풀이 아래 README.MD에서 설명 수기로 작성
        let x = i+1;
        while(x<nameLength &&name[x]=='A') x++;
        move = Math.min(move,i+nameLength-x+Math.min(i,nameLength-x));
    }
    answer+=move;
    return answer;
}
