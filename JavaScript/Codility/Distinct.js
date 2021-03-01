function solution(A) {
    var newSet = new Set();

    for (var i=0; i < A.length; i++){
        newSet.add(A[i]);
    }
    return newSet.size;
}