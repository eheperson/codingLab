//////////////////////////////
//////////////////////////////
///// System Dynamics

#include<iostream>
#include<sysdyn.hpp>

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

    //assigment of initial conditions
    x[0] = x0;

    ///////////// Input and State Iitialization

    //input variable initialization
    initi(u, SIZE, 10.0);

    //state variable initialization
    inits(x, SIZE, 1.2, 0.0);

    //////////////////// Iteration

    //forward difference solver
    fwdDifS(x, u, SIZE, dt, a, b);
    //display system results
    disp(x, u, SIZE);

    cout << endl;
    cout << " Backward Difference Solver Results : " << endl;

    //backward difference solver
    backDifS(x, u, SIZE, dt, a, b);
    //display system results
    disp(x, u, SIZE);

    cout << endl;
    cout << " Backward Difference Solver Results : " << endl;
    
    //central difference solver
    centralDifS(x, u, SIZE, dt, a, b);
    //display system results
    disp(x, u, SIZE);
    return 0;
}










//////////////////////////////
//////////////////////////////
///// System Dynamics


