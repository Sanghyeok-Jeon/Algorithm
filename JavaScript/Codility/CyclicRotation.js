function solution(A, K) {
    var lengthArray = A.length;
    var newArray = A.slice(lengthArray-K%lengthArray);
    newArray.push(...A.slice(0, lengthArray-K%lengthArray));
    return newArray;
}