
#ifndef TRIAL_H_
#define TRIAL_H_

#include<iostream>

using namespace std;

class testClass{
    private://Only the class and friend functions can access private members.
        int num =123123;
        string name;
        int age;

    public://A public member is accessible from anywhere outside the class but within a program.

        testClass();//Constructor Function
        //A constructor is a special type of member function that is called automatically when an object is created.
        //A constructor has the same name as that of the class and it does not have a return type


        ~testClass();//Destructor Function
        //A destructor is a member function that is invoked automatically when the
        //object goes out of scope or is explicitly destroyed by a call to delete .


        //Other Class Member Functions
        //A member function of a class is a function that has its definition
        //or its prototype within the class definition like any other variable
        void speak();
        void setName(string nameNew);
        void setAge(int ageNew);


    protected://Very similar to a private member but  they can be accessed in child classes.


};


#endif // TRIAL_H_
