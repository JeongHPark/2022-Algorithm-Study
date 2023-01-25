function solution(array, commands) {
    var answer = [];
    for(let i=0;i<commands.length;++i){
        let arr = [];
        /*
        commands 
        commands[i][0]-1 = 1
        commands[i][1] = 5
        commands[i][2]-1 = 2
        */ 
        for(let j=commands[i][0]-1;j<commands[i][1];++j){
            arr.push(array[j]);
        }
        arr.sort((a,b)=>a-b);
        answer.push(arr[commands[i][2]-1]);
    }
    return answer;
}


function solution(array, commands) {
    var answer = [];
    answer = commands.map(a=>{
        // map은 commands를 이용하여 answer을 만들어주는 함수로서
        // a[0]-1 을 하면 commands[i][0] - 1로 범위만큼 array를 자릅니다.
        // .sort를 통해 정렬한 뒤 a[2]-1 만을 리턴해줍니다. 이 과정을 commands의 length만큼 진행합니다.
        return array.slice(a[0]-1,a[1]).sort((b,c)=>b-c)[a[2]-1];
    })
    return answer;
}
