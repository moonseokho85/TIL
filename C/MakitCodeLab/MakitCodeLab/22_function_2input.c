#include <stdio.h>

double abc(int x, int y);

main() {
	int x, y;
	double z;
	printf("���� x���� �Է�: ");
	scanf_s("%d", &x);

	printf("���� y���� �Է�: ");
	scanf_s("%d", &y);

	z = abc(x, y);
	printf("z�� ����: %f\n", z);
}

double abc(int x, int y) {
	return x + y + 3.14;
}