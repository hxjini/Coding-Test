function solution(s){
    var answer = true;
    let pcnt = 0;
    let ycnt = 0;
    s = s.toLowerCase();
    
    for(let i = 0;i<s.length;i++){
        if(s[i] === 'p'){
            pcnt++;
        }
        else if(s[i]=== 'y'){
            ycnt++;
        }
        
    }
    if(pcnt === ycnt){
        answer = true;
    }
    else
        answer = false;
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    console.log(answer);

    return answer;
}