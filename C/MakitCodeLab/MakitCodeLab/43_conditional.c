#include <stdio.h>

main() {
	int a, b;

	printf("a 입력 값이 10보다 크면 b는 2 그렇지 않으면 b는 1의 값이 됩니다.\n");
	printf("a의 값을 입력하세요: ");
	scanf_s("%d", &a);

	b = a > 10 ? 2 : 1; // 삼항 연산자

	printf("b의 값은 %d입니다.\n", b);
}