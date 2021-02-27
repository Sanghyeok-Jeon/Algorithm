function solution(array, commands) {
    let answer = [];
    for (let c=0; c < commands.length; c++){
        let arr = array.slice(commands[c][0]-1, commands[c][1]);
        arr.sort(function(a, b){
            return a-b;
        });
        answer.push(arr[commands[c][2]-1])
    }
    return answer;
}