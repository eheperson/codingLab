#include<iostream>

using namespace std;

#define SIZE 3

//function declaration
void initializeArray(int* a, int s); //adress, initial adress
void displayArray(int* a, int s);
double meanArray(int* a, int s);

//void initializeArray(int a[SIZE], int s=SIZE); //adress, the whole adress
//void displayArray(int a[SIZE], int s=SIZE);

//void initializeArray(int a[], int s=SIZE); //adress, initial adress
//void displayArray(int a[], int s=SIZE);

int main(){

    int arr[SIZE];
    double meanValue;

    initializeArray(arr, SIZE);

    displayArray(arr, SIZE);

    meanValue = meanArray(arr, SIZE);

    cout << "Mean of the array : " << meanValue << endl;
    //cout << "Mean of the array : " << meanArray(arr, SIZE) << endl;
    
    cout << endl;
    return 0;
}

void initializeArray(int* a, int s){
    for(int i = 0; i<s; i++){
       // a[i] = i; // *(a + i) = i
        *(a+i) = i*10 + 7 - i*i;
    }
}; 

void displayArray(int* a, int s){
    for(int i = 0; i<s; i++){
        cout << "a[" << i << "] : " << a[i] << endl; // *(a + i)
    }
};

double meanArray(int* a, int s){
    int sum = 0;
    double mean;

    for(int i = 0; i<s; i++){
        //sum = sum + a[i];
        sum = sum + *(a+i);
    }

    mean = sum/s;

    return mean;


};