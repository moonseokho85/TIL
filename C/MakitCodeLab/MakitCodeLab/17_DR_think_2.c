#include <stdio.h>

main() {
	int a = 10; // a 변수 선언과 동시에 10으로 초기화
	int b = 20; // b 변수 선언과 동시에 20으로 초기화
	int temp; // 변수 값을 교환하기 위해 임시로 값을 저장할 변수 선언

	printf("a의 값은 %d이고, b의 값은 %d입니다.\n", a, b);

	temp = a;
	a = b;
	b = temp;

	printf("a의 값은 %d이고, b의 값은 %d입니다.\n", a, b);
}