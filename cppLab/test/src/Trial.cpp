#include<iostream>
#include "Trial.h"

using namespace std;

testClass::testClass(){
    cout<<"object created"<<endl;
    name = "Mike";
}

testClass::~testClass(){
    cout<<"object destroyed"<<endl;
}

void testClass::setAge(int ageNew){
    age = ageNew;
}

void testClass::setName(string nameNew){
    name = nameNew;
}

void testClass::speak(){
    cout<<"enivicivokki";
    cout<<num<<endl;
}
