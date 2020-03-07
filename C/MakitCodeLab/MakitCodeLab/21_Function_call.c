#include <stdio.h>

int sum(int x, int y); // sum() 함수 선언

main() {
	int x = 10, y = 20;
	int result;

	result = sum(x, y); // sum() 함수 호출
	printf("%d + %d = %d\n", x, y, result);
}

// sum() 함수의 몸체
int sum(int x, int y) {
	return x + y;
}