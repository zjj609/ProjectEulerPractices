#include <stdio.h>
#include <windows.h>

void main()
{
	int a[1000];
	int i=0;
	int b=0;
	int temp;
	FILE *fin;   //����һ���ļ�ָ��
	char ch;
	fin=fopen("num1.txt","r");  //��fopen��������Ҫ���ļ�
	if(fin == NULL)   //��ʧ��
	{
		puts("open file failed!");
		system("pause");
		return ;
	}
	for(;feof(fin) == 0;)   //�ļ�δ��ȡ��;feof�������ж��Ƿ��ļ�β
	{
		ch=fgetc(fin);   //��ȡһ���ַ�
		putchar(ch);   //�������ʾ��
		if(ch>47&&ch<58)
		{
			a[i]=ch-48;
			i++;
		}

	}
	putchar('\n');
	fclose(fin);   //�ر��ļ�

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