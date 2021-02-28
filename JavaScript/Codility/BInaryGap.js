function solution(N) {
    var binaryN = N.toString(2);
    var maxGap = 0;
    var tmpGap = 0;

    for (var i=0; i<binaryN.length; i++){
        if (binaryN[i] == "1"){
            if (tmpGap > maxGap){
                maxGap = tmpGap;
            }
            tmpGap = 0;
        }
        else {
            tmpGap += 1;
        }
    }
    return maxGap;
}