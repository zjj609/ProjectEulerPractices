#include <iostream>
#include <time.h>

using namespace std;

int FindDigitNumber(int n)
{
	int *p = new int[n];
	int i = 0;
	int current = 1;
	int yushu = 0;
	bool cycle = false;

	for( ; i<n ; i++)
	{
		p[i] = 0;
	}

	yushu = 10 % n;
	p[yushu] = current;
	while(yushu !=0)
	{
		yushu = 10 * yushu % n;
		if(p[yushu]!=0)
		{
			cycle = true;
			break;
		}
		else
		{
			current++;
			p[yushu] = current;
		}
	}

	if(cycle)
		return current+1-p[yushu];
	else
		return 0;
}

void main()
{
	double start;
	double end;
	start = clock();
	int max = 0;
	int temp = 0;
	int max_a = 0;
	for(int a = 2;a<100000;a++)
	{
		temp = FindDigitNumber(a);
		if(temp>max)
		{
			max = temp;
			max_a = a;
		}
	}
	end = clock();
	cout << max << " " << max_a <<endl;
	cout << (end-start)/1000 << endl;
}