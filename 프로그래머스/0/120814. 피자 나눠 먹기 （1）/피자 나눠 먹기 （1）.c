#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    for(int i = 1; i <= 100; i++){
        if((7*i)/n >= 1){
            answer = i;
            break;
        }
    }
    
    return answer;
}