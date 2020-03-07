#include <stdio.h>

func10(int x);

main() {
	int a = 1; int b = 3; int c = 5;

	func10(a); // 함수 호출
	func10(b);
	func10(c);
}

func10(int x) {
	x = x * 10;
	printf("10배가 된 값은 %d입니다.\n", x);
}