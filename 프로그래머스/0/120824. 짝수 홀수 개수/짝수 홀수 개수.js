function solution(num_list) {
    var answer = [];
    let ecnt = 0;
    let ocnt = 0;
    for(let i = 0; i<num_list.length;i++){
        if(num_list[i]%2===0){
            ecnt++;
        }
        else{
            ocnt++;
        }
    }
    answer[0] = ecnt;
    answer[1] = ocnt;
    return answer;
}