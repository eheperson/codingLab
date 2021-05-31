////////////////////////////////////////////
//////////////  Pointers 
////////////////////////////////////////////
/*
    -binary bit

        ---- ----   8bit = 1byte
        ---- ----
        ---- ----
        ---- ----

        int a = 2;  //variable -> value (mathematic)

        0000 0000   32bit = 4byte
        0000 0000
        0000 0000
        0000 0010

    memory

        0x68        0000 0000   32bit = 4byte
        0x69        0000 0000
        0x70        0000 0000
        0x71        0000 0010

        0x68, 0x69, 0x70, 0x71 : adresses

    !! adresses required to know where our variables are stored

    cout << a << endl;

    to perform that command above,
    the adress of storage of a must be known by compiler
    (somethimes by us)

----------------------------------------------------------------------

        char ch = 'e'   1byte

        0x12    0000 0100

        cout << ch << endl;

        0x12 : adress of ch

----------------------------------------------------------------------

     WE CANNOT DO ANYTHING IN PROGRAMMING WORLD
     WITHOUT RESERVE AREA IN MEMORY
     AND TO RESERVE AREA FROM MEMORY
     WE NEED POINTERS(ADRESSES)
     BEACUSE WITHOUT POINTERS 
     WE CANNOT KNOW WHICH ADRESSES 
     ARE RESERVED FOR OUR VARIABLES, FUNCTIONS ETC.
     
     POINTER -> DATA TYPE CONTAINING THE ADRESS OF SPECIFIC VARIABLES.

     book, pencil   -> variables
     bag or package -> pointer

     int (value) -> int* (adress)

     & : adress operator
     int a;     // variable
     int* ptr;  // pointer variable
     ptr = &a; // ptr will point to the adress of a
     *ptr -> will show the value of a;
     POINTERS POINTS ADRESSES OF ATTACHED VARIABLES

----------------------------------------------------------------------

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!       POINTERS  ARE  THE  POWER  OF  C++  AND  C            !!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

main() function is the first adress of program on the memory 
----------------------------------------------------------------------
int a;              //integer variable
int* aPtr;          //integer pointer variable

double b;           //double variable
double* bPtr;       //double pointer variable

char c;             //char variable
char* cPtr;         //char pointer variable

-POINTERS ARE NOT ONLY STORES THE ADRESSES BUT ALSO STORES THE BYTE LENGTHOF THE VARIABLES
 BECAUSE OF THAT, TYPE OF THE POINTER VARIABLE MUST BE SAME WITH THE POINTED VARIABLE
    int a;
    floar* aPtr;
    aPtr = &a; //error
----------------------------------------------------------------------
*/

#include<iostream>
#include<cstdio>

using namespace std;

int main(){

    int a = 2;
    double b = 3.14;
    char c = 'e';

    cout << "a              : " << a << endl;
    cout << "Size of a      : " << sizeof(a) << endl;
    cout << "Adress of a    : " << &a << endl;

    cout << endl ;

    cout << "b              : " << b << endl;
    cout << "Size of b      : " << sizeof(b) << endl;
    cout << "Adress of b    : " << &b << endl;

    cout << endl;

    cout << "c              : " << c << endl;
    cout << "Size of c      : " << sizeof(c) << endl;
    //cout << "Adress of c    : " << &c << endl;
    // we cannot see the adress of c properly with &c
    // because of the overloading operation
    // to the purpose of seeing adress of c properly
    // use that code below:
    printf("Adress of c     : %p\n", &c);

    //--------------------------------------------------------
    //--------------------------------------------------------
    //--------------------------------------------------------
    cout << endl;
    cout << endl;
    cout << endl;

    int* aPtr;
    double* bPtr;
    char* cPtr;

    aPtr = &a;
    bPtr = &b;
    cPtr = &c;

    cout << "Adress of 'a' with pointer    : " << aPtr << endl;
    cout << "Adress of 'b' with pointer    : " << bPtr << endl;
    // cout << "Adress of 'c' with pointer    : " << cPtr << endl;

    cout << endl;

    cout << "Adress of adress of a : " << &aPtr << endl;

    cout << endl;

    cout << "Size of adress int    : " << sizeof(int*) << endl;
    cout << "Size of adress double : " << sizeof(double*) << endl;
    cout << "Size of adress float  : " << sizeof(float*) << endl;
    cout << "Size of adress char   : " << sizeof(char*) << endl;

    return 0;
}






////////////////////////////////////////////
//////////////  Pointers 
////////////////////////////////////////////