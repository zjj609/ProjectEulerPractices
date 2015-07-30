#include <stdio.h>
#include <windows.h>
#include <math.h>

void main()
{
	double a[5000];
	int i=0;
	int j=0;
	double b[50];
	double temp=0;
	FILE *fin;   //定义一个文件指针
	char ch;
	fin=fopen("num2.txt","r");  //用fopen函数打开需要的文件
	if(fin == NULL)   //打开失败
	{
		puts("open file failed!");
		system("pause");
		return ;
	}
	for(;feof(fin) == 0;)   //文件未读取完;feof函数是判断是否到文件尾
	{
		ch=fgetc(fin);   //读取一个字符
//		putchar(ch);   //输出到显示屏
		if(ch>47&&ch<58)
		{
			a[i]=ch-48;
			i++;
		}

	}
	putchar('\n');
	fclose(fin);   //关闭文件


//	printf("%d\n",b);
//	printf("%d\n",temp);
//	system("pause"); 
	for(j=0;j<3;j++)
	{
		b[j]=0;
		for(i=0;i<500;i++)
		{
			if(i%50==j)
			{
				b[j]=b[j]+a[i];
			}
		}
	}
	for(j=1;j<3;j++)
	{
		temp=temp+b[j]*pow(10,(50-j));
	}

	putchar('\n');
	putchar('\n');
	printf("%f",temp);
}