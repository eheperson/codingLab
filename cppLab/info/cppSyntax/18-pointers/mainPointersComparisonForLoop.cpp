#include<iostream>

using namespace std;

const int SIZE = 3;

int main(){
    int a[SIZE] = {20,200,2000};
    int i;
    int* lastPtr;
    lastPtr = &a[SIZE -1];
    //int* aPtr;
    //aPtr = (a + 0);

    i = 0;
    cout << " For loop 1 :::: " << endl;
    for(int* aPtr = a; aPtr<=lastPtr; aPtr++){
        cout << "a[" << i << "] : " << *aPtr << endl;
        i++;
    }

    cout << endl;

    int* lastPtr2;
    lastPtr2 = a + (SIZE - 1);

    cout << "lastPtr2[0]   : " << lastPtr2[0] << endl;
    cout << "a[0]         : " << a[0] << endl;
    cout << "lastPtr2[-2]  : " << lastPtr2[-2] << endl;
    cout << "a[0]         : " << a[0] << endl;
    cout << "lastPtr2[-1]  : " << lastPtr2[-1] << endl;
    cout << "a[0]        : " << a[0] << endl;

    cout << endl;

    int* lastPtr3;
    lastPtr3 = a + (SIZE - 1) + 5;

    i = 0;
    cout << " For loop 2 :::: " << endl;
    for(int i =( -2 - 5); i < (-2 + 3  - 5); i++){
        cout << "lastPtr3[" << i << "] : " << lastPtr3[i] << endl;
    }

    cout << endl;

    int* lastPtr4;
    lastPtr4 = a + (SIZE - 1);

    i = 0;
    cout << " For loop3  :::: " << endl;
    for(int i = -2 ; i < (-2 + 3); i++){
        cout << "lastPtr4[" << i << "] : " << lastPtr4[i] << endl;
    }

/*
    // I M P O R T A N T
    for(int i = 0; i<SIZE; i++){
        cout << "a[i] : " << *a << endl;
        a++; // error
        // adress of array is not changeable
        // cannot be incremented 
        // or
        // cannot be decremented
        // because if the adress of array is changed,
        // all values of array must be move to another array
        // C++ does not allow tochange array adresses
    }
*/ 
  
    return 0;
}