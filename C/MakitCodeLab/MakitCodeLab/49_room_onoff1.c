#include <stdio.h>

main() {
	// 8개 방에 대한 정수형 변수를 각각 생성, 4 * 8 = 32 바이트 사용
	// 각 변수가 0이면 불이 꺼진 (off) 상태, 1이면 켜진(on) 상태
	// 모든 방을 불이 꺼진 상태로 초기화
	int room1 = 0, room2 = 0, room3 = 0, room4 = 0;
	int room5 = 0, room6 = 0, room7 = 0, room8 = 0;

	// 2번 방과 7번 방의 불을 켜진(on) 상태로 변경
	room2 = room7 = 1;

	// 1번 방, 2번 방, 7번 방의 불의 상태를 확인하여 출력
	if (room1 == 1) // if (room1)로 표현 가능
		printf("1번 방의 불은 켜져(on) 있습니다.\n");
	else
		printf("1번 방의 불은 꺼져(off) 있습니다.\n");
	if (room2 == 1)
		printf("2번 방의 불은 켜져(on) 있습니다.\n");
	else
		printf("2번 방의 불은 꺼져(off) 있습니다.\n");

	if (room7 == 1)
		printf("7번 방의 불은 켜져(on) 있습니다.\n");
	else
		printf("7번 방의 불은 꺼져(off) 있습니다.\n");
}