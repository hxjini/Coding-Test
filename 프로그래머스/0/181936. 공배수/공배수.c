#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
// number가 n과 m으로 모두 나누어 떨어지는지 확인하는 함수
int solution(int number, int n, int m) {
    int answer = 0;//반환 값을 담을 변수 초기화
    if (number % n == 0 && number % m == 0){ //number가 n과 m으로 나누어 떨어지는지 확인
        return 1; //나누어 떨어지면 1 반환
    }
    else
        return 0; //나누어 떨어지지 않는다면 0 반환
    return answer;//answer 값 반환
}