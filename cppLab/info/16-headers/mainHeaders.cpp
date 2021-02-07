/////////////////////////////////////////////////
////////// header - source file example ////////
/////////////////////////////////////////////////
#include<iostream>
#include<array.hpp>

using namespace std;

#define SIZE 10

//execute
int main(){

    int arr1[SIZE], arr2[SIZE];
    int resultArr[SIZE];
    double meanArray1, meanArray2;
    double sumArray1, sumArray2;
    int* resultArr2;

    initializeArray(arr1, SIZE);
    displayArray(arr1, SIZE);

    initializeArray(arr2, SIZE);
    displayArray(arr2, SIZE);

    meanArray1 = meanArray(arr1, SIZE);
    meanArray2 = meanArray(arr2, SIZE);

    cout << "Mean of Array 1 : " << meanArray1 << endl;
    cout << "Mean of Array 2 : " << meanArray2 << endl;

    sumArray1 = sumArray(arr1, SIZE);
    sumArray2 = sumArray(arr2, SIZE);

    cout << "Sum of Array 1 : " << sumArray1 << endl;
    cout << "Sum of Array 2 : " << sumArray2 << endl;

    cout << endl;
    
    cout << "Substract of two arrays : " << endl;
    substractTwoArray(arr1, arr2, resultArr, SIZE);
    displayArray(resultArr, SIZE);

    cout << "Sum of two arrays : " << endl;
    sumTwoArray(arr1, arr2, resultArr, SIZE);
    displayArray(resultArr, SIZE);

    cout << "Product of two arrays : " << endl;
    productTwoArray(arr1, arr2, resultArr, SIZE);
    displayArray(resultArr, SIZE);

    // En exapmle for different perspective of arrays
    cout << "Substract of two arrays in different perspective : " << endl;
    resultArr2 = substractTwoArray(arr1, arr2, resultArr, SIZE);
    displayArray(resultArr2, SIZE);

    system("Pause");

    return 0;
}



/////////////////////////////////////////////////
////////// header - source file example ////////
/////////////////////////////////////////////////