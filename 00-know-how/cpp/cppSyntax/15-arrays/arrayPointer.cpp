#include<iostream>

using namespace std;

#define SIZE1 3

int main(){

    int arr[SIZE1] = {1,2,3};
    // arr : adress, pointer

    int* arrPtr; 
    // arrPtr : adress, pointer

    arrPtr = arr;

    for(int i =0; i<SIZE1; i++){
        cout << "arr[" << i << "] :" << arr[i] << endl;
    } 

    cout << endl;

    for(int i =0; i<SIZE1; i++){
        cout << "arrPtr[" << i << "] :" << arrPtr[i] << endl;
    } 

    cout << endl;

    cout << "Adress of arr[]  : " << arr << endl;
    cout << "Adress of arrPtr : " << arrPtr << endl;

    return 0;
}