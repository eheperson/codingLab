#ifndef PERSON_H_
#define PERSON_H_

#include <iostream>
#include <sstream>
#include<string>

using namespace std;

class Person{
    public:
        //Constructor
        Person();
        // Overloading Constructors
        Person(string nameNew);
        Person(int ageNew);
        Person(string name, int age);

        //Destructor
        ~Person();

        //Other Member Functions
        string toString();


    protected:

    private:
        string name;
        int age;
};

#endif // PERSON_H_
