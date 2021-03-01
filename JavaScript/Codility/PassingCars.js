function solution(A) {
    var answer = 0;
    var cntZero = 0;

    for (var i=0; i < A.length; i++){
        if (A[i] === 0) {
            cntZero++;
        }
        else {
            answer += cntZero;
            if (answer > 1000000000) {
                return -1;
            }
        }
    }
    return answer;
}