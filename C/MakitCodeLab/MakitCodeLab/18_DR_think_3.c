#include <stdio.h>

main() {
	double force_a; // a 포탄의 힘, 세기
	double force_b; // b 포탄의 힘, 세기
	double ratio;

	force_a = 10.5 * 8.4;
	force_b = 12.2 * 6.3;

	ratio = force_a / force_b;

	printf("a 포탄의 힘은 %f, b 포탄의 힘은 %f입니다.\n", force_a, force_b);
	printf("a 포탄이 b 포탄보다 %f배 더 셉니다.\n", ratio);
}