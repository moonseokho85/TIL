#include <stdio.h> // C ǥ�� ���̺귯�� �� �ϳ��� stdio.h ��� ��� ���Ͽ� ����� ������ ����

int function1() {
	return 1; // ����� ��ȯ
}

int function2() {
	return 'A'; // ���ڸ� ��ȯ
}

int function3() {
	int x = 1;
	return x; // ������ ��ȯ
}

double function4() {
	double x = 1.2, y = 3.5;
	return x + y; // ������ ��ȯ
}

main() {
	printf("%d\n", function1());
	printf("%c\n", function2());
	printf("%d\n", function3());
	printf("%f\n", function4());

}


