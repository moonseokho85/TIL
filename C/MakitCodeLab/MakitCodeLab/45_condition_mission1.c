#include <stdio.h>

main() {
	int a, b, result;

	printf("a�� ���� ���� �� �Է�: ");
	scanf_s("%d", &a);

	printf("b�� ���� ���� �� �Է�: ");
	scanf_s("%d", &b);

	if (a > b)
		printf("�Էµ� �� �� �߿� �� ū ���� %d�Դϴ�.\n", a);
	else
		printf("�Էµ� �� �� �߿� �� ū ���� %d�Դϴ�.\n", b);

	result = a > b ? a : b;
	printf("�Էµ� �� �� �߿� �� ū ���� %d�Դϴ�.\n", result);
}