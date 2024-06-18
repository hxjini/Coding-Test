#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) 
{
int answer = 0; //answer라는 변수 선언

if(n%2!=0){ //n이 홀수라면
    for(int i=0;i<=n;i++){ //for문으로 들어가 n이하의 홀수인 모든 양의 정수의 합을 구한다
        if(i%2!=0)
            answer+=i;
    }
}
else{ //n이 짝수라면
    for(int i=0;i<=n;i++){ //for문으로 들어가 n이하의 짝수인 모든 양의 정수의 제곱의 합을 구한다
      if(i%2==0)
          answer+=i*i;
  }
}
return answer;
}