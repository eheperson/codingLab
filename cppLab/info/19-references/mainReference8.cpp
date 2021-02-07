/*

  references are only meaningfull for compilers.

    The difference between reference and pointer types:
        - reference only stores pointer, pointer stores whatever
            int*& r = ptr;
            int*& r2   = r;

            int* ptr = &a;
            ptr = *b;

        - reference cannot hold reference
            int &r = 1;
            int &r2 = r;
            int& r3 = r2;

            all of them are same

        - void pointer can be used, void reference cannot be used.
            void *
            void & -> syntax error;

        - pointer array, 
            int **a = {&b, &c, &d, ..}

        - reference array does not exist
            int& r = {r1, r2, r3} -> syntax error

        - NULL reference does not exit, pointer has

        -references must mask anything.
            int& r1 = 10; -> syntax error

            but : 

            const int& r = 10; //not error //temporary object

        -thing to be masked must have an initial value.

        -int* ptr = 10; // C lang - no error, C++ lang - syntax error
        
        -int x = 10;
         double* ptr = &x; // C - no error, C++ - error
        
        but : 
            int x = 10;
            const doube &dr = x;

*/

#include<iostream>

using namespace std;

int main(){
    
    int a[10] = {0};

    // masking pointer type of arrays by reference
    int (&r)[10] = a;

    for(int i = 0; i<10; i++){
        cout << r[i] << "  ";
    }

    cout << endl;

    int* ptr = r;
    *r = 99;
    *(a + 1) = 13;
    *(r+2) = 20;
    
    for(int i = 0; i<10; i++){
        cout << r[i] << "  ";
    }

    cout << endl;

    int b = 10;
    int &r2 = b;
     //(&r2 + 2) -> systax error

    return 0;
}