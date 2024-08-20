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
    

    return pcnt === ycnt;
}