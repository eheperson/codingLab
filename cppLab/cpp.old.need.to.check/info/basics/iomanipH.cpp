#include<iostream>
#include<iomanip>

using namespace std;

int main(){
    float fVal = 4.34;

    cout << scientific << fVal << endl;
    cout << fixed << fVal << endl;
    cout << setprecision(20) << fixed << fVal << endl;

    return 0;
}