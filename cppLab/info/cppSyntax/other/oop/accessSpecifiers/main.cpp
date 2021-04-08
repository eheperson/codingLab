#include<iostream>
#include "essence.h"

using namespace std;

int main(){
    
    essence e1; //instance or object of class
                // creating an object

    e1.setX(1);
    e1.setY(2);
    e1.setZ(3);

    cout << "ESSENCE PARAMETERS : " << endl;
    e1.getX();
    e1.getY();
    e1.getZ();

    system("Pause");
    return 0;
}