#include <stdio.h>
#include <string.h>

static char a[999] = "";

static char* foo(char *input) {
	strcpy(a, input);
	return a;
}

int main()
{
	printf("Hello World\n");
	char *a[999] = {};
	char *b[999] = {};
	char c[250] = "";
	memcpy(&a, &a, sizeof(a) + 999);
	//memcpy(&b, &a, sizeof(a));
	//memset(&c, 'a', 255);
	if (c[-1] == 0) return 1;
	return 0;

	if (c[-1] == 0) return 1;
	foo(c);
}