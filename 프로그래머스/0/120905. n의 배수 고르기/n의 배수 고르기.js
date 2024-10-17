function solution(n, numlist) {
    var answer = [];
    let cnt=0;
    for(let i = 0; i < numlist.length; i++){
        if(numlist[i]%n===0){
            answer[cnt] = numlist[i];
            cnt++;
        }
    }
    return answer;
}