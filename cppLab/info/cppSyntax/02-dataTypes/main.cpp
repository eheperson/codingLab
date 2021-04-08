/////////////////////////////////////
//  Data Types Example    ///////////
/////////////////////////////////////

#include<iostream>
#include<stdio.h>

using namespace std;

int main(){

    int a = 5;
    double b = 5.3;
    int c = 5.2;  // Runtime Error

    printf("Begining of C Functions \n");
    printf("Value of C : %d\n", c);
    printf("Value of B : %f\n", b);
    printf("End of C Functions \n\n");

    cout << "Size of char    : " << sizeof(char) << " byte" << endl;
    cout << "Size of int     : " << sizeof(int) << " byte" << endl;
    cout << "Size of double  : " << sizeof(double) << " byte" << endl;
    cout << "Size of float   : " << sizeof(float) << " byte" << endl;
    cout << "Size of boolean : " << sizeof(bool) << " byte" << endl;



    system("Pause");
    return 0;
}

/*
Basic Data Types : 
    type : how many bytes are used.
    
    Primitive built-in types:
        (1) boolean : bool : true,false
        (2) character : char : "abc"
        (3) integer : int
        (4) floating point : float
        (5) double floating point : double
        (6) valueless : void
        (7) wide character : wchar_t
    
    With some specific keywords relation to add before 
    and after to the code wecould change byte size
        (1) signed
        (2) unsigned
        (3) short
        (4) long

*/

/////////////////////////////////////
//  Data Types Example    ///////////
/////////////////////////////////////




