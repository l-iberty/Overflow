#include <stdio.h>

int v = 0x12345678;

int main()
{
	char buffer[256];
	fgets(buffer, sizeof(buffer), stdin);
	printf(buffer);
	printf("\nv = 0x%.8x, &v = 0x%.8x\n", v, &v);

	return 0;
}
