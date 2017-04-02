#include <stdio.h>
#include <stdlib.h>

void get_shell()
{
	printf("Shell got!\n");
	system("/bin/sh");
}


int test()
{
	int i;
	int buf[3] = { 1, 2, 3};

	printf("get_shell addr: %d\n",(int) get_shell);
	while (1) {
		printf("index, (-1) to quit: ");
		scanf("%d", &i);
		if (i == -1) break;

		printf("item: ");
		scanf("%d", &buf[i]);
	}

	return 0;
}

int main()
{
	test();
	return 0;
}
