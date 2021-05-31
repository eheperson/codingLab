#include <iostream>

using namespace std;

int main(){
    int x = 50;
    int&r1 = x;

    int& r2 = r1;  // r2 -> x


    cout << "r2 : " << r2;

    r1 ++;

    cout << "r2 : " << r2;
    cout << "x : " << x;

    return 0;
}