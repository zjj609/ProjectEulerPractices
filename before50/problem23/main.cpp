#include <stdio.h>
#include <windows.h>
#include <math.h>


int overnum(int r)
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

int notwoab(int r)
{
	int i;
	int a=0;
	for(i=1;i<(r/2+1);i++)
	{
		if(overnum(i)>i && overnum(r-i)>(r-i))
		{	
			a=1;
			break;
		}
	}
	if(a==1){return r;}
	else return 0;

}

void main()
{
	int i;
	int b;
	int sum=0;
	for(i=1;i<28124;i++)
	{
		b=notwoab(i);
		sum=sum+b;
		printf("%d ",b);
	}
printf("%d \n",sum);

//	printf("%d ",overnum(12));
//	printf("%d ",notwoab(24));
}