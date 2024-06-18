#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
// num이 n으로 나누어 떨어지는지를 확인하는 함수
int solution(int num, int n) {
    int answer; //answer라는 변수 선언
    if(num % n == 0){ // num을 n으로 나누었을 때 나머지가 0이면
        answer = 1;   // answer을 1로 초기화
    }
    else if(num % n != 0){ // num을 n으로 나누었을 때 나머지가 0이 아니면
        answer = 0;        // answer을 0으로 초기화
    }
    return answer; //answer의 값 반환
}