#include <stdio.h>

main() {
	int a;

	printf("���� ������ �Է��ϼ���: ");
	scanf_s("%d", &a);

	if (a % 2) // a % 2�� 1�̶��, �� if(1)�� ������ �����Ѵٴ� �ǹ�
		printf("�Է��� ���� ������ Ȧ���Դϴ�.\n");
	else
		printf("�Է��� ���� ������ ¦���Դϴ�.\n");
}