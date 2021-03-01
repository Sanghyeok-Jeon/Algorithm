function solution(S, P, Q) {
    var answer = [];

    for (var i=0; i < P.length; i++){
        var tmpS = S.slice(P[i], Q[i]+1);

        if (tmpS.indexOf('A') !== -1){
            answer.push(1);
        }
        else if (tmpS.indexOf('C') !== -1){
            answer.push(2);
        }
        else if (tmpS.indexOf('G') !== -1){
            answer.push(3);
        }
        else {
            answer.push(4);
        }
    }
    return answer;
}