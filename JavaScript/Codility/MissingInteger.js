function solution(A) {
    A.sort(function(a, b){
        return a-b;
    });
    var missingInteger = 1;

    for (var i=0; i < A.length; i++){
        if (A[i] > 0 && A[i] === missingInteger){
            missingInteger++;
        }
    }
    return missingInteger;
}