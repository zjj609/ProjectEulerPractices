#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream input("simple_tri.txt");
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

	while(input >> temp)
	{
		numbers[i].push_back(temp);
		for(j=0;j<i;j++)
		{
			input >> temp;
			numbers[i].push_back(temp);
		}
		i++;
	}

	for(j=0;j<i;j++)
	{
		for(k=0;k<=j;k++)
			cout << numbers[j][k];
		cout << endl;
	}


return 0;
}