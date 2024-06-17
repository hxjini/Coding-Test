#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int num) {
    // 리턴할 값은 메모리를 동적 할당해야 합니다.
    char* answer = (char*)malloc(sizeof(char) * 5); // "Even" 또는 "Odd"를 저장할 메모리 동적 할당

    if(num % 2 == 0) {
        strcpy(answer, "Even"); // 짝수인 경우 "Even" 문자열을 answer에 복사
    } else {
        strcpy(answer, "Odd"); // 홀수인 경우 "Odd" 문자열을 answer에 복사
    }

    return answer; // 문자열 포인터 반환
}