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

    for(int i = 0; i<20; i++){
        aPtr++;
        cout << "aPtr " << i << " " << (*aPtr) << endl;
    }

    cout << endl;
    cout << endl;

    for(int i = 0; i<10; i++){
        aPtr--;
        cout << "aPtr " << i << " " << (*aPtr) << endl;
    }


    return 0;
}






////////////////////////////////////////////
//////////////  Pointer Aritmetic
////////////////////////////////////////////