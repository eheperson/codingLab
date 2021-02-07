#include<iostream>

using namespace std;

int main(){
    int x = 50;
    int* ptr = &x;
    int*& r = ptr;  //reference of pointer

    *r = 999;

    cout << " x : " << x << endl;
    cout << " r : " << r << endl; 
    cout << " ptr : " << ptr << endl; 

    cout << endl;

    r++;
    cout << " r : " << r << endl; 

    cout << endl;

    ptr++;
    cout << " ptr : " << ptr << endl;     

    return 0; 
}