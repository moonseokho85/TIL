#include <stdio.h>

void test3(void);

main() {
	test3();
	test3();
	test3();
}

void test3(void) {
	printf("Hello\n");
}