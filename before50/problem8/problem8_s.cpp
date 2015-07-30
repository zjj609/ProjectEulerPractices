#include <stdio.h>
#include <windows.h>

void main()
{
	int a[1000];
	int i=0;
	int b=0;
	int temp;
	FILE *fin;   //定义一个文件指针
	char ch;
	fin=fopen("num1.txt","r");  //用fopen函数打开需要的文件
	if(fin == NULL)   //打开失败
	{
		puts("open file failed!");
		system("pause");
		return ;
	}
	for(;feof(fin) == 0;)   //文件未读取完;feof函数是判断是否到文件尾
	{
		ch=fgetc(fin);   //读取一个字符
		putchar(ch);   //输出到显示屏
		if(ch>47&&ch<58)
		{
			a[i]=ch-48;
			i++;
		}

	}
	putchar('\n');
	fclose(fin);   //关闭文件

	for(i=0;i<996;i++)
	{
		temp=a[i]*a[i+1]*a[i+2]*a[i+3]*a[i+4];
			if(temp>b)
			{
				b=temp;
			}
	}

	printf("%d\n",b);
	printf("%d\n",temp);
//	system("pause"); 
	for(i=0;i<10;i++)
	{
		printf("%d ",a[i]);
	}

	putchar('\n');
}