/////////////////////////////////////
// Constants Example    ///////////
/////////////////////////////////////

/*
    (1) Literal : number and symbol
           85 -> int
           36.02 -> double
           30u -> unsigned int
           45l -> long int

    (2) In C++, thera are two ways to define constants
        - using #define preprocessor
        - using const keyword

        !! User cannot change the constants !!
*/  
#include <iostream>
#include <stdio.h>

#define LENGTH 5
#define WIDTH 5

using namespace std;
int main(){

    int area = LENGTH*WIDTH;

    const int L = 50;
    const int W = 30;

    int area2 = L*W; 

    cout << "Area 1  : " << area << endl;
    cout << "Area 2  : " << area2 << endl;

    system("Pause");
    return 0;
}


/////////////////////////////////////
// Constants Example    ///////////
/////////////////////////////////////