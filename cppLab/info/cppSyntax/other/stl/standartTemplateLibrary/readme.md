#
# Standard Template Library
- A set of tools available in C++ programming platforms.
- Code quickly, efficiently and in generic way.  

## Generic Programming
- Data types not specified in implementation, but rather in its use.
- Compile time polymorphism

## Generic Types in C+ : Templates
- C++ enables generic programming by means of special constructs called 'Templates'

 - Function Template syntax :
temlate <typename T>
T area(T a, T b){
    T result = a*b;
    return result;
}

int x=area<int>(5,10)
double y = area<double>(5.5, 10)