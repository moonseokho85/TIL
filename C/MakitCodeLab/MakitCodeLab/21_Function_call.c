#include <stdio.h>

int sum(int x, int y); // sum() �Լ� ����

main() {
	int x = 10, y = 20;
	int result;

	result = sum(x, y); // sum() �Լ� ȣ��
	printf("%d + %d = %d\n", x, y, result);
}

// sum() �Լ��� ��ü
int sum(int x, int y) {
	return x + y;
}