#include <stdio.h>

main() {
	int a, b, c;

	printf("���� �ٸ� ���� 3���� �Է��ϼ���:\n");
	printf("a = ");

	scanf_s("%d", &a);
	printf("b = ");

	scanf_s("%d", &b);
	printf("c = ");

	scanf_s("%d", &c);

	if ((a > b) && (a > c))
		printf("a�� b�� c���� ū ���̴�.\n");
	else
		printf("a�� ��� b�� c�� �ϳ� ���ٴ� �۴�.\n");

	if ((b > a) || (b > c))
		printf("b�� ��� a�� c�� �ϳ� ���ٴ� ũ��.\n");
	else
		printf("b�� ���� ���� ���̴�.\n");
}