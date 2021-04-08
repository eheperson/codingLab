#include "Animal.h"

Animal::Animal()
{
    //ctor
    cout<<"ANimal CReated !! "<<endl;
}

/*
Animal::Animal(const Animal& other){
    //copy onstructor function definition
    cout<<"Animal Created with copy"<<endl;

}
*/
Animal::Animal(const Animal& other){
    //copy onstructor function definition
    name = other.name;
    cout<<"Animal Created with copy"<<endl;

}

Animal::~Animal()
{
    //dtor
}

void Animal::setName(string name){
    this->name = name;
    // name = "fefef";  will occure error because of the const keyword
    // const forbit to change any thing n instance
    // if we want the method cannot change anything we must use const keyword
}

void Animal::speak() const{
    cout << "My name is : " << name <<endl;
}
