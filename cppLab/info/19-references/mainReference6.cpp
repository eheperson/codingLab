#include<iostream>

using namespace std;

struct Data{
    int a, b, c;
};


int* func(){
    // without static keyword 
    // compiller will get error
    static int x = 56;

    /* !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
        Without static keyword,
        we cannot return a reference variable 
        from anywhere to anyehere
        --static keyword is needed at decleretation 
        to return reference variable
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! */
    return &x;
}

int main(){
    //int x = 13;
    //that line of code below means
    // the reference(adress) of a is constant
    //int &const r = x;

    Data mydata;
    Data &r = mydata;
    // for C language
    // struct Data mydata;
    // struct Data &r = mydata;

    r.a = 11;
    cout << " r.a : " << r.a << endl;

    cout << endl;

    int* ptr = func();
    cout << " ptr : " << *ptr << endl;
    return 0;   
}