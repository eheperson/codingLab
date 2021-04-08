/////////////////////////////////////
//  Enum Example    ///////////
/////////////////////////////////////

#include<iostream>
#include <stdio.h>

using namespace std;

enum{
    purple,
    black,
    red = 255, //integer
    green = 140,
    blue = 18,
    orange,
    yellow
} c;

int main(){

    cout << "Purple Type value is   : "<< purple <<endl;
    cout << "Black Type value is   : "<< black <<endl;
    cout << "Red Type value is   : "<< red <<endl;
    cout << "Green Type value is : "<< green <<endl;
    cout << "Blue Type value is  : " << blue <<endl;
    cout << "Orange Type value is   : "<< orange <<endl;
    cout << "Yellow Type value is   : "<< yellow <<endl;

    system("Pause");
    return 0;
}

/*
    Enum :  It is used to assign names to the integral 
            constants which makes a program easy to read and maintain. 
            The keyword “enum” is used to declare an enumeration.

*/

/////////////////////////////////////
//  Enum Example    ///////////
/////////////////////////////////////
