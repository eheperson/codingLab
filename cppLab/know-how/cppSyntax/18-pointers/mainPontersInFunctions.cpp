#include<iostream>

using namespace std;


// declaration (function prototypes)

void changeVariableNormal(int, int);
// to overload changeVariableNormal() function
// void changeVariableNormal(int *, int);
void changeVariablePointer(int*, int);



int main(){
    int a = 3;
    cout << "Initial value of 'a'                       : " << a << endl;
    
    changeVariableNormal(a, 7);
    cout << "Value of 'a' after changeVariableNormal()  : " << a << endl;

    changeVariablePointer(&a, 7);
    cout << "Value of 'a' after changeVariablePointer() : " << a << endl;



    return 0;
}

//function definitions 
void changeVariableNormal(int n, int value){
    n = value;
};

void changeVariablePointer(int* nptr, int value){
    *nptr = value;
};