// source code, implementations, definitions
#include<iostream>
#include "array.hpp"

using namespace std;

void initializeArray(int* a, int size){
    for(int i = 0; i<size; i++){
        a[i] = i + 1;
    };
};


void displayArray(int* a, int size){
    cout << endl << "Array Start" << endl;
    for(int i = 0; i< size; i++){
        cout << "array[" << i << "] : " << a[i] << endl;
    };
        cout  << "Array End" << endl << endl;
};

double sumArray(int* a, int size){
    double sum = 0.0;
    for(int i = 0; i<size; i++){
        sum = sum + *(a + i);
    };
    return sum;
};

double meanArray(int* a, int size){
    double mean = 0.0;
    mean = sumArray(a, size) / size;
    return mean;
};

int* sumTwoArray(int* arr1, int* arr2, int* resArr, int size){
    for(int i=0; i<size; i++){
        resArr[i] = *(arr1 +i) + *(arr2 +i);
    }
    return resArr;
}; 

int* substractTwoArray(int* arr1, int* arr2, int* resArr, int size){
    for(int i=0; i<size; i++){
        resArr[i] = *(arr1 +i) - *(arr2 +i);
    }
    return resArr;
}; 

int* productTwoArray(int* arr1, int* arr2, int* resArr, int size){
    for(int i=0; i<size; i++){
        resArr[i] = *(arr1 +i) * *(arr2 +i);
    }
    return resArr;
}; 