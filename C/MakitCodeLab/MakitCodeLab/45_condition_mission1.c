#include <stdio.h>

main() {
	int a, b, result;

	printf("a의 양의 정수 값 입력: ");
	scanf_s("%d", &a);

	printf("b의 양의 정수 값 입력: ");
	scanf_s("%d", &b);

	if (a > b)
		printf("입력된 두 수 중에 더 큰 값은 %d입니다.\n", a);
	else
		printf("입력된 두 수 중에 더 큰 값은 %d입니다.\n", b);

	result = a > b ? a : b;
	printf("입력된 두 수 중에 더 큰 값은 %d입니다.\n", result);
}