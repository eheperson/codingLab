#include<iostream>

using namespace std;

#define SIZE 3

int main(){

    int arr[SIZE] = {100,200,300};
    // arr : adress, pointer

    int* arrPtr; 
    // arrPtr : adress, pointer

    arrPtr = arr;

    /*
        arr[i] => *(arr + i)
        * => asterix operator, reaching value within its adress
        & => adress operator, adress of some variable type 
    */


    for(int i =0; i<SIZE; i++){
        cout << "Via Array : " << endl;
        cout << "arr[" << i << "]           : " << arr[i] << endl;
        cout << "arr[" << i << "]           : " << *(arr + i) << endl;
        cout << "Adress of arr[" << i << "] : " << &arr[i] << endl;
        cout << "Adress of arr[" << i << "] : " << (arr + i) << endl;

        cout << "Via Adress : " << endl;
        cout << "arrPtr[" << i << "]           : " << *(arrPtr + i) << endl;        
        cout << "Adress of arrPtr[" << i << "] : " << (arrPtr + i) << endl; 
        cout <<  endl;
        cout <<  endl;
    } 



    return 0;
}