function solution(numbers) {
    var answer ='';
  //(b+a) -(a+b) 
  // 6,10 이 있는 경우 '610' , '106' 중 더 큰 수 비교해주기 위함
     function compareNumbers(a,b){
        return (b+a)-(a+b);
    }
  /*
  [6,10,2] => join => 6,10,2 (string) => split(',') => ['6','10','2'] (object) => sort 진행
  string 6,10,2 에서는 sort가 안되기 때문에 각각의 string으로 바꾸어서 진행하였습니다.
  */  
    answer = numbers.join().split(',').sort(compareNumbers).join('');
  // testcase 11에서 실패가 떠서 질문하기에서 예제를 보니 [0,0,0,0] 인 경우 '0'을 return 해줘야하는 규칙을 넣어줬습니다.
    return answer[0]==='0' ? '0' :answer;
}
