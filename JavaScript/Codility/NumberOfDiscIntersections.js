function solution(A) {
    var newArray = [];
    for (var i=0; i < A.length; i++){
        newArray.push({a:i-A[i], b:i+A[i]});
    }
    newArray.sort((a,b) => (a.a-b.a));

    var result = 0;
    for (var i=0; i < newArray.length-1; i++){
        for (var j=i+1; j <newArray.length; j++){
            if (newArray[i].b >= newArray[j].a){
                result++;
            }
            else{
                break;
            }
            if (result > 10000000){
                return -1;
            }
        }
    }
    return result;
}