#include <stdio.h>

main() {
	int a = 1, b;

	b = ++a; // 증감 연산자 ++ 가 변수 a 앞에 놓임

	printf("a의 값은 %d\n", a);
	printf("b의 값은 %d\n", b);
	printf("\n");

	a = 1;
	b = a++; // 증감 연산자 ++ 가 변수 a 뒤에 놓임

	printf("a의 값은 %d\n", a);
	printf("b의 값은 %d\n", b);
}