#include <iostream>
#include <math.h>

using namespace std;

void main(){
	const int standmax = 9;
	int i,j,k;
	int count = 0;
	int temp_1,temp_3,temp_5;
	double temp_2,temp_4;
	double temp_i;
	
	for(i=2;i<standmax;i++){
		if(i!=4 && i!=8 && i!=9)
		{
		for(j=2;j<standmax;j++)
			for(k=2;k<standmax;k++){
				temp_1 = j*k;
				temp_i = i+0.0;
				temp_2 = pow(temp_i,k);
				temp_3 = (int)temp_2;
				temp_4 = pow(temp_i,j);
				temp_5 = (int)temp_4;

				if(temp_1 <standmax && temp_3<standmax){
					cout << i << " " << temp_1 <<"   ";
					count++;
				}
				else if(temp_1 <standmax && temp_5<standmax){
					cout << i << " " << temp_1 <<"   ";
					count++;
				}
				else
					break;
			}
		cout << endl;
		}
	}

	cout << count <<endl;
	cout << (standmax-2) *(standmax-2) -count <<endl;
}