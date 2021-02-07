//////////////////////////////
//////////////////////////////
///// System Dynamics

#include<iostream>

using namespace std;

int main(){

    ////////////// System Parameters

    //sampling time
    double dt = 0.01;    

    // time parameters for simulation and iterations
    double tinit = 0.0;
    double tfinal = 5.0;

    //initial conditions for solvers
    double x0 = 0.0;

    //system coefficients
    double a = -2;
    double b = 1;

    const int SIZE = (tfinal - tinit)/dt;

    //system array
    double x[SIZE];  //system state array
    double u[SIZE];  //system input array


    ///////////// Input and State Iitialization

    //input variable initialization
    for(int i = 0; i<SIZE; i++){
        u[i] = 5;
    }

    //state variable initialization
    for(int i = 0; i<SIZE; i++){
        x[i] = 0;
    }

    //assigment of initial conditions
    x[0] = x0;


    ///////////////////// Iteration

    for(int i = 0; i<SIZE; i++){
        /* Forward Difference Iteration*/
        x[i + 1] = x[i] + dt*(a*x[i] + b*u[i]);
        cout << "State : " << x[i] << "   |   " << "Input : " << u[i] << endl; 
    }
    return 0;
}


//////////////////////////////
//////////////////////////////
///// System Dynamics


