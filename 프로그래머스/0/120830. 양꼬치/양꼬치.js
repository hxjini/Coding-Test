function solution(n, k) {
    var answer = 0;
    let free = Math.floor(n / 10)
    answer = 12000 * n + 2000*(k-free);
    return answer;
}