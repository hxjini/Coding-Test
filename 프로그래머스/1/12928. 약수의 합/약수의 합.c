#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0; //answer 라는 변수 선언
    for (int i= 1; i <= n; i++){ //n의 약수를 찾기 위해 for문 사용
        if(n % i == 0){ // n이 i로 나누어 떨어지면
            answer += i; // answer에 i를 더해준다
        }

    }
    return answer; //answer 값 반환
}