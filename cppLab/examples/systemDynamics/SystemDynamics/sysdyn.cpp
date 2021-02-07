// source code, implementations, definitions
#include<iostream>
#include "sysdyn.hpp"

using namespace std;

void disp(double* state, 
          double* input,
          const int SIZE){

    for(int i = 0; i < SIZE; i++){
        //cout << "State : " << state[i] << "Input : " << input[i] << endl;
        cout << "State : " << *(state + i) << "Input : " << *(input + i) << endl;
    }
};


void inits(double* state, 
             const int SIZE,
             double value,
             double initCond){
/* or
    for(int i = 0; i<SIZE; i++){
        state[i] = value;
    }

    state[0] = initCond;
*/

/*or
    int i = 0;
    while(i<SIZE){
        state[i] = value;
        i++;
    }

    *state = initCond;
    //or 
    //*(state + 0) = initCond;
*/

    double *ptrLast = &state[SIZE - 1];
    *state++ = initCond;
    while(state < ptrLast){
        *state++ = value;
    }
}


void initi(double* state, 
           const int SIZE,
           double value){
    
    for(int i = 0; i<SIZE; i++){
        state[i] = value;
    }

    state[0] = initCond;      
}

void fwdDifS(double* state, 
             double* input, 
             const int SIZE,
             double dt,
             double firstCoef,
             double secCoef){

    for(int i = 0; i<SIZE; i++){
        state[i + 1] = state[i] + dt*(firstCoeff*state[i] + secCoeff*input[i]);
    }           
}

void backDifS(double* state, 
             double* input, 
             const int SIZE,
             double dt,
             double firstCoef,
             double secCoef){

    for(int i = 1; i<SIZE; i++){
        state[i] = state[i-1] + dt*(firstCoeff*state[i-1] + secCoeff*input[i-1]);
    }           
}

void centralDifS(double* state, 
             double* input, 
             const int SIZE,
             double dt,
             double firstCoef,
             double secCoef){

    for(int i = 0; i<SIZE; i++){
        state[i + 1] = state[i-1] + 2*dt*(firstCoeff*state[i-1] + secCoeff*input[i-1]);
    }           
}