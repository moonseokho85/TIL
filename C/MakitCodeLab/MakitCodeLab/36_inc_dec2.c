#include <stdio.h>

main() {
	int a = 1, b;

	b = ++a; // ���� ������ ++ �� ���� a �տ� ����

	printf("a�� ���� %d\n", a);
	printf("b�� ���� %d\n", b);
	printf("\n");

	a = 1;
	b = a++; // ���� ������ ++ �� ���� a �ڿ� ����

	printf("a�� ���� %d\n", a);
	printf("b�� ���� %d\n", b);
}