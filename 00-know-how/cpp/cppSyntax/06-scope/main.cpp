/////////////////////////////////////
//  Scope Example    ///////////
/////////////////////////////////////
/*
    A scope is a region of the program and broadly speaking 
    there are three places, where variables can be declared :
        (1) Inside a function or a block which is called local variables,
        (2) In the definition of function parameters which is called formal parameters.
        (3) Outside of all functions which is called global variables

    !! Scopes works hierarchically !!
*/
#include<iostream>
#include<stdio.h>

using namespace std;

//global scope
int c = 13; // global variable

int main(){
    //function scope
    int a = 5;
    int b = 10;

    { //internal scope
        int a = 7; //local variable
        cout << "Internal Scope " << a << endl; 
        cout << "Internal Scope " << b << endl; 
        cout << "Internal Scope " << c << endl; 

    }

    cout <<"Function Scope " << a << endl;
    cout <<"Function Scope " << b << endl;
    cout <<"Function Scope " << c << endl;

    
    system("Pause");
    return 0;
}


/////////////////////////////////////
//  Scope Example    ///////////
/////////////////////////////////////