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
	FILE *fin;   //����һ���ļ�ָ��
	char ch;
	fin=fopen("num2.txt","r");  //��fopen��������Ҫ���ļ�
	if(fin == NULL)   //��ʧ��
	{
		puts("open file failed!");
		system("pause");
		return ;
	}
	for(;feof(fin) == 0;)   //�ļ�δ��ȡ��;feof�������ж��Ƿ��ļ�β
	{
		ch=fgetc(fin);   //��ȡһ���ַ�
//		putchar(ch);   //�������ʾ��
		if(ch>47&&ch<58)
		{
			a[i]=ch-48;
			i++;
		}

	}
	putchar('\n');
	fclose(fin);   //�ر��ļ�


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