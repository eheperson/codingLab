#include "Person.h"

Person::Person()
{
    name = "undefined";
    age = 0;

    cout<<" Location of Objects : "<<this<<endl;
};

Person::Person(string nameNew){
    name = nameNew;
    age = 0;

    cout<<" Location of Objects : "<<this<<endl;
};

Person::Person(int ageNew){
    name = "undefined";
    age = ageNew;

    cout<<" Location of Objects : "<<this<<endl;
};

Person::Person(string name, int age){
    this->name = name;
    this->age = age;

    cout<<" Location of Objects : "<<this<<endl;
};

Person::~Person()
{
    //dtor
};

string Person::toString(){
    stringstream ss;
    string info;

    ss<<"Name : ";
    ss<<name;
    ss<<" Age : ";
    ss<<age;

    info = ss.str();

    return info;

};
