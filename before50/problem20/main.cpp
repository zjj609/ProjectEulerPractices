#include <stdio.h>
#include <windows.h>
#include <math.h>

void main()
{

double a=1;
double b;
double i;
double sum=0;
div_t x;

for(i=1;i<31;i++)
{
	a=a*i;
}
printf("%f\n",a);

while(a!=0)
{
	x=div(a,10);
	a=x.quot;
	b=x.rem;
	sum=sum+b;

}

printf("%f\n",sum);

}