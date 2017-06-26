#include <stdio.h>

int main()
{
	FILE *fp_in, *fp_out;
	int start_off, end_off;
	int len, i;
	char filename[16];
	int ch;
	char buf[4];

	printf("filename: ");
	scanf("%s", filename);
	printf("start_off and end_off: ");
	scanf("%x %x", &start_off, &end_off);

	fp_in = fopen(filename, "rb");
	fp_out = fopen("shellcode.txt", "w");
	fseek(fp_in, start_off, SEEK_SET);

	len = end_off - start_off;
	for (i = 0; i < len; i++)
	{
		ch = fgetc(fp_in);
		sprintf(buf, "\\x%.2x", ch);
		fprintf(fp_out, buf);
	}
	fclose(fp_in);
	fclose(fp_out);
}
