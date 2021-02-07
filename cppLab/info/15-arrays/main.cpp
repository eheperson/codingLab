/////////////////////////////////////
// Arrays Example    ///////////
/////////////////////////////////////

/*
    C++ provides a data structure, the array, which stores 
    a fixed-size sequential collection of elements of the same type. 
    An array is used to store a collection of data, but it is often 
    more useful to think of an array as a collection of variables of the same type.

    Arrays :
        (1) Data in organized form
        (2) No Adress Required

    Array Declaration : 
    -----------------------------
    main -> adress
    () -> calling
    main()
    -----------------------------
    [] -> calling
    arrayName ->adress

    Syntax :
        <type> <array_name>[<array_size>]
        
        int a[10]
            int(2byte)
            a-> start adress
            2*10 = 20 byte in memory
    -----------------------------

*/  
#include <iostream>
#include <stdio.h>

using namespace std;

int main(){

    //initialization 

    int a[5]; //garbage value

    int b[5] = {1,2,3}; //initial value
    //b[0]=1, b[1]=2, b[2]=3, b[3]=NULL (\0) 
    //NULL (\0) character : end of the array

    int c[] = {8, 7, 6};


    cout << "first element of a : " << a[0] << endl;
    cout << "first element of a : " << a[1] << endl;
    cout << "first element of a : " << a[2] << endl;
    cout << endl;
    cout << "first element of b : " << b[0] << endl;
    cout << "first element of b : " << b[1] << endl;
    cout << "first element of b : " << b[2] << endl;
    cout << endl;
    cout << "first element of c : " << c[0] << endl;
    cout << "first element of c : " << c[1] << endl;
    cout << "first element of c : " << c[2] << endl;
    cout << endl;
    
    //assigment
    a[0] = 10;
    a[1] = 11;
    a[2] = 12;

    cout << "After Assigment :" << endl;
    cout << "first element of a : " << a[0] << endl;
    cout << "first element of a : " << a[1] << endl;
    cout << "first element of a : " << a[2] << endl;

    system("Pause");
    return 0;
}


/////////////////////////////////////
// Arrays Example    ///////////
/////////////////////////////////////