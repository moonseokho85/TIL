#include <stdio.h>

int a = 1; // 전역 변수

void func1();

main() {
	int b = 2; // 지역 변수

	printf("여기는 main() 함수입니다.\n");
	printf("main() 함수에서 a값은 %d 입니다.\n", a); // a 값 출력
	printf("main() 함수에서 b값은 %d 입니다.\n", b);

	func1(); // 함수 호출
}

void func1() {
	printf("여기는 func1() 함수입니다.\n");
	printf("func1() 함수에서 a값은 %d 입니다.\n", a); // a 값 출력
	printf("func1() 함수에서 b값은 %d 입니다.\n", b); // b 값 출력
}