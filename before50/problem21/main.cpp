#include <stdio.h>
#include <windows.h>
#include <math.h>


int dd(int r)
{
	int sum=0;
	int i;
	for(i=1;i<r;i++)
	{
		if(r%i==0)
		{
			sum=sum+i;
		}
	}
	return sum;
}

void main()
{



int j;
int a;
int b;
int sumsum=0;

for(j=1;j<10000;j++)
{
	a=dd(j);
	b=dd(a);
	if(j==b&&a!=j)
	{
		sumsum=sumsum+j;
		printf("%d %d\n",j,a);
	}

}
printf("%d\n",sumsum);



}

