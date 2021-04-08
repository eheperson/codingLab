#include<iostream>

using namespace std;

#define SIZE 3

void initializeArray(int*, int);
void displayArray(int*, int);


int main(){
    
    int a[SIZE] = {3, 5, 7};

    initializeArray(a, SIZE);
    displayArray(a, SIZE);


    return 0;
}

void initializeArray(int* aptr, int size){
    /*
    *(aptr + 0) = 11;
    *(aptr + 1) = 12;
    *(aptr + 2) = 13;
    */
    
    // check the displayArray() function scope 
    // to read about firstPtr
    int* lastPtr = aptr + size;
    int i = 0;
    int* firstPtr = aptr;
    while(aptr < lastPtr){
        *firstPtr++ = i*i;
        //*firstPtr++ = (i*i) + (i*i);
        //*firstPtr++ = (i++) + (i - 1);
        i++;
    }


}


void displayArray(int* aptr, int size){
    int* lastPtr = aptr + size;
    int i = 0;
    // aptr is a parameter cames from outside of the function scope
    // we could walk in memory through aptr
    // but if we try to increase aptr
    // that could be a problem
    // to avoid that problem
    // assign aptr to a new pointer variable    
    
    // use firtptr instead of aptr 
    int* firstPtr = aptr;
    while(firstPtr < lastPtr){
    // while(aptr < lastPtr){
        //cout << "a[" << i << "] : " << *(aptr + i) << endl; 
        cout << "a[" << i << "] : " << firstPtr << endl; 
        i++;
        // aptr++;
        firstPtr++;
    }
}
