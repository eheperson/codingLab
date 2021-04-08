/////////////////////////////////////
// Arrays Example    ///////////
/////////////////////////////////////



#include <iostream>
#include <stdio.h>

using namespace std;

int main(){

    int array[10];

    for (int i = 0; i<10; i++){
        array[i] = 0;
    }

    for (int i = 0; i<10; i++){
        cout << "a[" << i << "] :" << array[i] << endl;
    }

    
    // Segmentation fault
    // Runtime Error
    // if that adree is used by different application
    // that line below will return segmentation fault
    // otherwise, there is no any error, everything will run erfect
    // a little bit luck
    // array[450] = 10; 

    cout << endl;
    cout << endl;
    cout << "Another Example " << endl;
    int j = 0;
    while(j<10){
        array[j++] = j;
        cout << "index " << j << " : " << array[j-1] << endl;
    }

    cout << endl;
    cout << endl;
    cout << "Another Example " << endl;
    int k = 0;
    while(k++<10){
        array[k - 1] = k;
        cout << "index " << k - 1 << " : " << array[k-1] << endl;
    }

    system("Pause");
    return 0;
}


/////////////////////////////////////
// Arrays Example    ///////////
/////////////////////////////////////