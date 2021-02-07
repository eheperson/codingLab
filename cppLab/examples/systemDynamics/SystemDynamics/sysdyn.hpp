//declerations
#ifndef __SYSDYN_HPP__
#define __SYSDYN_HPP__

/*
    ax^2 + bx + c = 0
    (x - x1)*(x - x2) = 0  // root

    xdot = dx/dt

    xdot = a*x^2  //continuous

    Matlab -> Standard Solution

    We cannot use continuous time in computers or microprocessors 
    we have to convert continuous expression to disctrete

    solver(forward - difference - central)

    example :
        (1) discreetzation

        xdot = ( x[i+1] - x[i])/dt = a*x[i]

        x[i + 1] = x[i] + dt*(a*x[i]) //forward difference solver

    Mechatronic -> System -> w.r.t time -> require solver
    Matlab : Library of solvers


    -- SOLVERS : 
        forward differential solver  -> x[i+1] - x[i]   = dx
        backward differential solver -> x[i]   - x[i-1] = dx
        central differential solver  -> x[i+1] - x[i-1] = dx

*/

////////////////////////////////////////////////////////////////////////////////
// STANDARD FUNCTIONS BEGIN
/*disp() : To display system results*/

void disp(double* state, 
          double* input,
          const int SIZE);

// STANDARD FUNCTIONS END
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
// SOLVER DYNAMIC FUNCTIONS BEGIN


void fwdDifS(double* state, 
             double* input, 
             const int SIZE,
             double dt,
             double firstCoef,
             double secCoef);
/*fwdDifS() : Forward Difference Solver
    forward difference :
        x[1] = x[0] + dt(a*x[0] + b*u[0])
        x[2] = x[1] + dt(a*x[1] + b*u[1])
        x[3] = x[2] + dt(a*x[2] + b*u[2])
        ...
        ...
        ...
        x[n] = x[n-1] + dt(a*x[n-1] + b*u[n-1])
*/


void backDifS(double* state, 
             double* input, 
             const int SIZE,
             double dt,
             double firstCoef,
             double secCoef);
/*backDifS() : Backward Difference Solver
    forward difference :
        x[1] = x[0] + dt(a*x[0] + b*u[0])
        x[2] = x[1] + dt(a*x[1] + b*u[1])
        x[3] = x[2] + dt(a*x[2] + b*u[2])
        ...
        ...
        ...
        x[n] = x[n-1] + dt(a*x[n-1] + b*u[n-1])
*/


void centralDifS(double* state, 
             double* input, 
             const int SIZE,
             double dt,
             double firstCoef,
             double secCoef);
/*centralDifS() : Central Difference Solver
    forward difference :
        x[1] = x[0] + dt(a*x[0] + b*u[0])
        x[2] = x[1] + dt(a*x[1] + b*u[1])
        x[3] = x[2] + dt(a*x[2] + b*u[2])
        ...
        ...
        ...
        x[n] = x[n-1] + dt(a*x[n-1] + b*u[n-1])
*/

// SOLVER DYNAMIC FUNCTIONS END
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
// ARRAY OPERATIONS BEGIN

/*inits() : state variables init fcn*/
void inits(double* state, 
             const int SIZE,
             double value,
             double initCond);


/*initi() : input variables init fcn*/
void initi(double* state, 
           const int SIZE,
           double value);

// ARRAY OPERATIONS END
////////////////////////////////////////////////////////////////////////////////
#endif