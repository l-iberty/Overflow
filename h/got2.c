#include <stdio.h>


int main()
{
  char *name1, *name2;
  unsigned int addr,value;
  printf("What's your name?\n");
  name1 = (char *)malloc(64);
  name2 = (char *)malloc(64);
  fgets(name1, 64, stdin);
  printf("Please input again\n");
  fgets(name2, 64, stdin);
  if (strcmp(name1,name2)!=0)
  {
    printf("Authenticate failed!\n");
    return 0;
  }
  free(name2);
  printf("Hello %sThis time, I'll show you more technique in stack overflow.\n", name1);
  printf("But I'm not willing to tell you hint directly,so discover by yourself.\n");
  printf("I promised that you can solve it by what you learned so far.\n");
  printf("Which address you wanna read:");
  scanf("%d",&addr);
  value = *(unsigned int *)addr;
  printf("%#x\n",value);
  printf("What value you wanna write in the address:");
  scanf("%d",addr);
  free(name1);
  return 0;
}
