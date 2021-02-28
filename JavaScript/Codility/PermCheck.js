function solution(A) {
    A.sort(function(a, b){
        return a-b;
    });
    var answer = 1

    for (var i=0; i < A.length; i++){
        if (i+1 !== A[i]){
            answer = 0;
        }
    }

    return answer;
}