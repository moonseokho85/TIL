#include <stdio.h>

void bell();

main() {
	bell(); // 첫번째 주문
	bell(); // 두번째 주문
	bell(); // 세번째 주문
}

void bell() {
	static int order = 0;

	order++;
	printf("현재 주문 번호는 %d입니다.\n", order);
}