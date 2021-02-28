function solution(A) {
    var lenA = A.length;
    var answer = (lenA+1) * (lenA+2) /2;
    for (var i=0; i < lenA; i++){
        answer -= parseInt(A[i]);
    }
    return answer;
}