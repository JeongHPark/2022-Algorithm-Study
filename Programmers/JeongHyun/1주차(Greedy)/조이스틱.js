
function solution(name) {
    // 'A'~'Z' : 65~90
    let answer = 0;
    const nameLength = name.length;
    let move = nameLength - 1;
    for(let i=0;i<nameLength;++i){
        let howManyClickButton = name.charCodeAt(i)-65;
        if(howManyClickButton>13) howManyClickButton = (26- howManyClickButton);
        answer+=howManyClickButton;
        let x = i+1;
        while(x<nameLength &&name[x]=='A') x++;
        
        move = Math.min(move,i+nameLength-x+Math.min(i,nameLength-x));
    }
    answer+=move;
    return answer;
}