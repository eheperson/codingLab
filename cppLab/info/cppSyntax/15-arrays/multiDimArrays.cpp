/////////////////////////////////////
// Arrays Example    ///////////
/////////////////////////////////////

/*
    1D Array  : vector
        int a[3] = {1,2,3};     3x1

        a[3] -> integer value
        a    -> pointer

    2D Array : matrix

        int a[4][5];
        <type> <arrayName>[<Size1>][<Size2>]

        a[4][5] -> integer value
        a[0][]  -> pointer
        a[1][]  -> pointer
        a[2][]  -> pointer
        a       -> pointer to pointer
        ---------------------------------
        a[3][3]

        1,2,3
        4,5,6
        7,8,9

        1 -> a[0][0]
        2
        3

        4 -> a[1][0]
        5
        6

        7 -> a[2][0]
        8
        9
        


*/


#include <iostream>
#include <stdio.h>

using namespace std;

#define SIZE1 2
#define SIZE2 2
#define SIZE3 2

int main(){

    //decleration
    //but no initializatin
    // garbage values
    int a[SIZE1][SIZE2];

    //initialization and decleration
    int b[SIZE1][SIZE2] = {{1,2}, {3,4}};
    //  b -> adress of adress
    //  b[] -> adress
    int c[SIZE1] = {3,4}; 
    // c-> adress

    //initialization and decleration
    int d[3][3] = {{1,2,3}, {4,5,6}, {7,8,9}};

    for(int i =0; i < SIZE1; i++){
        for(int j = 0; j < SIZE2; j++){
            cout << "b[" << i << "][" << j << "] : " << b[i][j] << endl;
        }
    }

    int e[SIZE1][SIZE2][SIZE3];
    // size3 -> integer
    // size2 -> integer adress
    // size2 -> integer adress of adress
    // e -> integer adress of adress of adress 
    
    return 0;
}


/////////////////////////////////////
// Arrays Example    ///////////
/////////////////////////////////////