// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(N, A) {
    var counter = new Array(N);
    for (var i=0; i < N; i++){
        counter[i] = 0;
    }
    var maxCounter = 0;
    var lastMaxCounter = 0;

    for (var K=0; K < A.length; K++){
        if (A[K] === N+1){
           lastMaxCounter = maxCounter;
        }
        else {
            if (counter[A[K]-1] < lastMaxCounter){
                counter[A[K]-1] = lastMaxCounter;
            }
            
            counter[A[K]-1]++;
            
            if (counter[A[K]-1] > maxCounter){
                maxCounter = counter[A[K]-1];
            }
        }
    }
    
    for (var i=0; i < N; i++){
        if (counter[i] < lastMaxCounter){
            counter[i] = lastMaxCounter;
        }
    }

    return counter;
}