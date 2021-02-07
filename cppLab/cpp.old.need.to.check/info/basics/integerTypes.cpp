#include<iostream> 

using namespace std;


int main(){
    int val = -54645;
    long int lVal = 34234234123123;
    short int sVal = 23434;
    unsigned int uVal = 234354;

    cout << " Integer Value : " << val << endl;
    cout << "Size of int : " << sizeof(int) << endl;

    cout << " Long Integer Value : " << lVal << endl;
    cout << "Size of long int : " << sizeof(long int) << endl;

    cout << " Short Integer Value : " << sVal << endl;
    cout << "Size of short int : " << sizeof(short int) << endl;

    cout << " Unsigned Integer Value : " << uVal << endl;
    cout << "Size of unsigned int : " << sizeof(unsigned int) << endl;


    return 0;
}