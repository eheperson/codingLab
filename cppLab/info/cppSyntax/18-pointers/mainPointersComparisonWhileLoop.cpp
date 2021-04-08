#include<iostream>

using namespace std;

const int SIZE = 3;

int main(){
    int a[SIZE] = {20,200,2000};
    int i;

    int* lastPtr;
    lastPtr = &a[SIZE -1];

    int* aPtr;
    aPtr = a;

    cout << " While loop 1 :::: " << endl;
    i = 0;
    while(i++<SIZE){
        //cout << "a[" << i << "] : " << a[i] << endl;
        cout << "a[" << i << "] : " << *(a + i - 1)<< endl;
    }

    cout << endl;

    cout << " While loop 2 :::: " << endl;
    i = 0;
    while(aPtr++ <= lastPtr){
        i++;
        cout << "a[" << i << "] : " << *(a + i - 1)<< endl;
        //cout << "a[" << i << "] : " << a[i - 1]<< endl;
    }

    
    return 0;
}