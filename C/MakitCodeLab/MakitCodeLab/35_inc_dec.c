#include <stdio.h>

main() {
	int a = 1, b = 1;

	a++;
	++b;

	printf("a의 값은 %d\n", a); // 증감 연산자 + +을 사용하여 a를 1 증가
	printf("b의 값은 %d\n", b); // 증감 연산자 + +을 사용하여 b를 1 증가

	a--;
	--b;

	printf("a의 값은 %d\n", a); // 증감 연산자 - -를 사용하여 a를 1 감소
	printf("b의 값은 %d\n", b); // 증감 연산자 - -를 사용하여 b를 1 감소
}