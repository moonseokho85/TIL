#include <stdio.h>

void bell();

main() {
	bell(); // ù��° �ֹ�
	bell(); // �ι�° �ֹ�
	bell(); // ����° �ֹ�
}

void bell() {
	static int order = 0;

	order++;
	printf("���� �ֹ� ��ȣ�� %d�Դϴ�.\n", order);
}