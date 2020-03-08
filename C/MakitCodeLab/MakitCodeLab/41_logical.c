#include <stdio.h>

main() {
	int a = 5;
	int b = 3;
	int c = 2;

    printf("0 && 0 = %d\n", (a < b) && (b < c)); // °ÅÁş && °ÅÁş
    printf("0 && 1 = %d\n", (a < b) && (b > c)); // °ÅÁş && Âü
    printf("1 && 0 = %d\n", (a > b) && (b < c)); // Âü && °ÅÁş
    printf("1 && 1 = %d\n", (a > b) && (b > c)); // Âü && Âü

    printf("0 || 0 = %d\n", (a < b) || (b < c)); // °ÅÁş || °ÅÁş
    printf("0 || 1 = %d\n", (a < b) || (b > c)); // °ÅÁş || Âü
    printf("1 || 0 = %d\n", (a > b) || (b < c)); // Âü || °ÅÁş
    printf("1 || 1 = %d\n", (a > b) || (b > c)); // Âü || Âü

    printf("!0 = %d\n", !(5 < 3)); // !(°ÅÁş)
    printf("!1 = %d\n", !(5 > 3)); // !(Âü)
}