function solution(X, A) {
    var setPosition = new Set();

    for (var i=0; i < A.length; i++){
        setPosition.add(A[i]);
        if (setPosition.size === X){
            return i;
        }
    }
    return -1;
}