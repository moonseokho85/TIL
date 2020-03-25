#include <stdio.h>

main() {
	char room = 0;
	int i, j;

	printf("2번 방과 7번 방의 불을 on합니다.\n\n");

	room |= 2;  // 0000 0010 마스크와 비트 OR연산으로 두 번째 비트를 켬
	room |= 64; // 0100 0000 마스크와 비트 OR연산으로 일곱 번째 비트를 켬

	if (room & 1) // & 연산자로 0000 0001 비트가 켜져 있는지 확인
		printf("1번 방은 켜져(on) 있습니다.");
	else
		printf("1번 방은 꺼져(off) 있습니다.");
	if (room & 2)  // & 연산자로 0000 0010 비트가 켜져 있는지 확인, 2번 방 확인
		printf("2번 방은 켜져(on) 있습니다.\n");
	else
		printf("2번 방은 꺼져(off) 있습니다.\n");

	if (room & 64) // & 연산자로 0100 0000 비트가 켜져 있는지 확인, 7번 방 확인
		printf("7번 방은 켜져(on) 있습니다.\n");
	else
		printf("7번 방은 꺼져(off) 있습니다.\n");

	printf("\n");

	printf("2번 방의 불을 끄겠습니다\n");

	room &= ~2; // 2번 방의 비트를 1 -> 0으로 반전하고 & 연산

	if (room & 2) // & 연산자로 0000 0010 비트가 켜져 있는지 확인
		printf("2번 방은 켜져(on) 있습니다.\n");
	else
		printf("2번 방은 꺼져(off) 있습니다.\n");
	
	printf("\n");

	printf("1번 방이 켜져 있다면 끄고 꺼져 있다면 켜겠습니다.\n");

	room ^= 1;

	if (room & 1) // & 연산자로 0000 0001 비트가 켜져 있는지 확인
		printf("1번 방은 켜져(on) 있습니다.\n");
	else
		printf("1번 방은 꺼져(off) 있습니다.\n");
	printf("\n");

	printf("현재 모든 방의 점등 상태를 확인하겠습니다!\n");

	for (i = 1, j = 1; i <= 128; i = i * 2, j++) {
		if (room & i)
			printf("%d번 방은 켜져(on) 있습니다.\n", j);
		else
			printf("%d번 방은 꺼져(off) 있습니다.\n", j);
	}
}