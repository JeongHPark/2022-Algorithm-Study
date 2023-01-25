function solution(s){
    
    let current  = 0;
    let arr = s.split(""); //string형  배열 형식으로 바꾸기 => for문을 사용하고 싶어서 바꾸어주었습니다.
    //leftHand : 왼쪽 괄호일 경우의 수 , rightHand : 오른쪽 괄호일 경우의 수
    for(let i = 0,leftHand = 0,rightHand = 0;i<arr.length;++i){
        if(arr[i]==='(') leftHand++;
        else if(arr[i]===')')rightHand++;
       // 예외 발생으로 ()))((() 이런 경우를 걸러주기 위해서
        current = (leftHand-rightHand);
        if(current < 0) { //rightHand가 더 커지는 경우에는 잘못된 경우이기 때문에 return false;
            return false;
        }
    }
    return current === 0 ? true : false;  //current 값이 0이라면 true 아니라면 false로 리턴해주기
}

//다른 사람의 풀이 참조로 재풀이
function solution(s){
    let current =0;
    for(let parenthesis of s){  //굳이 배열로 바꾸지 않아도 되는 것을 알게되어 수정
        current += parenthesis === '(' ? 1 : -1; // ( 라면 1을 아니라면 -1을 parenthesis에 대입해줘 current로 매상황을 판단
        if(current<0) return false;
    }
    return current ===0 ? true : false;
}
