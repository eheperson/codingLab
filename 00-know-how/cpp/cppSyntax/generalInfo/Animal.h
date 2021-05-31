#ifndef ANIMAL_H
#define ANIMAL_H

#include <iostream>
#include <sstream>
#include<string>

using namespace std;


class Animal
{
    private:
        string name;
    public:
        void setName(string name);
        void speak() const ;
        Animal();

        //Copy Constructor
        Animal(const Animal& other);

        /*  Copy Constructor alternatives
        Animal(const Animal& other): {name(other.name);

        Animal(const Animal& other): {name(other.name){
            //if we will use that :

            other.speak();
            cout<<"Animal Created with copy"<<endl;
        };
        */
        virtual ~Animal();

    protected:


};

#endif // ANIMAL_H
