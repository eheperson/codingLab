/*
    int a = {3, 5, 7};
    int* aptr;
    aptr = &a;

    aptr++           : use variable then increase it
    ++aptr           : increase variable then use it
    aptr--           : use variable then decrease it
    --aptr           : decrease variable then use it

    *aptr++          : (*aptr)++
    *++aptr          : *(++aptr)

    ++(*aptr)        : ++a
    &*aptr           : adress of first element of array( adress of 'a')
    &*aptr++         : aptr++
    &*++aptr         : ++aptr
    *(&*++aptr)      : *(++aptr)
    &*(&*++aptr)      : &*(++aptr)


    int* bptr = &*(&*++aptr);
    cout << *(bptr + 1) << endl; //7
    cout << *aptr << endl;   //5
*/

#include <iostream>

using namespace std;
 
#define SIZE 3

// Example macro
// #define bArray b[SIZE]

int main(){
    //assigment of macro definiton above
    //int bArray = {1, 2, 3};

    int a[SIZE] = {1, 2, 3};

    int* aptr = a;
/*
    cout << *(aptr++) << endl;
    cout << *aptr << endl;

    cout << *(++aptr) << endl;
    cout << *aptr << endl;

    cout << *(aptr--) << endl;
    cout << *aptr << endl;

    cout << *(--aptr) << endl;
    cout << *aptr << endl;
*/
    return 0;
}