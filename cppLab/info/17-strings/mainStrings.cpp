/////////////////////////////////////////////////
//////////////// String example
/////////////////////////////////////////////////

/*
    number definitions : 
        int a = 5;
        double b = 5.1;
        floatt pi = 3.14;

    but what about characters ?????  :

        char -> word, alphabet  : 1byte

        char[] = "Hello"   ->string

    C/C++ :
        C   -> string(char array)
        c++ -> string class
*/

#include<iostream>

using namespace std;


int main(){

    char c = 'H';

    cout << "Size of char : " << sizeof(char) << endl;
    cout << "c : " << c << endl;

    char firstMessage[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
    /*
        arrays have null character from their nature
        but when we declare a char array, 
        we have to append a null character (\0) at the end of the array
        to inform compiter that is the end of the char array.
    */

    cout << "First Message : " << firstMessage << endl;


    return 0;
}


/////////////////////////////////////////////////
//////////////// String example
/////////////////////////////////////////////////