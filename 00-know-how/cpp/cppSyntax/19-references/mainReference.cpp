/*
REFERENCE

    reference : another name of variable
                (pointerlerin yukseltilmis bir seviyesi)
    int x = 34;
    int& = x;

    r -> update aritmetic statement on x

    reference -> masking pointer
*/

#include<iostream>

using namespace std;


void funcPtr(int* x); //call by pointer
void funcRef(int& x); //call by reference


void swapRef(int& x1, int& x2);
void swapPtr(int* x1, int* x2);


int main(){

    int x = 13;
    cout << "x                          : " << x << endl;

    int& r = x;
    r++;
    cout << "x after reference increment: " << x << endl;

    funcPtr(&x);
    cout << "x after funcPtr()          : " << x << endl;

    funcRef(x);
    cout << "x after funcPtr()          : " << x << endl;

    cout << endl;

    int a = 13;
    int b = 21;
    cout << "a : " << a << "  b : "  << b << "<before swap>" << endl;
    swapRef(a,b);
    cout << "a : " << a << "  b : "  << b << "<after swap with reference>" << endl;
    swapPtr(&a ,&b);
    cout << "a : " << a << "  b : "  << b << "<after swap with pointer>" << endl;
    return 0;
}

void funcPtr(int* x){
    *x = 9999;
};

void funcRef(int& x){
    x = 8888;
};

void swapRef(int& x1, int& x2){
    int temp = x1;
    x1 = x2;
    x2 = temp;
};

void swapPtr(int* x1, int* x2){
    int temp = *x1;
    *x1 = *x2;
    *x2 = temp;
};