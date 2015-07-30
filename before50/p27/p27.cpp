#include <iostream>
#include <math.h>

using namespace std;

bool IsPrime(int a){

	if(a <= 1)
		return false;
	if(a==2 || a==3)
		return true;

	for(int i = 2;i<=sqrt(a);i++){
		if(a%i == 0)
			return false;
	}
	return true;
}

int Formula(int a,int b,int n,int i){
	if(i==0)
		return (n*n+n*a+b);
	if(i==1)
		return (n*n+n*a-b);
	if(i==2)
		return (n*n-n*a+b);
	if(i==3)
		return (n*n-n*a-b);
	
	return 0;
}


void main(){
	int i,j,k,n;
	int max_a,max_b,max_n,max_i;
	max_a = 0;
	max_b = 0;
	max_n = 0;
	max_i = -1;
	for(i=0;i<4;i++)
		for(j=0;j<1000;j++)
			for(k=0;k<1000;k++){
				n=0;
				while(IsPrime(Formula(j,k,n,i)))
					n++;
				if((n-1)>max_n){
					max_n = n-1;
					max_a = j;
					max_b = k;
					max_i = i;
				}
			}

	cout << max_a << endl;
	cout << max_b << endl;
	cout << max_i << endl;
	cout << max_n << endl;
	cout << max_a * max_b << endl;
}