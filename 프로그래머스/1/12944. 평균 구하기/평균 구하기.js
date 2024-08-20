function solution(arr) {
    var answer = 0;
    let cnt = 0;
    let sum = 0;
    for(let i = 0; i<arr.length;i++){
        
        sum += arr[i];
        cnt++;
        answer = sum / cnt;
    }
    return answer;
}