#include <stdio.h>

int main(void) {
    int a;
    int b;
    scanf("%d %d", &a, &b);
    for(int i=0;i<b;i++){ //b만큼 가로줄이 출력된다
        for(int j=0;j<a;j++){//a값만큼 *을 출력한다
            printf("*");
        }
        printf("\n");
    }
    
    return 0;
}