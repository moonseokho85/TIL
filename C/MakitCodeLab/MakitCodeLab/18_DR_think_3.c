#include <stdio.h>

main() {
	double force_a; // a ��ź�� ��, ����
	double force_b; // b ��ź�� ��, ����
	double ratio;

	force_a = 10.5 * 8.4;
	force_b = 12.2 * 6.3;

	ratio = force_a / force_b;

	printf("a ��ź�� ���� %f, b ��ź�� ���� %f�Դϴ�.\n", force_a, force_b);
	printf("a ��ź�� b ��ź���� %f�� �� ���ϴ�.\n", ratio);
}