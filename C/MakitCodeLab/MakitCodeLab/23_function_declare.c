#include <stdio.h>

double abc(int x, int y) { // 함수 선언과 동시에 정의
	return x + y + 3.14;
}

main() {
	int x, y;
	double z;

	printf("정수 x의 값 입력:");
	scanf_s("%d", &x);

	printf("정수 y의 값 입력:");
	scanf_s("%d", &y);

	z = abc(x, y);
	printf("z의 값은: %f\n", z);
}