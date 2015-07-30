#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int FindMaxQueue(int a,int b,int i,vector<vector<int> > numbers)
{
	if(a == i-1)
		return numbers[a][b];
	int max;
	int left = FindMaxQueue(a+1,b,i,numbers);
	int right = FindMaxQueue(a+1,b+1,i,numbers);
	if(left>right)
		max = left;
	else 
		max = right;
	return numbers[a][b]+max;
}



int main()
{
//	ifstream input("G:\\test_c\\Cpractice\\problem67\\findmaxse\\findmaxse\\smalldata.txt");
	ifstream input(".\\bigdata.txt");
	if(!input)
	{
		cerr << "can not open the file." <<endl;
		return -1;	
	}

	int i = 0;
	int j = 0;
	int k = 0;
	int temp = 0;
	vector<vector<int> > numbers;
	vector<int> v_temp;

	while(input >> temp)
	{
		v_temp.push_back(temp);
		for(j=0;j<i;j++)
		{
			input >> temp;
			v_temp.push_back(temp);
		}
		numbers.push_back(v_temp);
		v_temp.clear();
		i++;
	}

	cout<< i << endl;
	for(j=0;j<i;j++)
	{
		for(k=0;k<=j;k++)
			cout << numbers[j][k] << " ";
		cout << endl;
	}
	j=0;
	k=0;

	int max = FindMaxQueue(j,k,i,numbers);

	cout << max <<endl;



return 0;
}