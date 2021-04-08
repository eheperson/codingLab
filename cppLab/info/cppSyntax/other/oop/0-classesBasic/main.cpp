#include<iostream>
#include "essence.h"

using namespace std;

int main(){
    
    essence e1;  //instance or object of class
                // creating an object

    essence e2;  //instance or object of class
                // creating an object

    //instance specifications
    e1.x = 11;
    e1.y = 12;
    e1.z = 13;

    //istance specifications
    e2.x = 21;
    e2.y = 22;
    e2.z = 23;


    cout<<"e1 parameters : " << e1.x <<" - " << e1.y <<" - "  << e1.z<<endl;
    cout<<"e2 parameters : " << e2.x <<" - " << e2.y <<" - "  << e2.z<<endl;


    e1.speak();
    e2.speak();

    system("Pause");
    return 0;
}