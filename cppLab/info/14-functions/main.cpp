/////////////////////////////////////
//  Functions Example    ///////////
/////////////////////////////////////
/*
    Functions : Performing special task
        (1) Scope {codes}
        (2) Return type
        (3) name
        (4) parameter list
    
        - Reading Flexibility
        - Specific Process

    Function Structure : 
        <return_type> <function_name>(<parameter_list>){

            body of the function

            return value;
        }

    Calling operatr : ()
*/
#include<iostream>

using namespace std;

// fucntion prototype
// for the functions have decleration but have not definition
int sum(int a, int b);

//function definition
int multiple(int a, int b){

    return a*b;
}

int main(){

    int x = 5;
    int y = 6;

    int s, m;

    //calling functions with calling operator ()
    s = sum(x,y);
    m = multiple(x,y);

    cout << "Sum function result : " << s << endl;
    cout << "Multiple function result : " << m << endl;




    system("Pause");
    return 0;
}



/////////////////////////////////////
//  Functions Example    ///////////
/////////////////////////////////////
