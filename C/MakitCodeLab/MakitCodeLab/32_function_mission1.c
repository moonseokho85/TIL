#include <stdio.h>

int func1(void) {
	return 1;
}

char func2(void) {
	return 'a';
}

void func3(void) {
	printf("hello\n");
}

double func4() {
	float v;

	printf("�Ǽ� v���� �Է�: ");
	scanf_s("%f", &v);
	
	return v;
}

main() {
	printf("%d\n", func1());
	printf("%c\n", func2());
	func3();
	printf("%f\n", func4());
}