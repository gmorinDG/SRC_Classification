#include <stdio.h>
#include <time.h>

struct Filler 
{
	int rows;
	char *pieces;
};


int main() 
{
	struct Filler pyramid = {1, ". "};
	int i;
	int j;
	int k;
	int rows;

	printf("Row Filler\n");
	printf("Enter number of rows: ");
	scanf("%d", &rows);
	
	pyramid.rows = rows;
	pyramid.pieces = "* ";

	for (i=1; i <= (pyramid.rows + pyramid.rows); ++i)
	{
		if (i > pyramid.rows)
		{
			for (k=j-1; k >= 1; --k)
			{
				printf(pyramid.pieces);
			}
			j -= 1; 
	
		}
		else
		{
			for (j=1; j <= i; ++j)
			{
				printf(pyramid.pieces);
			}
		}
		printf("\n");
	}
	return 0;
}

/* example company ip */
