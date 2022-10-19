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
