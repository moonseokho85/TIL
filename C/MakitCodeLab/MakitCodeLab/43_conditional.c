#include <stdio.h>

main() {
	int a, b;

	printf("a �Է� ���� 10���� ũ�� b�� 2 �׷��� ������ b�� 1�� ���� �˴ϴ�.\n");
	printf("a�� ���� �Է��ϼ���: ");
	scanf_s("%d", &a);

	b = a > 10 ? 2 : 1; // ���� ������

	printf("b�� ���� %d�Դϴ�.\n", b);
}