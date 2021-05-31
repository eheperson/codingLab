#include<iostream>

using namespace std;

int main(){

    int x = 13;

    int& r1 = x;
    int& r2 = x;
    int& r3 = x;

    int* p1 = &x;
    int* p2 = &x;
    int* p3 = &x;

    r1++;
    r2++;
    r3++;
    cout << "x after reference increment: " << x << endl;

    (*p1)--;
    (*p2)--;
    (*p3)--;

    cout << "x after pointer decrement: " << x << endl;

    return 0;
}