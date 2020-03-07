#include <stdio.h> // C 표준 라이브러리 중 하나인 stdio.h 라는 헤더 파일에 선언된 내용을 포함

int function1() {
	return 1; // 상수를 반환
}

int function2() {
	return 'A'; // 문자를 반환
}

int function3() {
	int x = 1;
	return x; // 변수를 반환
}

double function4() {
	double x = 1.2, y = 3.5;
	return x + y; // 수식을 반환
}

main() {
	printf("%d\n", function1());
	printf("%c\n", function2());
	printf("%d\n", function3());
	printf("%f\n", function4());

}


