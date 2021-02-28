function solution(A) {
    var obj = A.reduce((a, cur) => {
        a[cur] = a[cur] ? ++a[cur] : 1;
        return a
    }, {})

    for (var key in obj){
        if (obj[key] % 2 == 1) {
            return parseInt(key);
        }
    }
}