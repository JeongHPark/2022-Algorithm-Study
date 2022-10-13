function solution(progresses, speeds) {
    var answer = [];
    let cnt =1; //cnt는 앞 뒤 원소 비교후 앞의 원소가 다음으로 오는 원소보다 작을 때까지 ++ 
    let success = []; // success에 (100-progresses)/speeds = ?(일간 작업 후 배포가 가능한지에 대한 저장소)
    for(let i = 0,standard = 0;i<progresses.length;++i){
        success[i]= Math.ceil((100-progresses[i])/speeds[i]);
        if(success[standard]>=success[i]&& i!==0) cnt++; //i!==0 을 해준 이유는 0번째 원소가 기준되어 시작하기 때문에
        else if(success[standard]<success[i]&&i!==0){
            standard = i; //standard를 i번째 인덱스로 바꿔주고
            answer.push(cnt); //그동안 count 된 값 : cnt 를 answer에 push해주기
            cnt = 1; // 다시 같은 것을 반복해주기 위해 1로 초기화
        }
    }
    answer.push(cnt);
    return answer;
}
