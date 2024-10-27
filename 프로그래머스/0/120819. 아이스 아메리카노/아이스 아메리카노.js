function solution(money) {
    const price = 5500;  
    const maxCups = Math.floor(money / price); 
    const remainingMoney = money % price;  
    return [maxCups, remainingMoney];
}