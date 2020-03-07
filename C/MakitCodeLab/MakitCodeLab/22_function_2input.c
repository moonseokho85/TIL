#include <stdio.h>

double abc(int x, int y);

main() {
	int x, y;
	double z;
	printf("정수 x값의 입력: ");
	scanf_s("%d", &x);

	printf("정수 y값의 입력: ");
	scanf_s("%d", &y);

	z = abc(x, y);
	printf("z의 값은: %f\n", z);
}

double abc(int x, int y) {
	return x + y + 3.14;
}