#include <stdio.h>

main() {
	int a = 10;
	int b = 20;

	printf("a의 값은 %d이고, b의 값은 %d입니다.\n", a, b);

	a = 20;
	b = 10;

	printf("a의 값은 %d이고, b의 값은 %d입니다.\n", a, b);
}