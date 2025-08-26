#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    string s1, s2;
    cin >> s1;
    cin >> s2;

    int cnts1 = count(s1.begin(), s1.end(), 'a');
    int cnts2 = count(s2.begin(), s2.end(), 'a');

    if (cnts1 >= cnts2)
        cout<<"go";
    else
        cout<<"no";

    return 0;
}
