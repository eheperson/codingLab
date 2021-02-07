#include<iostream>

using namespace std;


int main(){

    const int x = 50;

    // error : int* ptr = &x;
    const int* ptr = &x;

    // *ptr = 40;  error: x is constant

    ptr++; //that is not error.
            // we cannot change const int x,
            // but we can change const int* ptr;

    // if we want user cannot change ptr :
    const int* const   ptr2 = &x; 

    //int& r = x  -> error
    
    //not error
    const int& r = x;
    return 0;
}