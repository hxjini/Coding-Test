function solution(n) {
    var answer = 0;
    for(let i = 1; i <= 100; i++){
        if((7*i)/n >= 1){
            answer = i;
            break;
        }
    }
    return answer;
}