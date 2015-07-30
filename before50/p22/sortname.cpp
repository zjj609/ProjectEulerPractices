#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

int main() {
    int sum = 0;
	int i = 0;
	int j = 0;
	int namesum = 0;
    vector<string> names;
    char name[50], junk[5];
    string str;
    ifstream inFile(".\\names.txt");


    while(inFile.getline(junk, 50, '/"') && inFile.getline(name, 50, '/"')){
        stringstream sstr;
        sstr << name;
        sstr >> str;
        names.push_back(str);
    }

    sort(names.begin(), names.end());

    for(i=0; i<names.size(); i++) {
        namesum = 0;
        for(j=0; j<names[i].size(); j++)
            namesum += (names[i][j] - 64);
        sum += (namesum*(i+1));
    }
	
    cout << "Sum: " << sum << endl;
    return 0;
}