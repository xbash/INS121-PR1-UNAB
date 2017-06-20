#include <stdio.h>
#include <stdlib.h>

int main()
{
	int a = 3, *b = NULL;
	printf ("a = %d\n", a);
	b = &a;
	printf ("b = %p\n", b);
	printf ("*b = %d\n", *b);
	return EXIT_SUCCESS;
}