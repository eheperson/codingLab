////////////////////////////////////////////
//////////////  Pointers 
////////////////////////////////////////////

/*
    IF THE ADRESS OF THE ANY VARIABLE IS KNOWN
    THEN
    VALUE OF THAT VARIABLE COULD CHANGE FROM ANYWHERE OF THE PROGRAM

*/
#include<iostream>

using namespace std;

int main(){

    int a = 13;
    int* aPtr;  
 
    cout << "Value of 'a'                 : " << a << endl; // masking pointers

    aPtr = &a;

    cout << "Value of 'aPtr'              : " << aPtr << endl;

    // reaching to the value of the pointed variable from pointer
    // asterix (*) operator
    cout << "Value of 'a' from 'aPtr'     : " << *aPtr << endl; // masking pointers

    return 0;
}






////////////////////////////////////////////
//////////////  Pointers 
////////////////////////////////////////////