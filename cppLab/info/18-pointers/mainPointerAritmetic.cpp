////////////////////////////////////////////
//////////////  Pointer Aritmetic
////////////////////////////////////////////

/*
    Pointer Aritmetic : 
        ++ : increment
        -- : decrement

        int a    -> 4 byte
        double b -> 8 byte
        char c   -> 1 byte

        int* aPtr = &a;
        double* bPtr = &b;
        char* cPtr = &c;

        &a = 1000;
        &b = 2000;
        &c = 3000;

        aPtr++ : 1000 + 4  -> int    : 4byte
        bPtr-- : 2000 - 8  -> double : 8byte
        cPtr99 : 3000 + 1  -> char   : 1byte

*/
#include<iostream>

using namespace std;

int main(){

    int a = 13;
    int* aPtr;  
    aPtr = &a;

    cout << "Value of 'aPtr'              : " << aPtr << endl;
    aPtr++; 
    cout << "Value of 'aPtr'              : " << aPtr << endl;
    aPtr++; 
    cout << "Value of 'aPtr'              : " << aPtr << endl;
    aPtr--; 
    cout << "Value of 'aPtr'              : " << aPtr << endl;

    //------------------------------------------------------------
    cout << endl;
    cout << endl;
    //------------------------------------------------------------

    double b = 13.5;
    double* bPtr;  
    bPtr = &b;

    cout << "Value of 'bPtr'              : " << bPtr << endl;
    bPtr++; 
    cout << "Value of 'bPtr'              : " << bPtr << endl;
    bPtr++; 
    cout << "Value of 'bPtr'              : " << bPtr << endl;
    bPtr--; 
    cout << "Value of 'bPtr'              : " << bPtr << endl;

    //------------------------------------------------------------
    cout << endl;
    cout << endl;
    //------------------------------------------------------------

/* use cstdio library to see char variable adress
    char c = 'e';
    char* cPtr;  
    cPtr = &c;

    cout << "Value of 'cPtr'              : " << cPtr << endl;
    cPtr++; 
    cout << "Value of 'cPtr'              : " << cPtr << endl;
    cPtr++; 
    cout << "Value of 'cPtr'              : " << cPtr << endl;
    cPtr--; 
    cout << "Value of 'cPtr'              : " << cPtr << endl;
*/
    return 0;
}






////////////////////////////////////////////
//////////////  Pointer Aritmetic
////////////////////////////////////////////