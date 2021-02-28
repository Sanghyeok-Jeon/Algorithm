function solution(A) {
    var sumPartFirst = 0;
    var sumPartSecond = A.reduce((total, a) => total+a, 0);
    var answer = null;

    for (var i=0; i<A.length-1; i++){
        sumPartFirst += A[i];
        sumPartSecond -= A[i];
        
        var diffSum = Math.abs(sumPartFirst - sumPartSecond);
        if (answer === null || diffSum < answer){
            answer = diffSum;
        }
    }
    return answer;
}