#include <stdio.h>

void test2(int x);

main() {
	test2(3);
}

void test2(int x) {
	printf("메인 함수로부터 받은 값은 %d입니다.\n", x);
}