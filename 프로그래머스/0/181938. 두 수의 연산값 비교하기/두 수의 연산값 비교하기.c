#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b) {
    int answer = 0; //반환 값을 담을 변수 초기화
    int c = 10; //c를 10으로 초기화
    while(1){ //b가 c로 나눈 값이 0이 될 때까지 반복
        if(b/c==0){ //만약 b를 c로 나눈값이 0 이면 멈춤
            break;
        }
        c*=10; //c에 10를 곱한값을 c에 정의
    }
    if(a*c+b < 2*a*b){ //a⊕b와 2*a*b 를 비교하여 2*a*b 값이 크면 2*a*b 값 반환
        return 2*a*b;
    }
    else
        return a*c+b; //a⊕b와 2*a*b 를 비교하여 2*a*b 값이 작으면 a*c+b 값 반환
    return answer; //answer의 값 반환
}