#include <stdio.h>

func10(int x);

main() {
	int a = 1; int b = 3; int c = 5;

	func10(a); // �Լ� ȣ��
	func10(b);
	func10(c);
}

func10(int x) {
	x = x * 10;
	printf("10�谡 �� ���� %d�Դϴ�.\n", x);
}