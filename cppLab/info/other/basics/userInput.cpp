#include<iostream>

using namespace std; 

int main(){
    string name;
    int age;

    cout << "Enter Your Name : " << flush;
    cin >> name;
    cout << " Your Name is : " << name << endl;

    cout << "Enter Your Age : " << flush;
    cin >> age;
    cout << " Your Age is : " << age << endl;

    return 0;
}