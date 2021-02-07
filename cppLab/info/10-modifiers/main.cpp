/////////////////////////////////////
// Constants Example    ///////////
/////////////////////////////////////

/*
    A modifier is used to alter the meaning 
    of the base type so that it more precisely 
    fits the needs of various situations.

    it helps to memory usage restriction

    C++ modifiers :
        signed
        unsigned
        long
        short

    unsigned int -> memory size of the int is changed
    signed a =5 //integer

    bit organization :
        short int          : store values in it's memory from right to left
        unsigned short int : vice-versa of short int 
*/  
#include <iostream>
#include <stdio.h>

using namespace std;

int main(){

    short int i;
    short unsigned int j;

    j = 50000;
    i = j;

    cout << " i : " << i << endl;
    cout << "Size of i : " << sizeof(i) << endl;
    cout << " j : " << j << endl;
    cout << "Size of j : " << sizeof(j) << endl;

    system("Pause");
    return 0;
}


/////////////////////////////////////
// Constants Example    ///////////
/////////////////////////////////////