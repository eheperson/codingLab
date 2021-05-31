/////////////////////////////////////
//  Typedef Example    ///////////
/////////////////////////////////////

#include<iostream>
#include<stdio.h>

using namespace std;

typedef double pressUnit;
// double -> pressUnit
// change the name of variable keyword
typedef char String; //char -> String
typedef int integer; //int -> integer

int main(){

    pressUnit pressMeasurement;
    pressUnit pressMeasurement2;

    pressMeasurement = 5.4;
    pressMeasurement2 = 6.7;

    cout << "First Pressure Value : " << pressMeasurement <<endl;
    cout << "Second Pressure Value : "<< pressMeasurement2 <<endl;

    system("Pause");
    return 0;
}

/*
    Typedef : The C programming language provides a keyword called typedef, 
              which you can use to give a type a new name. 
*/

/////////////////////////////////////
//  Typedef Example    ///////////
/////////////////////////////////////
