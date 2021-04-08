////////////////////////////////////////////
//////////////  Pointer Aritmetic
////////////////////////////////////////////

#include<iostream>

using namespace std;

#define SIZE 3

int main(){

    int a[SIZE] = {1, 2, 3};

    for(int i = 0; i<SIZE; i++){
        cout << "a[" << i << "] :  " << a[i] << endl;
    }

    cout << "Adress of a : " << endl;

    for(int i = 0; i<SIZE; i++){
        cout << "&a[" << i << "] :  " << &a[i] << endl;
    }

    //------------------------------------------------------------
    cout << endl;
    cout << endl;
    //------------------------------------------------------------

    int* aPtr;
    aPtr = &a[0];

    cout << "aPtr        : " << aPtr << endl;
    cout << "a[0] adress : " << &a[0] << endl;

    cout << endl;

    for(int i = 0; i<SIZE; i++){
        cout << "a[" << i << "] :  " << *aPtr << endl;
        aPtr++;
        //or
        // cout << "a[" << i << "] :  " << a[i] << endl;
        //or
        // cout << "a[" << i << "] :  " << *(aPtr + i) << endl;
    }

    //------------------------------------------------------------
    cout << endl;
    cout << endl;
    //------------------------------------------------------------ 

    int* aPtr2;
    aPtr2 = &a[SIZE -1];

    for(int i = 0; i<SIZE; i++){
        cout << "a[" << i << "] :  " << *aPtr2 << endl;
        aPtr2--;
        //or
        // cout << "a[" << i << "] :  " << a[i] << endl;
        //or
        // cout << "a[" << i << "] :  " << *(aPtr2 - i) << endl;
    }

    //------------------------------------------------------------
    cout << endl;
    cout << endl;
    //------------------------------------------------------------ 

//!!!!!!!!!!!!!!!!!!!!!!!!!!!
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// THAT CODE SECTION  IS IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    int* aPtr3;
    aPtr3 = &a[0];

    for(int i = 0; i<SIZE; i++){
        cout << "a[" << i << "] :  " << aPtr3[i] << endl;
    }
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


    // C O N C L U S I O N
    cout << endl;
    cout << endl;
    cout << "- - - - C O N C L U S I O N - - - -" << endl;
    cout << endl;
    
    int* aPtr4;
    int* aPtr5;
    int* aPtr6;

    aPtr4 = &a[0];
    aPtr5 = &a[0];
    aPtr6 = &a[0];

    for(int i = 0; i<SIZE; i++){
        cout << "a[" << i << "] :  " << *(aPtr4 + i) << endl;
        cout << "a[" << i << "] :  " << *(aPtr5++) << endl;
        cout << "a[" << i << "] :  " << aPtr6[i] << endl;
        cout << "a[" << i << "] :  " << a[i] << endl;
    }

    return 0;
}






////////////////////////////////////////////
//////////////  Pointer Aritmetic
////////////////////////////////////////////