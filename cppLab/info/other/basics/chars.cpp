#include<iostream>

using namespace std;

int main(){

    char cVal = 'g';
    wchar_t wcVal = 'i';

    cout << cVal << endl;
    cout << "Size of char : " << sizeof(char) << endl;

    cout << wcVal << endl;
    cout << "Size of wchar_t : " << sizeof(wchar_t) << endl;


    return 0;
}