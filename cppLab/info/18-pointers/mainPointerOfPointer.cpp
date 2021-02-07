#include<iostream>

using namespace std;

int main(){

    int a = 13;
    
    int* aPtr;
    aPtr = &a;
    cout << " Adress of a                : " << aPtr << endl;

    // to reach an adress of pointer
    // we need to declare different type of variable 
    // with double asterix (**)
    int **aPtrPtr;
    aPtrPtr = &aPtr;
    cout << " Adress of aPtr             : " << aPtrPtr << endl;

    //// adress of adress of adress of adress of........
    int ***aPtrPtrPtr;
    aPtrPtrPtr = &aPtrPtr;
    cout << " Adress of aPtrPtr          : " << aPtrPtrPtr << endl;

    int ****aPtrPtrPtrPtr;
    aPtrPtrPtrPtr = &aPtrPtrPtr;
    cout << " Adress of aPtrPtrPtr       : " << aPtrPtrPtrPtr << endl;

    int *****aPtrPtrPtrPtrPtr;
    aPtrPtrPtrPtrPtr = &aPtrPtrPtrPtr;
    cout << " Adress of aPtrPtrPtrPtr    : " << aPtrPtrPtrPtrPtr << endl;

    int ******aPtrPtrPtrPtrPtrPtr;
    aPtrPtrPtrPtrPtrPtr = &aPtrPtrPtrPtrPtr;
    cout << " Adress of aPtrPtrPtrPtrPtr : " << aPtrPtrPtrPtrPtrPtr << endl;

    cout << endl;

    cout << "---------------------------------------------------" << endl;
    cout << " C++ allows us to use 14 asterix : **************" << endl;
    cout << " It means 14 adresses of adresses" << endl;
    cout << "---------------------------------------------------" << endl;

    cout << endl;

    cout << "a values from pointers   ::::::::::::::::::::" << endl;
    cout << "a value from aPtr               :" << *aPtr << endl;
    cout << "a value from aPtrPtr            :" << **aPtrPtr << endl;
    cout << "a value from aPtrPtrPtr         :" << ***aPtrPtrPtr << endl;
    cout << "a value from aPtrPtrPtrPtr      :" << ****aPtrPtrPtrPtr << endl;
    cout << "a value from aPtrPtrPtrPtrPtr   :" << *****aPtrPtrPtrPtrPtr << endl;

    cout << endl;

    cout << "Size of int*      : " << sizeof(int*) << endl;
    cout << "Size of int**     : " << sizeof(int**) << endl;
    cout << "Size of int***    : " << sizeof(int***) << endl;
    cout << "Size of int****   : " << sizeof(int****) << endl;
    cout << "Size of int*****  : " << sizeof(int*****) << endl;

    
/* That section is not clear. It will be revised
    cout << " Pointer to pointer in 2D arrays : " << endl;

    int b[2][2] = {{1, 2}, {3, 4}};

    int* bPtr;
    int** bPtr2;

    // bPtr = &b; //error
    //bPtr2 = &b;

*/
    return 0;
}