#include<iostream>
/*

    THAT EXAMPLES ABOUT MASKING


*/
using namespace std;

int g = 90;

int& func(){

    return g;
}

int* foo(){
    return &g;
}

int main(){ 

    cout << "func()  :  " << func() << endl;

    //becauseof the reference return type of func()
    // it becomes like an variable
    // func() is the same thing with g variable for this example
    func() = -1;

    cout << "func()  :  " << func() << endl;

    // some reason ofreference type declaration
    // but this time for pointers.
    *foo() = 56;

    cout << "func()  :  " << func() << endl; 
    
    return 0;
}