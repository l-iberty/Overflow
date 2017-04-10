#include <stdio.h>

int target = 0x12345678;

int main(int argc, char **argv)
{
	printf("target = 0x%.8x, &target = 0x%.8x\n\n", target, &target);
	char buffer[512];
	fgets(buffer, sizeof(buffer), stdin);
	printf(buffer);

	printf("Now, target = 0x%.8x\n\n", target);
	return 0;
}
