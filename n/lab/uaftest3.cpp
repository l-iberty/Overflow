#include <stdio.h>
#include <stdlib.h>

class Fruit
{
private:
	virtual void give_shell()
	{
		printf("You got shell!\n");
	}
public:
	virtual void printMe()
	{
		printf("I am Fruit\n");
	}
};

class Apple: public Fruit
{
public:
	void printMe()
	{
		printf("I am Apple\n");
	}
};

class Orange: public Fruit
{
public:
	void printMe()
	{
		printf("I am Orange\n");
	}
};

void handleObj(Fruit* fruit)
{
	printf("Address: %p\n", fruit);
	fruit->printMe();
}

int main(int argc, char const *argv[])
{
	Fruit* apple = new Apple();
	handleObj(apple);
	int vfp = *(int*)apple;
	delete apple;

	char* buf = new char[4];
	printf("addr buf: %p\n", buf);
	*(int*)buf = vfp;
	handleObj(apple);
	delete buf;

	return 0;
}
