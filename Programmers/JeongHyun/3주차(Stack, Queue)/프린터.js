function solution(priorities, location) {
    var answer = 0;
    //arr = [priorities[i] , i] 로 value/index 를 저장해주기 위한 변수
    let arr = priorities.map((value,index)=>value = [value,index]);
    /*
    1. 우선 순위 최대값 찾기
    2. 대기목록에서 J보다 중요도가 높은 문서가 한개도 없을 때까지 pop하고 push해서 우선 순위가 가장 높은 것이 앞으로 오게 만들기
    3. J를 인쇄하기(pop)해주기(answer++)  => location과 맞는 것이 나올때까지 반복 (x라면 1번으로) (o라면 4번으로)
    4. 같은 것이 나오면 answer값 리턴 
    */
    while(1){ 
        //최대값 찾기
        let maxValue = -1;
        for(let i=0;i<arr.length;++i){
            if(maxValue<arr[i][0])maxValue =arr[i][0];
        }
        //대기목록에서 J보다 중요도가 높은 문서가 한개도 없을 때까지 pop하고 push해서 우선 순위가 가장 높은 것이 앞으로 오게 만들기
        while(maxValue!=arr[0][0]){
            arr.push([arr[0][0],arr[0][1]]);
            arr.splice(0,1);
        }
        //location과 맞는 것인지 여부판단
        if(arr[0][1]==location) return answer+=1;
        else{
            //아니라면 우선순위가 가장 높은 것 인쇄하고 재정렬
            arr.splice(0,1);
            answer++;
        }
    }
    return answer;
}
