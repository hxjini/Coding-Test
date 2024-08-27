function solution(numbers, num1, num2) {
    var answer = [];
    let cnt = 0;
    for(let i = num1; i<=num2;i++){
        answer[cnt]= numbers[i];
        cnt++;
    }
    
    return answer;
}