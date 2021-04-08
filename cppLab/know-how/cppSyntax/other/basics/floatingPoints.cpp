#include<iostream>
#include<iomanip>

using namespace std;

int main(){
    float fVal = 125.34632;
    double dVal = 125.34632;
    long double ldVal = 125.346323843847384;


    cout << sizeof(float) << endl;
    cout << setprecision(20) << fixed << fVal << endl;

    cout << sizeof(double) << endl;
    cout << setprecision(20) << fixed << dVal << endl;

    cout << sizeof(long double) << endl;
    cout << setprecision(20) << fixed << ldVal << endl;


    return 0;
}